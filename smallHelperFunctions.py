
import pinyin
import argparse

def toPinyin(s, rearrange=False):
    s = s.strip()
    chars = []
    if rearrange:
        firstname=s[1:]
        lastname=s[0]
        chars.append(pinyin.get(firstname, format="strip", delimiter="-").strip("-"))
        chars.append(pinyin.get(lastname, format="strip", delimiter="-"))
    else:
        chars+= pinyin.get(s, format="strip", delimiter=" ").split()
    return " ".join(map(lambda x: x.capitalize(), chars))

def getEnglishLastName(lastname, num):
    return toPinyin(lastname)


def isEnglish(s):
    try:
        s.encode('ascii')
    except UnicodeEncodeError:
        return False
    else:
        return True