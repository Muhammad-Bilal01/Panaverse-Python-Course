name:str = "Bilal"
print(name)
print(type(name))  # type of the object
print(id(name)) # pysical address
print([i for i in dir(name) if "__" not in i]) # method and attributes