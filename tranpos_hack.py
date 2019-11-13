import transpos_decrypt,detect_English,time

def trans_hack():
    ctext=input("Enter your message: ")


    key=1
    print("Starting decryption process>>>>>>> ")

    while True:

        print()
        print()
        print("Starting decryption process  with key as %d....",%(key))

        hacked_messgae=transpos_decrypt.decrypt(key,ctext)

        if detect_English.isEnglish(hacked_message):
           
            print()
            print(hacked_message)
            print()
            ans=input("Would u like to continue with the decryption procss(y/n): ")
           
           if ans.lower().startswith('n'):
               
                print("Decryption Finished!!")
                time.sleep(6)
                sys.exit()

        print("continuing with the deryption process.......")
        time.sleep(2)

        key+=1

if __name__ == '__main__':
    trans_hack()








