x = 42 # scalar variables
# 4, 8, 15, 16, 23, 42, ... ?
# "jack", "jill", "jane", "john", "jim", "jack", "sun", "kim", ... ?
Collections: tuple, list, set, dictionary
I. Linear Collections:  tuple, list, set
   A. tuple: ordered, immutable, allow duplicates -> vector
   jack = ("jack bauer", 100000, "TR1", "IT", True, 1956)
   B. list: ordered, mutable, allow duplicates
   salaries = [40_000, 80_000, 150_000, 160_000, 230_000, 420_000, 150_000, 160_000, 230_000, 150_000]
   names = ["jack", "kim", "jane", "john", "jim", "jack", "sun", "kim"]
   C. set: unordered, mutable, no duplicates/unique values
   salaries = {40_000, 80_000, 150_000, 160_000, 230_000, 420_000}
   names = {"jack", "kim", "jane", "john", "jim", sun"}
II. Associative Collections: dictionary
    A. dict: key -> value, key unique, unordered, mutable, unique keys
     salaries = {"jack": 40_000, "kim": 80_000, "jane": 150_000, "john": 160_000, "jim": 230_000, "sun": 150_000}
     area_codes = { "ankara": 312, "istanbul": {"anadolu": 216, "avrupa":212}, "izmir": 232}
     area_codes["istanbul"]["avrupa"] # 212

I. Python Interpreters:
PyPy
IronPython
Cython
Jython
...

II. set() -> red-black tree, balanced tree
             in
             add()
    list() -> dynamic array
              [index] -> O(1)
              append() -> O(1)
              insert() -> O(n)
              pop() -> O(1)
              remove() -> O(n)
              sort() -> O(n log n)
              reverse() -> O(n)
              len() -> O(1)
              in -> O(n)
    dict() -> hash table
              ["key"] = "value" -> O(1)
              key in dict() -> O(1)
    deque() -> double-ended queue
              append() -> O(1)
              appendleft() -> O(1)
              pop() -> O(1)
              popleft() -> O(1)
              extend() -> O(n)
              extendleft() -> O(n)
              insert() -> O(n)
              remove() -> O(n)
              reverse() -> O(n)