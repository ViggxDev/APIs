#Comments = input type

#Errors
def err_list():
    return "There was an error executing your command"

#Lists
#d = digits
def d(l):
    for x in l:
        if not str(x).isdigit():
            return False
    return True

#rd = remove duplicates
def rd(l):
    for x in l:
        if l.count(x) >= 2:
            l.remove(x)
    return l

#Sorted list (increasing) without duplicates
def srd_i(l):
    return sorted(rd(l))

#Sorted list (decreasing) without duplicates
def srd_d(l):
    return sorted(rd(l))[::-1]

#Sorted list (increasing)
def si(l):
    return sorted(l)

#Sorted list (decreasing)
def sd(l):
    return sorted(l)[::-1]

#First target --> return index of first element
def ft(l, t):
    for i,e in enumerate(l):
        if e == t:
            return i
    return err_list()

#Reverse list
def r(l):
    return l[::-1]