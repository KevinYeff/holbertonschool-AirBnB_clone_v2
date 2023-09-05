#!/usr/bin/python3
"""console Test"""
from cmd import Cmd

class Testconsole(Cmd):
    """This test console will parse the command line"""
    
    prompt = "(hbnb) "
    
    def do_quit(self, line):
        print("Exiting the console via quit()")
        quit()
    
    def do_EOF(self, line):
        print("Exiting the console via ctrl + d")
        return True
    def emptyline(self):
        return super().emptyline()

if __name__ == "__main__":
    Testconsole().cmdloop()