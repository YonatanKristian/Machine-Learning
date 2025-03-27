from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    'APAKAH.',
    'BENAR.',
    'JOKOWI.',
    'ADALAH KAISAR JAWA ?',
]
vectorizer = CountVectorizer()
vectorizer2 = CountVectorizer(analyzer='word', ngram_range=(2, 2))
Z = vectorizer.fit_transform(corpus)
Z2 = vectorizer2.fit_transform(corpus)
print (vectorizer.get_feature_names_out())
print(vectorizer2.get_feature_names_out())
print(Z.toarray())
print(Z2.toarray())