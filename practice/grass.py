#由1-4组成的不同的每个位都不同的三位数

for i in range(1,5):
    for n in range(1,5):
        for q in range (1,5):
            if i != n and n != q and q != i:
                print (i,n,q)
