"""
immutability -> object pooling/caching
"""
name1 = "kate austen"
name2 = "kate austen"
name3 = "kate austen"
name3.upper() # "KATE AUSTEN" -> garbage collector
name1 = "jack shephard"