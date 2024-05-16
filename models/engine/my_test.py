#!/usr/bin/python3

from file_storage import FileStorage

sto = FileStorage()
obj1 = sto.new(sto)
obj2 = FileStorage()
print(sto.all())