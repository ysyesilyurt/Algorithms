#!/usr/bin/env python

def main():
    decision_tree = input("Please enter the decision tree list: \n")
    variable_value = input("Please enter the variable value list: \n")
    print query(decision_tree, variable_value)

def query(decision_tree, variable_value):
    if isleaf(decision_tree[0]):
        return decision_tree
    else:
        if checker(decision_tree[0]) == True:
            return query(decision_tree[1], variable_value)
        else:
            return query(decision_tree[2], variable_value)

def finder(variable, variable_value):
    if type(variable) == str:
        for tpl in variable_value:
            if tpl[0] == variable:
                return tpl[1]
        print variable + " value is not given!"
        exit(0)
    else:
        return variable

def checker(lst):
    if lst[0] == '==':
        return finder(lst[1], variable_value) == finder(lst[2], variable_value)
    elif lst[0] == '!=':
        return finder(lst[1], variable_value) != finder(lst[2], variable_value)
    elif lst[0] == '<':
        return finder(lst[1], variable_value) < finder(lst[2], variable_value)
    elif lst[0] == '>':
        return finder(lst[1], variable_value) > finder(lst[2], variable_value)
    elif lst[0] == "in":
        return finder(lst[1], variable_value) in finder(lst[2], variable_value)
    elif lst[0] == "and":
        for i in range(1, len(lst)):
            if checker(lst[i]) == False:
                return False
        else:
            return True
    elif lst[0] == "or":
        for i in range(1, len(lst)):
            if checker(lst[i]) == True:
                return True
        else:
            return False
    elif lst[0] == "not":
        if checker(lst[1]) == True:
            return False
        else:
            return True
    else:
        print "Operator " + lst[0] + " is not defined in decision tree!"
        exit(0)

def isleaf(lstt):
    return len(lstt) == 1

if __name__ == "__main__":
    main()

