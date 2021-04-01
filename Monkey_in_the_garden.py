n=int(input("Enter the number of trees\n"))   #Taking the input for number of trees from the user
l=[int(x) for x in input("Enter the height of trees\n").split()]      #Taking the height of trees from the user
p=0     #Setting the intial travel time as zero
for i in range(len(l)):          #These loops are checking the distance of each tree from every other tree in the park 
    for j in range(len(l)):      #To find the trees with maximum travel time between them               
        d=l[i]+l[j]+abs(l.index(l[i])-l.index(l[j]))     #Calculating the travel time between two trees
        if d>p:
            p=d                 #If travel time is larger than the previous one, change the value
print("Maximum possible travel time is ",p)   #Displaying the output
    
        
        
