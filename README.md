# ForeignNameRecommender
A name generator which recommends foreign names in different languages.

The main 4 files are (we list the require packages after the files): 
  
  _projectWithMeaning.py (requires: "colorama", and "Levenshtein")_
  
  _meaningFunctions.py ("nltk", "string", "numpy", and "sklearn")_
  
  _smallHelperFunctions.py ("pinyin", "argparse")_
  
  _bagOfWordsFunctions.py ("metapy")_
  
  Users who do not have these installed on their machines could install these packages by pip (e.g. `pip install pinyin`).
  
  Our system currently could recommmend between Chinese names and English names. It's more challenging than we thought before to obtain data of name lists. We wrote a lot of programs to parse and refine the found data into the clean and formatted data for our needs. Other languages might be added to our system in the future.
  We also prompt the user to enter their genders and number of recommendations they want.
  
 ## 1. By lexical similarity

  - Our recommender could generate names by lexcial similarity of two names, which in some sense achieves to match names with similar sounds. _For example, a Chinese name "李然", represented as "Ran Li" in pinyin, would be matched to the following English names:_
  
     _['Raen Li', 'Rain Li', 'Rana Li', 'Rani Li', 'Rean Li', 'Rwan Li', 'Raana Li', 'Raena Li']._ 
  
    Similarly for generating Chinese names to an English name.
  
  - We tried two methods to calculate the similarity (or distance) between names. One using "difflib", the other using "Levenshtein Algorithm" (or "Levenshtein Distance"). Finally we chose the latter since it works better at matching.
  
  ## 2. By semantic similarity
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
   
   - We used three types of method trying to calculate the similarity of semantic meaning of two sentences (or words), and they are “sklearn”, “spacy”, and “gensim”. Finally we chose the “cosine_sim” function in “sklean” using “TfidfVectorizer” method in “sklearn.feature_extraction.text”. 
  
  For more details on the instructions please refer to this video: ????.
  
  
  All rights reserved by Xiaomin Li (xiaomin3@illinois.edu) and Jinyuan Li (jinyuan2@illinois.edu).
  😄
