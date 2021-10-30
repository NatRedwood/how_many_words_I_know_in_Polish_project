# How many words do I know in Polish?
# The analysis of WhatsApp chats in Polish

This project is a part of the NLP class.

## Project Description
The purpose of this project is:
1. Practicing working with different types of data: txt, csv, df.
2. Practicing Unix commands as basic text analysis tool.
3. Cleaning the linguistic data: stemming, tokenizing.
4. Extracting important features: removing stopwords, removing names, removing english words and function words that are part of the WhatsApp chat interface.
5. Analyzing words and extracting main topics discussed. 

### Methods Used
* Text Mining
* Data Visualization
* Frequency Distribution

### Technologies
* Python, jupyter. Unix bash
* Pandas
* matplotlib, wordcloud

## Needs of this project

- data exploration
- data processing/cleaning
- feaure extraction
- Unix commands

## Methodology:
To conduct the analysis and answer the question I used Unix commands for simple text analysis like tokenizing and counting words in plain text files, as well as regular expressions.

## Data used:
- the Polish dictionary “Wielki Słownik Języka Polskiego” (“The Great Dictionary of Polish Language”, my translation; available online, [link](https://wsjp.pl/))
- 7 different private WhatsApp conversations exported from the app (I'm not uploading the full chat conversations)
- the AGH corpus of Polish speech and the paper written at the AGH University of Science and Technology, Kraków, Poland (“AGH corpus of Polish speech”, Piotr Zelasko • Bartosz Ziółko • Tomasz Jadczyk • Dawid Skurzok, published online: 6 May 2015, [link](https://link.springer.com/content/pdf/10.1007/s10579-015-9302-y.pdf))
- txt file of Polish stopwords from @bieli, thanks! [link](https://github.com/bieli/stopwords/blob/master/polish.stopwords.txt) GitHub profile / [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/polish_stopwords_names_english_words.txt) txt file with some english words to clean from
## Project files:
1. How  many words do I know in Polish **@PDF**: [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/How%20many%20words%20do%20I%20know%20in%20Polish.pdf)
2. How many words I know in polish **JUPYTER, UNIX** commands: [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/How%20many%20words%20I%20know%20in%20polish%20JUPYTER.ipynb)
3. Cleaning and processing wiht Python **PY**: [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/Cleaning%20and%20processing%20with%20Python.py)
4. Top 1000 words from chats **CSV** (cleaned from polish stopwords and names from the group chat): [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/top_1000_clean_wh_names.csv)


## Project plots and graphs
1. Heap's Law - frequency of the first 1000 words: [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/Heap's%20Law%20-%20frequency%20of%20the%20first%201000%20words.png)
2. Most frequent 20 words not cleaned: [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/Most%20frequent%2020%20words%20not%20cleaned.png)
3. Most frequent 40 words after cleaning: [link](https://github.com/Nwojarnik/how_many_words_I_know_in_Polish_project/blob/main/Most%20frequent%2040%20words%20after%20cleaning.png)
