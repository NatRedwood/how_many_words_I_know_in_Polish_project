
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#from wordcloud import WordCloud

data = pd.read_csv('C:/Users/natal/CU BOULDER NLP COURSE/Asssigment1/PART 1 Polish/data/chat_top_1000.txt',sep='\s+',header=None)
data
words_list = list(data[1])
#print(words_list)
counts_list = list(data[0])
counts_head = counts_list

plt.plot(np.arange(1000), counts_head)
plt.title("Heap's Law - frequency of the first 1000 words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.show()

data = pd.read_csv('C:/Users/natal/CU BOULDER NLP COURSE/Asssigment1/PART 1 Polish/data/chat_top_1000.txt',sep='\s+',header=None)
data.columns = ['Count', 'Word']
most_common = data[:20]

words_list_com = list(most_common['Word'])
words_list_com
counts_list_com = list(most_common['Count'])
counts_list_com

plt.plot(words_list_com, counts_list_com)
plt.xticks(rotation = 75)
plt.title("Most frequent 20 words")
plt.xlabel("Words")
plt.ylabel("Counts")
plt.show()

f = open('C:/Users/natal/CU BOULDER NLP COURSE/Asssigment1/PART 1 Polish/data/polish.txt', encoding='utf-8')
f = f.read()
stopwords = f.split()

words = [w for w in data['Word'] if w not in stopwords]
words_cleaned = [word for word in words if len(word) > 3]
words_cleaned[:20]

names = ['igor','nats','mamcik','tatko']
words_cleaned_wh_names = [word for word in words_cleaned if word not in names]

data_cleaned = data[data['Word'].isin(words_cleaned_wh_names)]

data_cleaned.to_csv('top_1000_clean_wh_names.csv')

len(data_cleaned)

first_40 = data_cleaned[:40]
first_40

plt.plot(first_40['Word'], first_40['Count'])
plt.xticks(rotation = 90)
plt.title("Most frequent 40 words after cleaning")
plt.xlabel("Words")
plt.ylabel("Counts")
plt.show()

#df = data_cleaned.Word
#text = df.to_string()
#wordcloud = WordCloud().generate(str(['Count']))
