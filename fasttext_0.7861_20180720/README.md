将一二级标签看作多标签问题，同时预测两个标签，有利于处理某一级标签空缺的问题，当一二级标签都为空时，设定为其它类。
data: `fasttext_0.7861_20180720/data`(jieba分词，没有stopwords和其他预处理) ; `training:valid=8:2`
    
training:  
```
./fasttext supervised -input ../pingce/train.txt -output ../pingce/model -epoch 50 -wordNgrams 2
```

tune:
```
classifier.predict(sentence_list, k=2, threshold=0.08)       # 选取不同的预测概率阈值以使得accuracy最高
```

results:  `total : 0.7861`

error_prediction: `fasttext_0.7861_20180720/error_prediction.txt`