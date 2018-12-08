from meaningFunctions import cosine_sim
# from meaningFunctions import cosine_sim_method2
from smallHelperFunctions import toPinyin
from smallHelperFunctions import getEnglishLastName
from smallHelperFunctions import isEnglish
from bagOfWordsFunctions import getBadOfWords



import colorama
from colorama import Fore, Back, Style
colorama.init()


#Initialize EnglishNames list
file = open('EnglishFirstNames_Male.txt', 'r') 
EnglishNames_Male = []
for line in file: 
    EnglishNames_Male.append(line[:-1]) #-1 to get rid of the \n character
file = open('EnglishFirstNames_Female.txt', 'r') 
EnglishNames_Female = []
for line in file: 
    EnglishNames_Female.append(line[:-1]) #-1 to get rid of the \n character


    
#Initialize ChineseNames list
file = open('ChineseFirstNames_Male.txt', 'r') 
ChineseNames_Male = []
for line in file: 
    ChineseNames_Male.append(line[:-1]) #-1 to get rid of the \n 

file = open('ChineseFirstNames_Female.txt', 'r') 
ChineseNames_Female = []
for line in file: 
    ChineseNames_Female.append(line[:-1]) #-1 to get rid of the \n character
   
file = open('ChineseLastNames.txt', 'r') 
ChineseLastNames = []
for line in file: 
    ChineseLastNames.append(line[:-1]) #-1 to get rid of the \n 
   

PinyinNames_lastname = []
PinyinChineseDict_lastname = {}
for name in ChineseLastNames:
    pinyinName = toPinyin(name, False)
    PinyinNames_lastname.append(pinyinName)
    PinyinChineseDict_lastname[name] = pinyinName


#Convert all ChineseNames to PinyinNames list
PinyinNames_Male = []
PinyinNames_Female = []
PinyinChineseDict = {}
for name in ChineseNames_Male:
    pinyinName = toPinyin(name, False)
    PinyinNames_Male.append(pinyinName)
    PinyinChineseDict_lastname[name] = pinyinName
for name in ChineseNames_Female:
    pinyinName = toPinyin(name, False)
    PinyinNames_Female.append(pinyinName)
    PinyinChineseDict_lastname[name] = pinyinName

    
# print(len(EnglishNames_Male))
# print(len(EnglishNames_Female))
# print(len(ChineseNames))
# print(len(PinyinNames))

#========Meaning:
ch_char_meaning_map = {}
file_ch_chars = open('Meaning/ChineseCharacters.txt', 'r') 
file_ch_meanings = open('Meaning/ChineseCharacters_meaning.txt', 'r') 


for lineA, lineB in zip(file_ch_chars, file_ch_meanings):
    ch_char_meaning_map[lineA[:-1]] = lineB[:-1]





#================Two methods to get recommended Chinese names================

import Levenshtein
import queue as Q

def getChineseNames(EnglishName, num, gender):
    q = Q.PriorityQueue()

    if gender == "M":
        for (idx, pyname) in enumerate(PinyinNames_Male):
            similarity = Levenshtein.ratio(EnglishName, pyname)
            q.put((-similarity,ChineseNames_Male[idx]))#python priority queue uses min heap, we use -similarity
    else:
         for (idx, pyname) in enumerate(PinyinNames_Female):
            similarity = Levenshtein.ratio(EnglishName, pyname)
            q.put((-similarity,ChineseNames_Female[idx]))#python priority queue uses min heap, we use -similarity
            
    recChineseNames=[]
    for i in range(num):
        recChineseNames.append(q.get()[1])#get returns tuple if (priority,str)
       
    print(Fore.CYAN + "\nHi %s, here are your %d recommendations for a Chinese name by lexical similarity: " % (EnglishName, num)) 
    print(recChineseNames)
    return recChineseNames

    
def getChineseLastName(lastname, num):
    
    q = Q.PriorityQueue()

    for (idx, pyname) in enumerate(PinyinNames_lastname):
        similarity = Levenshtein.ratio(lastname, pyname)
        q.put((-similarity,ChineseLastNames[idx]))#python priority queue uses min heap, we use -similarity
    
    recChineseNames=[]
    for i in range(num):
        recChineseNames.append(q.get()[1])#get returns tuple if (priority,str)
        
    print(Fore.CYAN + "\nYour recommended Chinese last name:\n", recChineseNames)





