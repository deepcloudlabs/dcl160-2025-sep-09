import gc


class A:
    def __del__(self):
        print("Object is destroyed!")

a = A() # counter: 1
#b = a # counter:2
print("Before assigning a")
#del a
a = None # counter: 0 -> calls __del__()
#gc.collect()
print("After assigning a")