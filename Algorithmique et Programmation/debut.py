def fonctionA():
    x = 11
    print("x = " + str(x))
def fonctionB(y):
    x = 878
    y = y+1
    print("x = " + str(x))
    print("y = " + str(y))
    fonctionA()
    x = 33
    y = 44
    print("x = " + str(x))
    print("y = " + str(y))
fonctionB(42)