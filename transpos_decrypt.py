def decrypt(key,message):

    ctext=message
    
    c_len=len(ctext)
    col_no=round(c_len/key)
    row_no=key

    void_cell=col_no*row_no-c_len
    
    for i in range(void_cell):
        ctext+=" "

    ptext=[]
    plain_text=""
    k=0

    for i in range(row_no):
        m=[]
        for j in range(col_no):
            m.append(ctext[k])
            k+=1
        
        ptext.append(m)      
    

    for a in range(col_no):
        for b in range(row_no):
            print(ptext[b][a],end=" ")
    
    

if __name__=='__main__':
   
    cipher_text=input("Enter text to be decrypted: ")
    key=int(input("Enter the key: "))
    decrypt(key,message)
