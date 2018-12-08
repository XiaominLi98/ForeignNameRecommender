
import nltk, string
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

# nltk.download('punkt') # if necessary...



def stem_tokens(tokens):
	stemmer = nltk.stem.porter.PorterStemmer()
	return [stemmer.stem(item) for item in tokens]

'''remove punctuation, lowercase, stem'''
def normalize(text):
	remove_punctuation_map = dict((ord(char), None) for char in string.punctuation)
	return stem_tokens(nltk.word_tokenize(text.lower().translate(remove_punctuation_map)))


def cosine_sim(text1, text2):
	vectorizer = TfidfVectorizer(tokenizer=normalize, stop_words='english')
	tfidf = vectorizer.fit_transform([text1, text2])
	return ((tfidf * tfidf.T).A)[0,1]

# ========================
# import gensim  


# def avg_sentence_vector(words, model, num_features, index2word_set):
#     #function to average all words vectors in a given paragraph
#     featureVec = np.zeros((num_features,), dtype="float32")
#     nwords = 0

#     for word in words:
#         if word in index2word_set:
#             nwords = nwords+1
#             featureVec = np.add(featureVec, model[word])

#     if nwords>0:
#         featureVec = np.divide(featureVec, nwords)
#     return featureVec

# def cosine_sim_method2(sentence_1,sentence_2):
# 	#get average vector for sentence 1
# 	sentence_1_avg_vector = gensim.avg_feature_vector(sentence_1.split(), model=word2vec_model, num_features=100)

# 	#get average vector for sentence 2
# 	sentence_2_avg_vector = gensim.avg_feature_vector(sentence_2.split(), model=word2vec_model, num_features=100)

# 	sen1_sen2_similarity =  gensim.cosine_similarity(sentence_1_avg_vector,sentence_2_avg_vector)
# 	return sen1_sen2_similarity