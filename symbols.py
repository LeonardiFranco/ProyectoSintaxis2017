pass
# from lex import *

# class Type(Word):
#     def __init__(self, s, t, **kwds):
#         super().__init__(s,t, **kwds)

# _Num = Type('num', Tag.TYPE)
# _Char = Type('char', Tag.TYPE)
# _Bool = Type('bool', Tag.TYPE)

# class Env():
#     def __init__(self, n):
#         self.table = {}
#         self.prev = n

#     def put(self, w, i):
#         self.table[w]=i

#     def get(self, w):
#         e = self
#         while e:
#             found = e.table.get(w)
#             if found:
#                 return found
#             e = e.prev
#         return None