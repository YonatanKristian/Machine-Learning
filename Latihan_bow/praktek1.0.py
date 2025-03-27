from sklearn.feature_extraction.text import CountVectorizer
dataset_feature =["Saya suka belajar machine learning", "Machine learning itu menarik"]
vectorizer = CountVectorizer()
vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
X = vectorizer.fit_transform(dataset_feature)
X2 = vectorizer2.fit_transform(dataset_feature)
X
print(vectorizer.get_feature_names_out())
print(X.toarray())
print(vectorizer2.get_feature_names_out())
print(X2.toarray())
print(X2)