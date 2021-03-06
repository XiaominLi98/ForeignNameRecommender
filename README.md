# ForeignNameRecommender
A name generator which recommends foreign names in different languages.

## Getting Started

  The main 4 files are (we list the require packages after the files): 
  
  _projectWithMeaning.py (requires: "colorama", and "Levenshtein")_
  
  _meaningFunctions.py ("nltk", "string", "numpy", and "sklearn")_
  
  _smallHelperFunctions.py ("pinyin", "argparse")_
  
  _bagOfWordsFunctions.py ("metapy")_
  
  Users who do not have these packages (listed above: "colorma", "Levenshtein" and etc.) installed on their machines need to install them. It can be done by running pip install in terminal (e.g. `pip install pinyin`).
  
  ### Usage Instructions:
   1. Download the project folder to your working directory. 
   
   2. Install below packages: _"[colorama](https://pypi.org/project/colorama/)", "[Levenshtein](https://pypi.org/project/python-Levenshtein/)", "[nltk](https://www.nltk.org/)", "string", "numpy", "[sklearn](https://pypi.org/project/scikit-learn/)", "[pinyin](https://pypi.org/project/pinyin/)", "[argparse](https://docs.python.org/3/howto/argparse.html)", "[metapy](https://github.com/meta-toolkit/metapy)"_.
      (Again, you can use methods such as `pip install pinyin`)
   
   3. Go to ForeignNameRecommender repository in terminal. Then run:
   
      `python3 projectWithMeaning.py meaningFunctions.py smallHelperFunctions.py bagOfWordsFunctions.py`
      
      (If do not have python3, python might also work)
   
   Note: if it shows error such as "haven't found module XXX", then it might be possible that we forgot to mention this package. Please install XXX package as well.
   
  
## Overview of the functions
  This program support two functions, one is recommending foreign names that most closely matches the spelling of the input name and the other one is recommmending foreign names that have similar meanings to the input name. This project currently support two languages, Chinese and English. It asks user for an input name and gender and how many names he/she wants to be generated, then it recommends a number of names in which their meanings have the highest similarity with the input name.
   It's more challenging than we thought before to obtain data of name lists. We wrote a lot of programs to parse and refine the found data into the clean and formatted data for our needs. Other languages might be added to our system in the future.

## How it works
  For the first function, we use lexical similarity to support transliteration between English and Chinese names, where we first convert Chinese characters into [pinyin](https://en.wikipedia.org/wiki/Pinyin). For the second function, we measure similarity of the meaning of names by calculating cosine similarity between names. 
  
 ### 1. By lexical similarity

  - Our recommender could generate names by lexcial similarity of two names, which in some sense achieves to match names with similar sounds. _For example, a Chinese name "李然", represented as "Ran Li" in pinyin, would be matched to the following English names:_
  
     _['Raen Li', 'Rain Li', 'Rana Li', 'Rani Li', 'Rean Li', 'Rwan Li', 'Raana Li', 'Raena Li']._ 
  
    Similarly for generating Chinese names to an English name.
  
  - We tried two methods to calculate the similarity (or distance) between names. One using "difflib", the other using "Levenshtein Algorithm" (or "Levenshtein Distance"). Finally we chose the latter since it works better at matching.
  
  ### 2. By semantic similarity
  - Our recommender could also generate names by similarity of meanings of two name, which might be more useful for users. _For example, for a Chinese name "李迅", the first name "迅" means "fast" in Chinese. Our system would recommend the following (we also output their meanings):_
  
    _Name: 'Dashee'; meaning is:'One who is on fast'_
    
    _Name: 'Hartman'; meaning is:'Fast Runner'_
    
    _Name: 'Sherwinn'; meaning is:'He who is as fast as the wind'_
    
    _Name: 'Swift'; meaning is:'One who is swift, fast'_
    
    _Name: 'Aedelflete'; meaning is:'A fast noble person'_
    
    _Name: 'Skete'; meaning is:'To be swift, fast and rapid'_
    
    _Name: 'Speed'; meaning is:'A very fast man'_
    
    _Name: 'Swefred'; meaning is:'A swift, fast man'_
   
     Similarly for generating Chinese names to an English name.
   
   - We used three types of method trying to calculate the similarity of semantic meaning of two sentences (or words), and they are “sklearn”, “spacy”, and “gensim”. Finally we chose the “cosine_sim” function in “sklearn” using “TfidfVectorizer” method in “sklearn.feature_extraction.text”. 
  
  For more details on this project please refer to this video: https://youtu.be/ZadRRnv9Kso
  
  All rights reserved by Xiaomin Li (xiaomin3@illinois.edu) and Jinyuan Li (jinyuan2@illinois.edu).
  😄
