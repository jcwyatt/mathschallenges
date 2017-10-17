palstr = "123301"
print (palstr[0:3])
print (palstr[:2:-1])

for i in range (999,900,-1):
    for j in range (999,900,-1):
        #print(i,"/",j,i*j)
        palstr = str(i*j)
        if palstr[0:3] == palstr[:2:-1]:
            print(palstr)
            print (i,j)
            quit()

print (palstr)
