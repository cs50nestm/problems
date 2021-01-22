import check50
import check50.c

@check50.check()
def exists():
    """HelloName.c exists"""
    check50.exists("HelloName.c")

@check50.check(exists)
def compiles():
    """HelloName.c compiles"""
    check50.c.compile("HelloName.c", lcs50=True)

@check50.check(compiles)
def emma():
    """responds to name Emma"""
    check50.run("./HelloName").stdin("Emma").stdout("Hello, Emma!").exit()

@check50.check(compiles)
def rodrigo():
    """responds to name Rodrigo"""
    check50.run("./HelloName").stdin("Rodrigo").stdout("Hello, Rodrigo!").exit()
