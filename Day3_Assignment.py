a=int(input("how much height to fight moving (in ft):- "))
print(a)
if (a<=1000):
    print("Safe to Land")
elif (a>1000 and a<=5000):
    print("Bring down to 1000")
else:
    print("Turn Around")
