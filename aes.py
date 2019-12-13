
from Crypto.Cipher import AES

def aes_ECB_Encrypt(pt):
    
    key="YELLOW SUBMARINE"
    ctext=AES.new(key,AES.MODE_ECB)

    ct=ctext.encrypt(pt)

    return ct

def aes_ECB_Decrypt(ct):

    key="YELLOW SUBMARINE"
    PT=AES.new(key,AES.MODE_ECB)

    ptext=PT.decrypt(ct)

    return ptext

if __name__ == '__main__':

    pt="HELLO WORLD 1234"
    print()

    message=aes_ECB_Encrypt(pt)

    print(message)
    print()

    ct=message
    print()

    message=aes_ECB_Decrypt(ct)

    print(message)