#================Two methods to get recommended English names================


def getEnglishNames(ChineseName, num, gender):
    pyname = toPinyin(ChineseName, False)
    q = Q.PriorityQueue()
    
    if gender == "M":
        for EnglishName in EnglishNames_Male:
            similarity = Levenshtein.ratio(EnglishName, pyname)
            q.put((-similarity,EnglishName))#python priority queue uses min heap, we use -similarity
    else:
      for EnglishName in EnglishNames_Female:
            similarity = Levenshtein.ratio(EnglishName, pyname)
            q.put((-similarity,EnglishName))#python priority queue uses min heap, we use -similarity

    recEnglishNames=[]
    for i in range(num):
        recEnglishNames.append(q.get()[1])#get returns tuple if (priority,str)

    return recEnglishNames



def main():
    import colorama
    from colorama import Fore, Back, Style
    colorama.init()

    print(Back.CYAN+Fore.BLACK + '\nWelcome to our Chinese-English Name Recommender System!' + Style.RESET_ALL)
    print(Back.CYAN+Fore.BLACK + 'Please enter your full name:'+ Style.RESET_ALL)
    userName = input(Fore.WHITE)
    if isEnglish(userName):
        forEnglishUser(userName)
    else:
        forChineseUser(userName)
    # userAge = input('\nHello %s! Please enter your age:' % (userName))


def forChineseUser(userName):
    lastname = userName[0]
    firstname = userName[1:]


    import colorama
    from colorama import Fore, Back, Style
    colorama.init()

    print(Fore.GREEN + '\n你好！Now please enter the gender you prefer for the names:')
    print(Fore.GREEN + 'Enter "M" for Male or "F" for Female:')
    userGender = input(Fore.WHITE)
    if userGender == "M" or userGender == "m" or userGender == "Male" :
        userGender = "M"
    else:
        userGender = "F"


    print(Fore.GREEN+'\nAlmost there! How many English names do you prefer our system to generate?')
    num = input(Fore.WHITE)
    num = int(num)
    recFirstNames = getEnglishNames(firstname, num, userGender)
    recLastName = toPinyin(lastname)

    recFullNames = []
    for fn in recFirstNames:
        recFullNames.append(fn + " " + recLastName)
    print(Fore.GREEN + "\nHi %s, here are your %d recommendations for an English name by lexical similarity: " % (firstname, num)) 
    print(recFullNames)

    recommendEnName_meaning(userName, num, userGender)


def forEnglishUser(userName):
    fullname = userName.split()
    firstname = fullname[0]
    lastname = fullname[1]


    
    print(Fore.CYAN + '\nNow please enter the gender you prefer for the names:')
    print(Fore.CYAN + 'Enter "M" for Male and "F" for Female:')
    userGender = input(Fore.WHITE)
    if userGender == "M" or userGender == "m" or userGender == "Male" :
        userGender = "M"
    else:
        userGender = "F"


    print(Fore.CYAN+'\nAlmost there! How many Chinese names do you prefer our system to generate?')
    num = input(Fore.WHITE)
    num = int(num)
    getChineseNames(firstname, num, userGender)
    getChineseLastName(lastname, num)


    recommendChName_meaning(firstname, num, userGender)

    


# =======================read meaning files========================================================================

file_name_male = open('Meaning/name_English_male.txt', 'r') 
file_name_female = open('Meaning/name_English_female.txt', 'r') 

file_meaning_male = open('Meaning/meaning_English_male.txt', 'r') 
file_meaning_female = open('Meaning/meaning_English_female.txt', 'r') 


names_male = []
for line in file_name_male: 
    names_male.append(line[:-1]) #-1 to get rid of the \n character
names_female = []
for line in file_name_female: 
    names_female.append(line[:-1]) #-1 to get rid of the \n character


meanings_male = []
for line in file_meaning_male: 
    meanings_male.append(line[:-1]) #-1 to get rid of the \n character
meanings_female = []
for line in file_meaning_female: 
    meanings_female.append(line[:-1]) #-1 to get rid of the \n character

file_name_male_ch = open('Meaning/name_Chinese_male.txt', 'r') 
file_name_female_ch = open('Meaning/name_Chinese_female.txt', 'r') 

