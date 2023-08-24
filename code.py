def cala(x):
    if x[1]=="*":
        print("The output =",(int(x[0])*int(x[2])))
    elif x[1]=="-":
        print("The output =",(int(x[0])-int(x[2])))
    elif x[1]=="+":
        print("The output =", (int(x[0]) + int(x[2])))
    else:
        print("The output =",(int(x[0])/int(x[2])))
expression=list(input("Enter the expression please :\n").split())
cala(expression)
