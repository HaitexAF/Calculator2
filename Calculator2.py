while True:
    Operation = input("send your Operation... ")
    if "+" in Operation:
        j = Operation.index("+")
        x1 = int(Operation[:j])
        y1 = int(Operation[j+1:])
        print(f"{x1} + {y1} = {x1 + y1}")
    elif "-" in Operation:
        m = Operation.index("-")
        x2 = int(Operation[0:m])
        y2 = int(Operation[m+1:])
        print(f"{x2} - {y2} = {x2 - y2}")
        
    elif "*" in Operation:
        z = Operation.index("*")
        x3 = int(Operation[0:z])
        y3 = int(Operation[z+1:])
        print(f"{x3} * {y3} = {x3 * y3}")
    elif "/" in Operation:
        t = Operation.index("/")
        x4 = float(Operation[0:t])
        y4 = float(Operation[t+1:])
        print(f"{x4} / {y4} = {x4 / y4}")
    else:
        raise ValueError
