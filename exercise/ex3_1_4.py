from sklearn.feature_extraction.text import CountVectorizer
from nltk.stem import PorterStemmer

with open('data/textDocs.txt', 'r') as f:
    raw_file = f.read()
corpus = raw_file.split('\n')
corpus = list(filter(None, corpus))

with open('data/stopWords.txt', 'r') as f:
    raw_file = f.read()
stopwords = raw_file.split('\n')

stemmer = PorterStemmer()
analyzer = CountVectorizer(token_pattern=r'\b[^\d\W]+\b', 
                           stop_words=stopwords).build_analyzer()

def stemmed_words(doc):
    return (stemmer.stem(w) for w in analyzer(doc))

vectorizer = CountVectorizer(analyzer=stemmed_words)    

vectorizer.fit(corpus)
attributeNames = vectorizer.get_feature_names_out()


X = vectorizer.transform(corpus)
N,M = X.shape
X = X.toarray()