file_meaning_male_ch = open('Meaning/meaning_Chinese_male.txt', 'r') 
file_meaning_female_ch = open('Meaning/meaning_Chinese_female.txt', 'r') 


names_male_ch = []
for line in file_name_male_ch: 
    names_male_ch.append(line[:-1]) #-1 to get rid of the \n character
names_female_ch = []
for line in file_name_female_ch: 
    names_female_ch.append(line[:-1]) #-1 to get rid of the \n character



meanings_male_ch = []
for line in file_meaning_male_ch: 
    meanings_male_ch.append(line[:-1]) #-1 to get rid of the \n character
meanings_female_ch = []
for line in file_meaning_female_ch: 
    meanings_female_ch.append(line[:-1]) #-1 to get rid of the \n character


# ===========================recommend meaning=====================================================================


def recommendChName_meaning(userName, num, userGender):

    print("\n\n^_^ Now we generate some names with similar meaning!")
    q = Q.PriorityQueue()
    recNamesIdx = []
    meanings=[]
    names=[]



    if userGender == "M":
        if userName not in names_male:
            print("Sorry your name is not in our data. Cannot recommend meaning names!")
            return
        meanings = meanings_male_ch
        names = names_male_ch

        user_idx = names_male.index(userName)
        user_meaning = meanings_male[user_idx]

    else:
        if userName not in names_female:
            print("Sorry your name is not in our data. Cannot recommend meaning names!")
            return
        meanings = meanings_female_ch
        names = names_female_ch

        user_idx = names_female.index(userName)
        user_meaning = meanings_female[user_idx]

    print(user_meaning)

    user_meaning = getBadOfWords(user_meaning)
    print(user_meaning)



    for (idx,enMeaning) in enumerate(meanings):
        # print(enMeaning)
        if enMeaning == '':
            similarity = 0
        else:
            similarity = cosine_sim(user_meaning,enMeaning)
        if idx % 2000 == 0:
            print("Have tried %d names..." % (idx))

        if similarity > 0.3:
            recNamesIdx.append(idx)

        elif similarity > 0:
            q.put((-similarity,idx))#python priority queue uses min heap, we use -similarity
        if len(recNamesIdx) >= num:
            break

    



    for i in range(num-len(recNamesIdx)):
        if q.empty():
            break
        qtuple = q.get()
        idx = qtuple[1]        
        recNamesIdx.append(idx)#get returns tuple if (priority,str)


    print("\nYour recommend Chinese names by meaning similarity:")
    for idx in recNamesIdx:
        print("Name: \'%s\'; meaning is:\'%s\'" % (names[idx],meanings[idx][:-1]))

    if(len(recNamesIdx) == 0):
        print("Ah-oh, your name is too unique! We haven't found any similar ones!")

 


def recommendEnName_meaning(userName, num, userGender):
    print("\n\n^_^ Now we generate some names with similar meaning!")
    user_meaning = ""   
    for c in userName:
        user_meaning += ch_char_meaning_map[c]
        user_meaning += " "



    q = Q.PriorityQueue()
    recNamesIdx = []
    meanings=[]
    names=[]


    if userGender == "M":
        meanings = meanings_male
        names = names_male
    else:
        meanings = meanings_male
        names = names_male



    for (idx,enMeaning) in enumerate(meanings):
        # print(enMeaning)
        if enMeaning == '':
            similarity = 0
        else:
            similarity = cosine_sim(user_meaning,enMeaning)
        if idx % 500 == 0:
            print("Have tried %d names..." % (idx))

        if similarity > 0.3:
            recNamesIdx.append(idx)

        elif similarity > 0:
            q.put((-similarity,idx))#python priority queue uses min heap, we use -similarity
        if len(recNamesIdx) >= num:
            break

    



    for i in range(num-len(recNamesIdx)):
        if q.empty():
            break
        qtuple = q.get()
        idx = qtuple[1]        
        recNamesIdx.append(idx)#get returns tuple if (priority,str)


    print("\nYour recommend English names by meaning similarity:")
    for idx in recNamesIdx:
        print("Name: \'%s\'; meaning is:\'%s\'" % (names[idx],meanings[idx]))

    if(len(recNamesIdx) == 0):
        print("Ah-oh, your name is too unique! We haven't found any similar ones!")








if __name__ == "__main__":
    main()



