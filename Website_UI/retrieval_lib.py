import pandas as pd
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import string
import pickle
from rank_bm25 import BM25Okapi
from spellchecker import SpellChecker
spell = SpellChecker()

def remove_stopwords(data):
  stop_words = set(stopwords.words('english'))
  new_data = []
  for w in data:
    if w not in stop_words:
      new_data.append(w)
  return new_data

def spellcheck(data):
  new_data = []
  for w in data:
    new_word = spell.correction(w)
    new_data.append(new_word)
  return new_data

def remove_punc(data):
  new_data = []
  for w in data:
    if w not in string.punctuation:
      new_data.append(w)
  return new_data

def lemmatizer(data):
  new_data = []
  lemm = WordNetLemmatizer()
  for w in data:
    new_word = lemm.lemmatize(w)
    new_data.append(new_word)
  return new_data

def preprocess(data):
  data = data.lower()
  data = remove_punc(data)
  data = word_tokenize("".join(data))
  data = remove_stopwords(data)
  data = spellcheck(data)
  data = lemmatizer(data)
  return data

def query_for_return(data):
  data = word_tokenize(data)
  data = spellcheck(data)
  return " ".join(data)

def preprocess_data(raw_text1):
  text = []
  for sent in raw_text1:
    new_sent = preprocess(sent)
    new_sent = " ".join(new_sent) 
    text.append(new_sent)
  return text

def load_values():
  bm25 = pickle.load(open("bm25_index", "rb"))
  patents = pickle.load(open("patents_dump", "rb"))
  return bm25, patents

bm25, patents = load_values()

def retrieve_patents(query):
  original_query = query
  upd_query = query_for_return(query)
  query = preprocess_data([query])[0]
  tokenized_query = query.split(" ")
  if len(tokenized_query[0]) == 0:
    return ([], original_query)
  doc_scores = bm25.get_scores(tokenized_query)
  retrieved_docs = bm25.get_top_n(tokenized_query, patents, n=10)
  return (retrieved_docs, upd_query)


if __name__ == "__main__":
  query = input()
  lst, q = retrieve_patents(query)
  print(q)
  print(len(lst))
  # print(len(lst[0]))
  # for i in lst[:2]:
  # 	print(i)
