import nltk
import re
import string
from nltk.corpus import stopwords
from nltk import chunk
from nltk.tokenize import word_tokenize, TreebankWordTokenizer
from nltk.tag.perceptron import PerceptronTagger

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('maxent_ne_chunker')
nltk.download('words')
nltk.download('tagsets')


# nltk.download('averaged_perceptron_tagger')
# sentence = "At eight o'clock on Thursday morning Arthur didn't feel very good."
# tokens = nltk.word_tokenize(sentence)
# # print(tokens)
# tagged = nltk.pos_tag(tokens)
# print(tagged[0:6])

# text = 'Statistics skills, and programming skills are equally important for analytics. Statistics skills, ' \
#        'and domain knowledge are important for analytics. I like reading books and travelling.'
# sent_tokenize_list = nltk.sent_tokenize(text)
# print(sent_tokenize_list)

# word_tokenize = word_tokenize(text)
# print(word_tokenize)

# spanish_tokenizer = nltk.data.load('tokenizers/punkt/spanish.pickle')
# spanish_tokenizer.tokenize('Hola. Esta es una frase espanola.')
# print(spanish_tokenizer)

# tokenizer = TreebankWordTokenizer()
# print(tokenizer.tokenize(text))

# Remove Number
def remove_number(text):
    return re.sub(r'\d', '', text)


# text = 'This is a sample English sentence, \n with whitespace and numbers 1234!'
# print(remove_number(text))


# Remove punctuations

def remove_punctuations(text):
    words = nltk.word_tokenize(text)
    punt_removed = [w for w in words if w.lower() not in string.punctuation]
    return " ".join(punt_removed)


# print(remove_punctuations('This is a sample English sentence, with punctuations!'))

# Remove stop words
def remove_stopwords(text, lang='english'):
    words = nltk.word_tokenize(text)
    lang_stop_words = stopwords.words(lang)
    stopwords_removed = [w for w in words if w.lower() not in lang_stop_words]
    return " ".join(stopwords_removed)


# print(remove_stopwords('This is a sample English sentence'))

def remove_whitespace(text):
    return " ".join(text.split())


# text = 'This is a sample English sentence, \n with whitespace and numbers 1234!'
# print(remove_whitespace(text))

# POS TAG
tagged_sent = nltk.pos_tag(nltk.word_tokenize('This is a sample English sentence'))
# print(tagged_sent)
tree = chunk.ne_chunk(tagged_sent)
# print(tree)

# Perceptron Tagger
PT = PerceptronTagger()
# print(PT.tag('This is a sample English sentence'.split()))
print(nltk.help.upenn_tagset('NNP'))