import pymongo

client = pymongo.MongoClient()
mydb = client["srima"]
mycol = mydb['srima']

def shopping_list():
    n=1
    print("\nITEM LIST")
    for x in mycol.find({}):
        print(n,":",x['item'],)
        n+=1

def read(name):
    print("ITEM DETAILS")
    for x in mycol.find({'item':name}):
        print("ITEM NAME : ",x['item'])
        print("COST OF ITEM : ",x['cost'],"Rs")


def delete(name):
    print("REMOVING ITEM FROM COLLECTION\n")
    myquery = { "item": name }

    mycol.delete_one(myquery)
    print(name,"removed for collection")


def create(item,cost):
    print("ADDING NEW ITEM TO COLLECTION\n")
    mydict = { "item": item, "cost": cost }

    x = mycol.insert_one(mydict)
    print(item,"added to the collection with cost ",cost,"Rs")


def update():
    print("UPDATION THE COST OF ITEM\n")
    item=input("Enter the name of item to br updated : ")
    cost=int(input("Enter the new cost of the item : "))
    myquery = { "item": item}
    newvalues = { "$set": { "cost": cost } }
    mycol.update_one(myquery, newvalues)
    print("update the cost of",item)
    
def buy_item():
    data=[]
    total_cost=0
    n=int(input("Enter the number of item to buy : "))
    for a in range(1,n+1):
        print("Enter the item",a,": ")
        item = input()

        for x in mycol.find({'item':item}):
            total_cost+=x['cost']
            data.append(x['item'])
            data.append(x['cost'])

    print("ITEM BUYING LIST")
    for x in range(0,len(data),2):
        
        print(data[x],"of Rs",data[x+1])
    print("\nTotal cost : ",total_cost)

while True:
    print("""
SHOPPING 
1.SHOW LIST(DISPLAY ALL THE ITEMS)
2.CREATE(ADDING ITEM)
3.SEE THE COST(READ THE COLLECIONS)
4.UPDATE(CHANGE THE COST OF  ITEM)
5.DELETE(REMOVE FROM COLLECTION)
6.BUY ITEMS
7.EXIT
""")

    ch = int(input("Enter your choice : "))
    if ch==1:
        shopping_list()
        print()
        print("Press enter to continue")
        input()

    elif ch==2:
        item=input("Enter the name of item : ")
        cost=int(input("Enter the cost of the item : "))
        create(item,cost)
        print()
        print("Press enter to continue")
        input()

    elif ch==3:
        name = input("Enter the name of the product : ")
        print()
        read(name)
        print()
        print("Press enter to continue")
        input()

    elif ch==4:
        update()
        print()
        print("Press enter to continue")
        input()

    elif ch==5:
        print("DELETING")
        name = input("Enter the name of the product : ")
        delete(name)
        print()
        print("Press enter to continue")
        input()

    elif ch==6:
        buy_item()
        print()
        print("Press enter to continue")
        input()

    elif ch==7:
        break

    else:
        print("INVALID CHOICE")

