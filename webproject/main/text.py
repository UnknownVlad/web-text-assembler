import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.tokenize import word_tokenize
from nltk.stem.snowball import SnowballStemmer
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer


def token(text):
    words = nltk.word_tokenize(text)
    return words


def lemm(text, choice_lang):
    if choice_lang == "rus":
        lemmatizer = SnowballStemmer("russian")
        words = [lemmatizer.stem(word) for word in token(text)]
    else:
        lemmatizer = WordNetLemmatizer()
        words = ' '.join([lemmatizer.lemmatize(w) for w in token(text)])
    return words


def stemm(text, choice_lang):
    if choice_lang == "rus":
        stemmer = SnowballStemmer("russian")
    else:
        stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in token(text)]
    return words


def check_text(choice, choice_lang, text):
    global words

    match choice:
        case "token":
            words = token(text)
        case "lem":
            words = lemm(text, choice_lang)
        case "stem":
            words = stemm(text, choice_lang)
    return words
