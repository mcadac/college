#!python3 -m spacy download en_core_web_lg
import spacy

nlp = spacy.load('en_core_web_lg')

train_x = ['i love the book', 'this ia great book', 'i love the shoes', 'the fit is great']
train_y = ['book', 'books', 'clothes', 'clothes']
labels = ['book', 'books', 'clothes', 'clothes']

from sklearn.feature_extraction.text import CountVectorizer
my_vectorizer = CountVectorizer()
the_vectors = my_vectorizer.fit_transform(train_x)

print(my_vectorizer.get_feature_names())
print(the_vectors.toarray())
