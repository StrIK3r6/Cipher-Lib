import string

def Caesers(message,key,mode):
    
    result = ''
    message=message.upper()
    letter=string.ascii_uppercase

    for i in message:
       
        counter=letter.find(i)
    
        if mode=="encrypt":
            counter+=key

        if mode=="decrypt":
            counter-=key

        if counter>26:
            counter-=26

        if counter<0:
            counter+=26

        result+=letter[counter]

    return result


if __name__ == '__main__':
    

    print("Choose an option: ")
    print()
    print("ENCRYPT [1]")
    print("DECRYPT [2]")
    choice=int(input("Your choice: "))
    if choice==1:
        mode="encrypt"
    if choice==2:
        mode="decrypt"
    print()    
    message=input("Enter the message to " + mode + ":")
    key=int(input("Enter the key: "))
    
    res=Caesers(message,key,mode)
    print(res)



