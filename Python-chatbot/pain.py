import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
  
# Dataset link: 
df=pd.read_csv('Questions&answer_dataset.csv')
  
# Extract the sentence only
sentence = df.Questions
ans = df.Answers
  
# create vectorizer
vectorizer = TfidfVectorizer(stop_words='english')
  
# vectorizer the text documents
vectorized_documents = vectorizer.fit_transform(sentence, ans)
  
# reduce the dimensionality of the data using PCA
pca = PCA(n_components=2)
reduced_data = pca.fit_transform(vectorized_documents.toarray())
  
  
# cluster the documents using k-means
num_clusters = 2
kmeans = KMeans(n_clusters=num_clusters, n_init=5,
                max_iter=500, random_state=42)
kmeans.fit(vectorized_documents)
  
  
# create a dataframe to store the results
results = pd.DataFrame()
results2 = pd.DataFrame()
results['document'] = sentence
results2['document'] = ans
results['cluster'] = kmeans.labels_
results2['cluster'] = kmeans.labels_
  
# print the results
print(results.sample(5))
print(results2.sample(5))
  
# plot the results
colors = ['red', 'green', 'blue']
cluster = ['related to software development','not software dev']
for i in range(num_clusters):
    plt.scatter(reduced_data[kmeans.labels_ == i, 0],
                reduced_data[kmeans.labels_ == i, 1], 
                s=10, color=colors[i], 
                label=f' {cluster[i]}')
plt.legend()
plt.show()