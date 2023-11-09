#!/usr/bin/python3
if _name_ == "_main_":
    import hidden_4 as extra


for x in dir(extra):
    if x[0:2] != "__":
        print("{:s}".format(x))
