# from .base import BaseConversion, LazyEscapedString, This
#
#
# class Cumulative(BaseConversion):
#     PREV = LazyEscapedString("prev_value")
#
#     def __init__(self, reduce_expression, prepare_first=This):
#         self.reduce_expression = reduce_expression
#         self.prepare_first = prepare_first
#
#
# def smart_f(locals_, function_name):
#     def reset():
#         locals_[function_name] = f1
#
#     def f1():
#         locals_[function_name] = f2
#         return 1
#
#     def f2():
#         return 2
#
#     reset()
#
#
# smart_f(locals(), "f")
