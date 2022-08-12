import nltk
from nltk import PorterStemmer, LancasterStemmer, SnowballStemmer


def words_stemmer(words, type="PorterStemmer", lang="english", encoding="utf8"):
    supported_stemmers = ["PorterStemmer", "LancasterStemmer", "SnowballStemmer"]
    if type is None or type not in supported_stemmers:
        return words
    else:
        stem_words = []
        if type == "PorterStemmer":
            stemmer = PorterStemmer()
            for word in words:
                stem_words.append(stemmer.stem(word).encode(encoding))
        if type == "LancasterStemmer":
            stemmer = LancasterStemmer()
            for word in words:
                stem_words.append(stemmer.stem(word).encode(encoding))
        if type == "SnowballStemmer":
            stemmer = SnowballStemmer(lang)
            for word in words:
                stem_words.append(stemmer.stem(word).encode(encoding))
        return b" ".join(stem_words).decode()


words = 'caring cares cared caringly carefully'
print("Original:", words)
print("Porter: ", words_stemmer(nltk.word_tokenize(words), "PorterStemmer"))
print("Lancaster: ", words_stemmer(nltk.word_tokenize(words), "LancasterStemmer"))
print("Snowball: ", words_stemmer(nltk.word_tokenize(words), "SnowballStemmer"))
