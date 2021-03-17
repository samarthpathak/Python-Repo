d={"Charles":["Coffee","Black","Cold","Medium"],"Patel":["Tea","Regular","Hot","Small"],"Sameer":["Coffee","Regular","Hot","Large"],"X":["Tea","Black","Cold","Large"]}
#Dictionary with keys as names of the customer and values containing  list with the customer pre saved order 
class machine:   # class machine
    global d
    def __init__(self):
        pass
    def new(self,name,item,flav,typ,size):          #Function to create a new saved order for the given customer name
        l=[]
        l.append(item)
        l.append(flav)
        l.append(typ)
        l.append(size)
        d[name]=l                                    #Appending the list in the dictionary for given name
    def priced(self,name):                           #Function to calculate the price of order
        self.name=name
        if d[self.name][0]=="Tea":
            self.price=20
        else:
            self.price=30
        if d[self.name][1]=="Black":
            self.price=self.price+10
        else:
            self.price=self.price+20
        if d[self.name][3]=="Large":
            self.price=self.price+40
        elif d[self.name][3]=="Medium":
            self.price=self.price+30
        else:
            self.price=self.price+20
        print("Your Order: ",*d[name],sep=" ")       #Displaying the order
        print("Your total bill: ",self.price)        #Diplaying the price for the item
            
            
            

ch="Y"
while ch=="Y":
    k=int(input("Enter your choice\n1.Search by name\n2.New customer\n"))  #Taking user choice
    if k==1:                                                  #To search a coffee by name
        name=input("Enter your name: ")
        if name in d.keys():                                #Searching for name in the dictionary
            machine().priced(name)                              
        else:
            print("Name not found")
    elif k==2:                                              #Creating a new customer profile
        name=input("Enter your name: ")
        item=input("What would you like to have Coffee/Tea?\n")
        flav=input("Would you like it Regular/Black?\n")
        typ=input("Would like it Hot/Cold?\n")
        size=input("What cup size do you want Large/Meduim/Small?\n")
        machine().new(name,item,flav,typ,size)
        machine().priced(name)
    ch=input("Would you like to order something else? Y/N\n").upper()               #Asking if customer wants something else
             


