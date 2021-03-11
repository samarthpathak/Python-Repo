s=input("Enter the sentence\n").upper()  #Input from the user and converting it to uppercase
l=['A','E','I','O','U']  
r=[]  #Creating two empty list to store the result
k=[]
for i in l:
    if i in s:
        r.append(i)               #If vowel is present apeend in list r
        k.append(s.count(i))      #Apeending the count of present vowel
print("Vowels in sentence -",r,"\nEach vowel repeated as -",k)    #Displaying the output
        
