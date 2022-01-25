datelist=[]
count=1
#Asks for birthday inputs until the total inputs have reached 5. An added detail is that I used %d and a counter so that it tells you how many dates you have added so far.
while len(datelist)<5:
    datelist.append(input("Enter Date %d:"%count))
    count+=1
#Splits the input, so that the day of the month can be converted to integer.
for i in range(5):
    datelist[i]=datelist[i].split()
    datelist[i][1]=int(datelist[i][1])
#Below adds a third value to the list inside the datelist, which is the ammound of days to add to the total days, depending on which month the birthday falls on.
for i in range(5):
    if datelist[i][0]=="January":
        datelist[i].append(0)
    elif datelist[i][0]=="February":
        datelist[i].append(31)
    elif datelist[i][0]=="March":
        datelist[i].append(59)
    elif datelist[i][0]=="April":
        datelist[i].append(90)
    elif datelist[i][0]=="May":
        datelist[i].append(120)
    elif datelist[i][0]=="June":
        datelist[i].append(151)
    elif datelist[i][0]=="July":
        datelist[i].append(181)
    elif datelist[i][0]=="August":
        datelist[i].append(212)
    elif datelist[i][0]=="September":
        datelist[i].append(243)
    elif datelist[i][0]=="October":
        datelist[i].append(273)
    elif datelist[i][0]=="November":
        datelist[i].append(304)
    elif datelist[i][0]=="December":
        datelist[i].append(334)
#Example date entry after this for loop: ['June', 0, 151]
#The added third value is the total days leading up to that month.
#This makes it much easier to sort, because I can just add the days in said month to the total days in previous months, using integers.
chronodate=[]
smallestdatel=1
print()
print("The birthdays in chronological order are:")
#Below sorts the dates and creates a new list in chronological order
for j in range(len(datelist)):
    smallestdate=367
    for i in range(len(datelist)):
        if datelist[i][1]+datelist[i][2]<smallestdate:
            smallestdate=datelist[i][1]+datelist[i][2]
            Sdateival=i
    chronodate.append(datelist[Sdateival])
    del datelist[Sdateival]
stringlist=[]
#Prints the dates
for p in range(5):
    print("%s %s"%(chronodate[p][0],chronodate[p][1]),end=" ")
print()