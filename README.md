## fastText安装
```
$ wget https://github.com/facebookresearch/fastText/archive/v0.1.0.zip
$ unzip v0.1.0.zip
$ cd fastText-0.1.0
$ make
```

安装python wrapper: (no pip install，二者不兼容)   =>官方不推荐python
```
$ git clone https://github.com/facebookresearch/fastText.git
$ cd fastText
$ pip install .
```

## fasttext API
reference : https://fasttext.cc/docs/en/supervised-tutorial.html
使用C++训练，不要使用python，原始C++有更多的API支持

```
# under installation directory
./fasttext supervised -input cooking.train -output model_cooking  # 生成model_cooking.bin 和model_cooking.vec

# 测试P,R
./fasttext test model_cooking.bin cooking.valid    
```

More API:
```
$ ./fasttext supervised
Empty input or output path.

The following arguments are mandatory:
  -input              training file path
  -output             output file path

  The following arguments are optional:
  -verbose            verbosity level [2]

  The following arguments for the dictionary are optional:
  -minCount           minimal number of word occurrences [5]
  -minCountLabel      minimal number of label occurrences [0]
  -wordNgrams         max length of word ngram [1]
  -bucket             number of buckets [2000000]
  -minn               min length of char ngram [3]
  -maxn               max length of char ngram [6]
  -t                  sampling threshold [0.0001]
  -label              labels prefix [__label__]

  The following arguments for training are optional:
  -lr                 learning rate [0.05]
  -lrUpdateRate       change the rate of updates for the learning rate [100]
  -dim                size of word vectors [100]
  -ws                 size of the context window [5]
  -epoch              number of epochs [5]
  -neg                number of negatives sampled [5]
  -loss               loss function {ns, hs, softmax} [ns]
  -thread             number of threads [12]
  -pretrainedVectors  pretrained word vectors for supervised learning []
  -saveOutput         whether output params should be saved [0]

  The following arguments for quantization are optional:
  -cutoff             number of words and ngrams to retain [0]
  -retrain            finetune embeddings if a cutoff is applied [0]
  -qnorm              quantizing the norm separately [0]
  -qout               quantizing the classifier [0]
  -dsub               size of each sub-vector [2]
```

## Models(短文本分类)

### fasttext_0.7861_20180719
将一二级标签看作多标签问题，同时预测两个标签，有利于处理某一级标签空缺的问题，当一二级标签都为空时，设定为其它类。
data: `fasttext_0.7861_20180720/data` ; `training:valid=8:2`
    
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

