#!/usr/bin/python3

"""Function that will extract the "class name" from the command line"""

def cls_extractor(line):
    """function that will recieve the line from the command interpreter and parses it
    to extract the class name"""
    splitting = line.split(".")
    
    cls = splitting[0]
    return cls

def commd_extractor(line):
    """function that will recieve the line from the command interpreter and parse it
    to extrac the command name"""
    splitting = line.partition(".")
    not_cmd_yet = splitting[2]
    if "(" in not_cmd_yet and not_cmd_yet[-3] != None:
        splitting2 = not_cmd_yet.split("(")
        cmmd = splitting2[0]
        return cmmd
    else:
        return
    
def id_extractor(line):
    """funtion that will recieve the line from the command interpreter and parse it
    to extract the id of the advanced command"""
    splitting = line.partition('(')
    not_id_yet = splitting[2]
    if "," not in not_id_yet:
        splitting2 = not_id_yet.split(")")
        class_id_quotes = splitting2[0]
        class_id = class_id_quotes.strip('"')
        return (class_id)
    else:
        splitting3 = not_id_yet.split(",")
        class_id_quotes = splitting3[0]
        class_id = class_id_quotes.strip('"')
        return (class_id)
    return