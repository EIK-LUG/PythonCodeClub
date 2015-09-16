#!/usr/bin/env python3
def pipe(val, *args):
    for func in args:
        val = func(val)
    return val


def trace(fn):

    def build_trace_line(fn, args, ret_val):
        return "    " + fn.__name__ + str(args) + " -> " + str(ret_val) + "\n"

    def wrapped(*args):
        ret_val = fn(*args)
        trace_line = build_trace_line(fn, args, ret_val)
        print(trace_line.ljust(10))
        return ret_val

    return wrapped
