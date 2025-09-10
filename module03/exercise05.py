import gc

numbers = [4,8,15,16,23,42]
del numbers[-3:]
gc.collect()
