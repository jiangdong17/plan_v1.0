

def init():
    global a
    a={}

def setvalue(name,value):
    a[name]=value

def getvalue(name,defalut=None):
    try:
        return a[name]
    except keyerror:
        return defalut