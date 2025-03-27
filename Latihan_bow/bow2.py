from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plot
dataset_feature= ['mari kita tolak ruu TNI','yang mana tni akan menjadi superior','apakah benar prabowo itu baik','apakah jokowi terlibat dalam kkn di ikn']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(dataset_feature)
print(X.shape)
features = vectorizer.get_feature_names_out()
idfValues = vectorizer.idf_
d = dict(zip(features, 9 - idfValues))
sortedDict = sorted(d.items(), key = lambda d: d[1], reverse = True)
for i in range(min(10, len(sortedDict))):
    print(sortedDict[i])
   
def PlotWordCloud(frequency):
    wordcloudPlot = WordCloud(background_color="white", width=1500, height=1000)
    wordcloudPlot.generate_from_frequencies(frequencies=frequency)
    plot.figure(figsize=(15,10))
    plot.imshow(wordcloudPlot, interpolation="bilinear")
    plot.axis("off")
    plot.show()
PlotWordCloud(d)