file = open('/Users/Mike/CS410/ChineseFirstNames.txt', 'r') 

i=0

characters = []
for line in file:
    for k in range(0,len(line)-1):
        characters.append(line[k])
    i += 1
    if i % 5000 ==0:
        print(i)
    
print("Done!")
print(len(characters))

charSet = set(characters)
print("len(charSet)=",len(charSet))
charList = list(charSet)
print(charList[:20])


# 用第一种方法试试快不快

import goslate
gs = goslate.Goslate()
 
    
file = open("ChineseCharacters_meaning.txt", "w")
for (i,char) in enumerate(charList):
    meaning = gs.translate(char,'en')
    file.write(meaning + "\n")
    
    if i %100 ==0:
        print(i)
file.close()

print("ChineseCharacters_meaning DONE!")