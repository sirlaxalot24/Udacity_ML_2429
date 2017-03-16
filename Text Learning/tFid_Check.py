from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

word_data = pickle.load(open(r'your_word_data.pkl', "r"))

tfidf = TfidfVectorizer(stop_words='english')
tfidf.fit_transform(word_data)
vocab_list = tfidf.get_feature_names()
print vocab_list[34597]