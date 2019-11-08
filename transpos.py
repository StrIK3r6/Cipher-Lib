def transpose():
   
    message=input("Enter the message: ")
    key=int(input("Enter the key: "))
    message_len=len(message)

    x=1
    col_no=0

    while(col_no<message_len):
         x+=1
         col_no=key*x


    for extras in range(col_no-message_len):
        message+=" "

    mesage_chunk=[message[i:i+key] for i in range(0,message_len,key)]
   
    i=0
    j=0
    ctext=[]

    while j<key:
        ctext_chunk=''
        while i<x:
            ctext_chunk+="".join(mesage_chunk[i][j])
            i+=1
        
        ctext.append(ctext_chunk)
        print(ctext)
        i=0
        j+=1
   
    ''.join(ctext)
    print(ctext)

if __name__=='__main__':
    transpose()


    
