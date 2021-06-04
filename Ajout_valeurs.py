test = [2,0,2,1]
cum = 0
tabs = [0,0,0,0]
n = 10

for k in range(n):
    for i in range(4):
        cum = 0
        for j in range(4):
            if i != j:
                cum = cum + test[j]
            tabs[i] = cum
    test = tabs
    tabs = [0,0,0,0]
    print(test)



