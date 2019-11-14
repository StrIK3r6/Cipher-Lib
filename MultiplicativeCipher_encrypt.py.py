import string,math

def encrypt(ptext,key):

    let_num_map = {}
    num_let_map = {}
    num = 0
    letters_and_symbols = string.ascii_letters + string.digits + string.punctuation + " "

    lent=len(letters_and_symbols)

    for char in letters_and_symbols:
       
        let_num_map[num]=char
        num_let_map[char]=num
        num+=1
    
    if key==0 or key==1 or math.gcd(key,lent)!=1:
       
        print("Key value is invalid or entered key is unsecure!!!")
        key=int(input("Enter new key: "))
    
    num_map = {}
    cipher_symbols = {}
 
    for i in range(lent):
        
        num_map[i]=(i*key)%lent
        cipher_symbols[(i*key)%lent]=let_num_map[(i*key)%lent]
    
    ctext = ""

    for letter in ptext:
            
        newNum=num_map[num_let_map[letter]]
        ctext+=cipher_symbols[newNum]

    print(ctext)

if __name__ == '__main__':

    message=input("Enter the text you want to encrypt: ")
    key=int(input("Enter the key [Do not set key as 0 or 1]: "))
    encrypt(message,key)
