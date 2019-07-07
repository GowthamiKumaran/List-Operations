'''List Operations'''
LIST = []
N = int(input("Enter the number"))
for i in range(N):
    A = input("Enter the operation you want to perform:").split()
    if len(A) == 3:
        eval("LIST."+A[0]+"("+A[1]+","+A[2]+")")
    elif len(A) == 2:
        eval("LIST."+A[0]+"("+A[1]+")")
    elif len(A) == 1:
        print(LIST)
    else:
        eval("LIST."+A[0]+"()")
		