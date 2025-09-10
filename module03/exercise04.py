import gc
gc.disable()
fullname="jack shephard"
print(fullname.title()) # after printing -> garbage collector
print(fullname.capitalize())  # after printing -> garbage collector
print(fullname)
gc.enable()
gc.collect() # trigger garbage collector