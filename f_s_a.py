import pandas as pd 
import nltk
from nltk.sentiment.vader import Sentiment 
file='users/simransetia/downloads/data_file.xslsx'
xl = pd.ExcelFile(file)
dfs = xl.parse(xl.sheet_names[0]) #parsing the excel sheet to dataset
dfs = list(dfs['Timeline']) #removes the blank rows from the data
print(dfs)

sid = SentimentIntensityAnalyzer()
str1="UTC+05:30"
for data in dfs:
    a = data.find(str1)
    if(a==-1):
        ss = sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])