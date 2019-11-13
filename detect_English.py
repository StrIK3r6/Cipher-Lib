
def Open_File():
   
    f.open('dictionary.txt' 'r')

    Dict=[]
    for words in f.readline():
        Dict.append(words)

    f.close()

    Dictionary=''.join(Dict)
    return Dictionary


def filter_letter(ctext):
  
    letters=[]
    for word in ctext:
        if word in check_array:
            letters.append(word)

    letters=''.join(letters)
    return letters


DictionaryWords=Open_File()

          
def word_Count(letters):
   
    matchScore=0
    letter=filter_letter(ctext)
    
    if letter==[]:
        return 0

    for word in letter:
        if word in DictionaryWords:
            matchScore+=1
     
    return float(matchScore)/len(letter)   



def is_english(ctext,letterPercent=85,wordPercent=20):
    
    actulLetterPercent=float(len(filter_letter(letters)))/len(ctext)*100
    LetterLimit=actulLetterPercent >= letterPercent  
    WordLimit=word_Count(letters)*100 >= wordPercent

    return LetterLimit & WordLimit


if __name__ == '__main__':
     
   import string

   check_array=string.ascii_lowercase + '\n\t ' + string.ascii_uppercase

   is_english(ctext)

