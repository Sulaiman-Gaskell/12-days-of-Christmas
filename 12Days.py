#Inital List
giftList = ["partridge in a pear tree","turtle doves","french hens","calling birds","gold rings","geese a laying",\
"swans a swimming","maids a milking","ladies dancing","lords of leaping","pipers piping","drummers drumming"]

counter = 1
for thing in giftList:
    #1 2 and 3 have differnt dates (doesnt end in 'th')
    if counter == 1:
        string = ['On the 1st day of Christmas my true love gave to me']
    elif counter == 2:
        string = ['On the 2nd day of Christmas my true love gave to me']
    elif counter == 3:
        string = ['On the 3rd day of Christmas my true love gave to me']
    else:
        string = ['On the',str(counter)+'th, day of Christmas my true love gave to me']

    #Sets up the number of items needed for each thing dependin on how far thru the song you are
    count = []
    for i in range(1,counter):
        count.append(i)

    #Packs it all together using counting in reverse order startimg from counter to 1 being the last thing (stops one before the zero)
    # checks if it the lat item for that day and doesnt't use end so the next string is no conacinated at the end 

    print(*string, end = ' ')
    for currentDay in range(counter, 0, -1):
        if currentDay == 1 and counter != 1:
            print(f'and a {giftList[0]}')
        else:
            print(f'{currentDay} {giftList[currentDay - 1]},', end = ' ')
    print()
   


    counter +=1