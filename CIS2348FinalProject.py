#Pranav Tetali
#ID 1541822
#Final Project


import csv
from operator import itemgetter
manufacList=[]#manufacturerlist csv
prilist=[]#price list csv
sdlist=[]#service dates list csv
with open("ManufacturerList.csv") as manufacturerlist:
    manufactList=csv.reader(manufacturerlist)
    for line in manufactList:
        manufacList.append(line)#used append to add
with open("PriceList.csv") as pricelist:
    prl = csv.reader(pricelist)
    for line in prl:
        prilist.append(line)#used append to add
with open("ServiceDatesList.csv") as servicedatelist:
    sel = csv.reader(servicedatelist)
    for line in sel:
        sdlist.append(line)#used append to add
new_manufacList=(sorted(manufacList, key=itemgetter(0))) #manufactuerlist sorted by id
new_prilist=(sorted(prilist, key=itemgetter(0))) #price list sorted by id
new_sdlist=(sorted(sdlist, key=itemgetter(0)))#service dates list sorted by id
for x in range(0,len(new_manufacList)):#with append i added prices to manufactuer list
    new_manufacList[x].append(prilist[x][1])
for x in range(0,len(new_manufacList)):#with append i added serice dates to manufactuer list
    new_manufacList[x].append(sdlist[x][1])
completed_list = new_manufacList
full_inventory = (sorted(completed_list, key=itemgetter(1)))
with open('FullInventory.csv','w') as newfile:
    fulinvenwrite = csv.writer(newfile)
    for x in range(0, len(full_inventory)):
        fulinvenwrite.writerow(full_inventory[x])
type_of_item = completed_list
laptop_list = []#list that is only for laptops
phone_list = []#list that is only for phones
tower_list = []#list that is only for towers
for x in range(0,len(type_of_item)):
    if type_of_item[x][2] == "laptop":
        laptop_list.append(type_of_item[x])#added laptop to types of items
    elif type_of_item[x][2] == "phone":
        phone_list.append(type_of_item[x])  # added phones to types of items
    elif type_of_item[x][2] == "tower":
        tower_list.append(type_of_item[x])#added towers to types of items
with open('LaptopInventory.csv','w') as newfile:#file for laptops
    laptopinventwrite = csv.writer(newfile)
    for x in range(0,len(laptop_list)):
        laptopinventwrite.writerow(laptop_list[x])
with open('PhoneInventory.csv','w') as newfile:#file for phones
    phoneinventwrite = csv.writer(newfile)
    for x in range(0,len(phone_list)):
        phoneinventwrite.writerow(phone_list[x])
with open('TowerInventory.csv','w') as newfile:#file for towers
    towerinventwrite = csv.writer(newfile)
    for x in range(0,len(tower_list)):
        towerinventwrite.writerow(tower_list[x])
damagedlist = []#list only for items that are damaged
for x in range(0,len(type_of_item)):
    if type_of_item[x][3] == "damaged":
        damagedlist.append(type_of_item[x])
damagedlist = (sorted(damagedlist, key=itemgetter(4), reverse=True))
with open('DamagedInventory.csv','w') as newfile:#file for damaged items
    damagedinventwrite = csv.writer(newfile)
    for x in range(0, len(damagedlist)):
            damagedinventwrite.writerow(damagedlist[x])
cust_manufactureritem = "init"#constructor helps initialize the attributes
while cust_manufactureritem !="q":#used "q" to exit the query
    cust_manufactureritem = str(input("Enter your manufacturer, or q to exit query:"))#user enters manufacturer, like Apple
    if (cust_manufactureritem == 'q'):#stops query
        continue
    cust_type_of_item = str(input("Please enter your item type: "))#user enters type of item, like phone
    cust_item = []
    for x in range(0,len(completed_list)):
        if cust_manufactureritem in completed_list[x] and cust_type_of_item in completed_list[x]:
            cust_item.append(completed_list[x])
    if len(cust_item) != 0:
        cust_item = sorted(cust_item,key=itemgetter(4), reverse=True)
        print("Your item is: ", cust_item[0])#provides user with the item manufacturer and type
        print("You may, also, consider: ")#provides user with alternatives
        with open("FullInventory.csv", newline='') as full_inventory:#provides inventory
            reader = csv.reader(full_inventory, delimiter=' ', quotechar='|')#field delimiter, provides commas to all fields
            linenum = 0
            for row in reader:
                if linenum == 0:
                    print(', '.join(row))
            else:
                linenum = linenum + 1
    else:
        print("No such item in Inventory")#provides user availability of item

