import jieba
from sklearn.feature_extraction.text import TfidfVectorizer

file = open(r'C:/Users/cqwjk/Desktop/ML_Projects/file/test.tsv', "r", encoding='UTF-8')
tmp = file.readlines()
text = ''
for i in tmp:
    text += i
sentences = text.split()
sent_words = [list(jieba.cut(sent0)) for sent0 in sentences]
document = [" ".join(sent0) for sent0 in sent_words]
tfidf_result = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b").fit(document)
print(tfidf_result.vocabulary_)
