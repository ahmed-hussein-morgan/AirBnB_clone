#!/usr/bin/python3

from file_storage import FileStorage

sto = FileStorage()
obj1 = sto.new(sto)
print(sto.all())