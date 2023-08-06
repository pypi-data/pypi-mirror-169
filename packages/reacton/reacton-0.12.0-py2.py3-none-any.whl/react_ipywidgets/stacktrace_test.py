import sys

from .stacktrace import Code, Frame


def test_1():
    def func2():
        try:
            assert False
        except AssertionError:
            traceback = sys.exc_info()[2]
            import pdb

            pdb.set_trace()

    def func():
        func2()

    func()
