# ForeignNameRecommender
A name generator which recommends foreign names in different languages.

The main 3 files are (we list the require packages after the files): 
  projectWithMeaning.py (requires: "colorama", and "Levenshtein")
  meaningFunctions.py ("nltk", "string", "numpy", and "sklearn")
  smallHelperFunctions.py ("pinyin", "argparse")
  bagOfWordsFunctions.py ("metapy")
  
  Users who do not have these installed on their machines could install these packages by pip (e.g. "pip install pinyin").
  
  Our system currently could recommmend between Chinese names and English names. It's more challenging than we thought before to obtain data of name lists. We wrote a lot of programs to parse and refine the found data into the clean and formatted data for our needs. Other languages might be added to our system in the future.
  
 ## 1. By lexical similarity

  - Our recommender could generate names by lexcial similarity of two names, which in some sense achieves to match names with similar sounds. *For example, a Chinese name "李然", represented as "Ran Li" in pinyin, would be matched to the following English names: ['Raen Li', 'Rain Li', 'Rana Li', 'Rani Li', 'Rean Li', 'Rwan Li', 'Raana Li', 'Raena Li']*. Similarly for generating Chinese names to an English name.
  - We tried two methods to calculate the similarity (or distance) between names. One using "difflib", the other using "Levenshtein Algorithm" (or "Levenshtein Distance"). Finally we chose the latter since it works better at matching.
  
  ## 2. By semantic similarity
  - Our recommender could also generate names by similarity of meanings of two name, which might be more useful for users. *For example, for a Chinese name "李迅", the first name "迅" means "fast" in Chinese. Our system would recommend the following (we also output their meanings):
    Name: 'Dashee'; meaning is:'One who is on fast'
    Name: 'Hartman'; meaning is:'Fast Runner'
    Name: 'Sherwinn'; meaning is:'He who is as fast as the wind'
    Name: 'Swift'; meaning is:'One who is swift, fast'
    Name: 'Aedelflete'; meaning is:'A fast noble person'
    Name: 'Skete'; meaning is:'To be swift, fast and rapid'
    Name: 'Speed'; meaning is:'A very fast man'
    Name: 'Swefred'; meaning is:'A swift, fast man'*
   
   S imilarly for generating Chinese names to an English name.
   -We used three types of method trying to calculate the similarity of semantic meaning of two sentences (or words), and they are “sklearn”, “spacy”, and “gensim”. Finally we chose the “cosine_sim” function in “sklean” using “TfidfVectorizer” method in “sklearn.feature_extraction.text”. 
  
  For more details on the instructions please refer to this video: ????.
