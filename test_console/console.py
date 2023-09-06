#!/usr/bin/python3
"""console Test"""
from cmd import Cmd
from parse_functions.class_extractor import cls_extractor, commd_extractor, id_extractor

class Testconsole(Cmd):
    """This test console will parse the command line"""
    
    prompt = "(hbnb) "
    
    def precmd(self, line):
        """parses basic commands"""
        
        if "." in line:
            parse_line = line[:]
            if parse_line[-2] != "(" and parse_line[-1] != ")":
                return line
            
            else:
                if "," in parse_line:
                    print("comma exists")
                else:                    
                    if '"' in parse_line and "," not in parse_line:
                        cls = cls_extractor(parse_line)
                        cmmd = commd_extractor(parse_line)
                        cls_id = id_extractor(parse_line)
                        formatkey = f"{cmmd} {cls} {cls_id}"
                        return formatkey
                    
                    else:
                        
                        cls = cls_extractor(parse_line)
                        cmmd = commd_extractor(parse_line)
                        formatkey = f"{cmmd} {cls}"
                        return formatkey
        
        return line
    
    def do_quit(self, line):
        print("Exiting the console via quit()")
        quit()
    
    def do_EOF(self, line):
        print("Exiting the console via ctrl + d")
        return True
    
    def emptyline(self):
        return super().emptyline()
    
    def do_printline(self, line):
        print(line)

if __name__ == "__main__":
    Testconsole().cmdloop()