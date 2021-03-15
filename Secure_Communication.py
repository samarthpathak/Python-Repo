def incr(s,k):
    for i in range(len(s)):
        if ord(s[i])== 32:               #To convert space to @
            s[i]="@"
        elif ord(s[i]) == 46:
            s[i]="#"                   #To convert "." to #
        elif ord(s[i]) in range(97,123):
            s[i]=ord(s[i])+k            #To encrypt A to Z 
            if s[i]<123:
                s[i]=chr(s[i])
            else:
                s[i]=chr(s[i]%123+97)
        elif ord(s[i]) in range(65,91):
            s[i]=ord(s[i])+k           #To encrypt a to z
            if s[i]<91:
                s[i]=chr(s[i])
            else:
                s[i]=chr(s[i]%91+65)
        elif ord(s[i]) in range(48,58):
            s[i]=ord(s[i])+k             #To encrypt 0 to 9
            if s[i]<58:
                s[i]=chr(s[i])
            else:
                s[i]=chr(s[i]%58+48)
            
print("Hello MIT CELL:")
k=int(input("Please enter k value to shift tranform message: "))               #Taking the shift value key for encrypting
s=list(input("Now please type your message: "))                                #Taking the message
l=s.copy()                  #Copying list to another list 
incr(l,k)                   #Calling Function to encrypt the message
print("You send-","".join(l))      
print("\nHello Instructor:\nYou got a message: ","".join(l))
m=int(input("To read this in original please type k value provided by Cell: "))  #Taking the key from the reciever
if k==m:
       print("Original Message: ","".join(s))                   #If key matches print the original message
else:
    print("Error in k value")
