# pip install yake
from winreg import KEY_WOW64_32KEY
import yake
deduplication_algo = 'seqm'
max_ngram_size = 3
text = 'Today is newday'
kw_extractor = yake.KeywordExtractor(lan='en', n=max_ngram_size, dedupFunc=deduplication_algo)
keywords = kw_extractor.extract_keywords(text)

for kw in keywords:
  print(kw)
# print(keywords[0][0])