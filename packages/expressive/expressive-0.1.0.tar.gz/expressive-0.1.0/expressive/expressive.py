#!/usr/bin/env python3

import sys

# symbols are stored as an ordered dict
# TODO consider collections.OrderedDict for older python support
#   https://docs.python.org/3.6/whatsnew/3.6.html#new-dict-implementation
# 3.6+ required for f-strings PEP 498
# what is the oldest version that can be supported with numba? probably 3.7
#   https://numba.readthedocs.io/en/stable/release-notes.html#version-0-56-0-25-july-2022
# TODO warn instead of hard fail for N+1
VERSION_PYTHON_MIN = (3, 7)
VERSION_PYTHON_MAX = (3, 10)
if not (VERSION_PYTHON_MIN <= sys.version_info[:2] <= VERSION_PYTHON_MAX):
    msg = f"Python must be between v({VERSION_PYTHON_MIN}) and v{VERSION_PYTHON_MAX}"
    if __name__ == "__main__":
        sys.exit(msg)
    raise ImportError(msg)

import warnings

import numba  # is a direct import sensible here?
import numpy
import sympy


class ArgsValidationError(TypeError):
    pass


class Expressive:

    def __init__(self, expr, build_with_args=None, rebuild_callback="warn"):
        """ create a new Expressive instance based upon expr

            optionally immediately build with build_with_args
            if not built, build will be lazy unless .build() is called
        """
        self._expr = expr  # assert str or sympy expression (also allow/prefer LaTeX)
        self.signatures = []  # FUTURE: store more information such as build duration
        assert callable(rebuild_callback) or rebuild_callback in ("warn", "raise", "ignore")
        self.rebuild_callback = rebuild_callback
        if build_with_args is not None:
            self.build(**build_with_args)

    def build(self, *, signatures=(), sample_data=None):
        """ build and compile the .fn property from signatures and/or given data
        """
        # TODO assert sample_data is a dict of numpy arrays
        if hasattr(self, "fn") and not signatures and not self.signatures and not sample_data:
            raise ValueError("already built, but building again with no arguments")

        # generate a signature if needed
        if sample_data is not None:
            # FUTURE matrix and other type support
            # assert all(isinstance(v, (numpy.ndarray, numpy.matrix)) for v in sample_data.values())
            assert all(isinstance(v, numpy.ndarray) for v in sample_data.values())
            data_sig = tuple(numba.typeof(sample_data[k]) for k in sample_data)
            if data_sig not in self.signatures:  # TODO option to raise?
                if self.signatures:
                    msg = f"adding data signature to signatures: {data_sig}"
                    if callable(self.rebuild_callback):
                        self.rebuild_callback(msg, data_sig, self.signatures)  # TODO define API
                    elif self.rebuild_callback == "warn":
                        warnings.warn(msg, RuntimeWarning)
                    elif self.rebuild_callback == "raise":
                        raise RuntimeError(msg)
                    elif self.rebuild_callback == "ignore":
                        pass  # lazy builds for busy callers
                    else:
                        raise Exception(f"BUG: rebuild_callback is not callable or appropriate string: {repr(self.rebuild_callback)}: {msg}")
                self.signatures.append(data_sig)
        elif not self.signatures:
            # TODO could be a ResourceWarning, though it's ignored by default..
            warnings.warn("warning: no signatures yet: build(s) will be lazy")

        self.signatures.extend(signatures)
        # opportunity to fix unusable symbol names
        self.expr = sympy.parse_expr(self._expr)
        # TOOD allow caller to pass dict of symbols
        #   use symbols in expr if given
        #   asserts for exactly the same or <=N degrees more
        self.symbols = {s.name: s for s in self.expr.free_symbols}
        # lexical sort which should be stable (sorted(d) is a list of keys)
        self.symbols = {a: self.symbols[a] for a in sorted(self.symbols)}

        # compile the callable function
        self._fn_simple = sympy.lambdify(self.symbols.values(), self.expr)
        self.fn = numba.jit(  # FUTURE consider timing each signature build
            self.signatures or None,
            nopython=True,
            fastmath=True,  # TODO allow toggle
            parallel=True,  # TODO allow toggle
        )(self._fn_simple)

    def __call__(self, *args, **kwargs):
        """ make instance callable, passing to the .fn() method
            if not built (lazy mode), build
        """
        # FIXME is this overly instructive, could be better described, or a bad API?
        try:
            if args:
                if len(args) != 1 or not isinstance(args[0], dict):
                    raise ArgsValidationError
                kwargs.update(args[0])
            elif not kwargs:
                raise ArgsValidationError
        except ArgsValidationError as ex:
            raise ArgsValidationError("expected dict mapping {symbol:numpy collection}") from ex
        if not hasattr(self, "fn"):
            self.build(sample_data=kwargs)
        # opportunity to extract kwargs, especially rebuild without warn/error
        result = self.fn(**kwargs)

        return result

    # TODO offer chunking iterator method?
    #   warn when size is too low (also is 1 ever reasonable?)
    #   is it better to integrate with a distributed system?

    def analyze(self, data_test, mapper_results=None):
        """ analysis method

            mapper_results to be a dict of known inputs to outputs

            TODO stats to help sample data_test
              avoiding bikeshedding for now
              don't report confidence
        """
        if not isinstance(data_test, dict):
            raise ArgsValidationError("data_test must be a dict")
        if not hasattr(self, "fn"):
            self.build(sample_data=data_test)
        # TODO random engine
        #   consider making a property or keep in config
        #   allow user to set seed
        rng = numpy.random.default_rng()

        data_len = len(next(iter(data_test.values())))  # length of first collection
        # TODO infer or get count from user (certainty -> compute)
        size_sample = min(1000, data_len)
        data_sample_indicies = rng.choice(range(data_len), size_sample, replace=False)

        # is there any reason to construct a new collection?
        # data_sampled = {k: numpy.take(v, data_sample_indicies) for k, v in data_test.items()}

        # TODO offer N() for NaN and Infinity
        results_cmp = []
        for data_sample_index in data_sample_indicies:
            # TOOD does this work for matrix outputs?
            row = {k: data_test[k][data_sample_index] for k in data_test}
            # TODO allow setting percision
            # FIXME is there any reason to prefer N() to .evalf()?
            # result = self._fn_simple.evalf(subs=row))
            single_value = sympy.N(self.expr.subs(row))
            # TODO also assert isclose if mapper_results is not None
            results_cmp.append(single_value)
        results_cmp = numpy.array(results_cmp, dtype="float32")  # FIXME results type from user or jit
        results_jit = self(data_test)
        results_jit_subset = numpy.take(results_jit, data_sample_indicies)  # just the matching indicies

        # comparison settings?
        # https://docs.sympy.org/latest/modules/evalf.html#accuracy-and-error-handling

        # https://numpy.org/doc/stable/reference/generated/numpy.isclose.html
        isclose = numpy.isclose(
            results_cmp,
            results_jit_subset,
            rtol=1e-4,  # TODO add toggle
        )

        # TODO find severe discontinuities
        #   note that these may not be errors for piecewise or asymptotic functions
        #   but most will be within a margin of their neightboring values

        # TODO compare different modules for lambidify
        #   https://docs.sympy.org/latest/modules/utilities/lambdify.html#sympy.utilities.lambdify.lambdify
        # sample results and use N()
        #   plot values
        #   real closeness (floating point)
        #   estimate speedup

        # TODO return some result object
        #   allow optional laziness?
        #   consider a dict for now too

        results = {
            "size_sample": size_sample,
            # "results_cmp": results_cmp,
            # "results_jit_subset": results_jit_subset,
            # "isclose":     isclose,  # FIXME this needs a better name
            "isclose_b":   all(isclose),
            "bad_members": {
                "results_cmp":        results_cmp[~isclose],
                "results_jit_subset": results_jit_subset[~isclose],
            },
            "confidence":  "no confidence for now!",
            # random seed
            # signature(s) used
            # library versions
        }

        return results
