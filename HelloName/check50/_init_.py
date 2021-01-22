from check50 import *

class HelloName(Checks):

@check()
def exists(self):
    """HelloName.c exists"""
    self.require("HelloName.c")

@check("exists")
def compiles(self):
    """HelloName.c compiles"""
   self.spawn("clang -o HelloName HelloName.c -lcs50 -lm").exit(0)

@check("compiles")
def emma(self):
    """responds to name Emma"""
    self.spawn("./HelloName").stdin("Emma").stdout("Hello, Emma!").exit(0)

@check50.check(compiles)
def rodrigo(self):
    """responds to name Rodrigo"""
    check50.run("./HelloName").stdin("Rodrigo").stdout("Hello, Rodrigo!").exit(0)
