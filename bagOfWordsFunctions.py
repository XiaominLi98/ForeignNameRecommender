#import the MeTA python bindings
import metapy
#If you'd like, you can tell MeTA to log to stderr so you can get progress output 
#when running long-running function calls.

def getBadOfWords(sentence):
	metapy.log_to_stderr()


	doc = metapy.index.Document()
	# doc.content("I said that I can't believe that it only costs $19.95!")
	doc.content(sentence)


	tok = metapy.analyzers.ICUTokenizer(suppress_tags=True)
	tok.set_content(doc.content()) # this could be any string


	# Here, we can see that the LengthFilter is consuming our original ICUTokenizer.
	# It modifies the token stream by only emitting tokens 
	# that are of a minimum length of 2 and a maximum length of 30.

	tok = metapy.analyzers.LengthFilter(tok, min=2, max=30)
	tok.set_content(doc.content()) # this could be any string

	# Stopword removal and stemming
	tok = metapy.analyzers.ListFilter(tok, "lemur-stopwords.txt", metapy.analyzers.ListFilter.Type.Reject)
	tok.set_content(doc.content())
	tokens = [token for token in tok]

	cleanSentence = ""
	for word in tokens:
		cleanSentence += word
		cleanSentence += " "
	return cleanSentence



