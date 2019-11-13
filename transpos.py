import string

def Railfence():
    rand_list=string.ascii_letters
    
    message=input("Enter the message: ")
    initial_len=len(message)

    message=message.replace(' ','')
    print("replaced message: ",message)

    while(len(message)%5!=0):

         rand_char=rand_list[randint(0,len(rand_list))]
         message=message+rand_char
    

    print(message)
    ctext=''        
    count=0
    j=0
    i=j

    while(count<len(message)):
        if(i>len(message)-1):
            j+=1
            i=j
        ctext=ctext+message[i:i+1]
        i+=4
        count+=1
        print(ctext)

    final_text=[ctext[i:i+5] for i in range(0,initial_len,5)]
    final_text=''.join(final_text)
    print(final_text)

if __name__=='__main__':    
    Railfence()

