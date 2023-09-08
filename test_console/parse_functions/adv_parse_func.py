#!/usr/bin/python3
"""Advanced functions"""

def args_extractor(line):
    """This function will parse the command line to extract the attributes"""
    splitting = line.partition(",")
    not_parameters_yet = splitting[2]
    cleaning = not_parameters_yet.strip()
    pseudo = cleaning.split(")")

    
    if pseudo[0][1] == '{' and pseudo[0][-1] == '}':
        parameters = eval("{" + pseudo[0] + "}")
        if isinstance(parameters, dict):
            return (parameters)
    
    return pseudo[0]
    