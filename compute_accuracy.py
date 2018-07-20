import fastText
import os


def print_results(N, p, r):
    print("N\t" + str(N))
    print("P@{}\t{:.3f}".format(1, p))
    print("R@{}\t{:.3f}".format(1, r))


def load_model(model_path):
    model = fastText.load_model(model_path)
    return model


def read_data(path):
    """读取txt，返回两个列表，一个是sentence list[]，一个是label list[[],[]](一个sentence对应一个label list)"""
    sentence_list, label_list = [], []
    with open(path, 'r', encoding="utf-8") as f:
        for line in f.readlines():
            line = line.split('__label__')
            sentence_list.append(line[0].strip())
            label_list.append([i.strip() for i in line[1:]])
        return sentence_list, label_list


def compute_accuracy(y_predict, y_label):
    """注意预测的label包含__label__"""
    if len(y_predict) != len(y_label):
        raise Exception("长度不一致")
    else:
        total, count = len(y_label), 0
        for i in range(total):
            y_predict[i] = [k.replace('__label__', '') for k in y_predict[i]]

            # 特殊处理
            if "其它" in y_predict[i]:
                y_predict[i] = ["其它"]      # ‘其它’代表两级标签都为空，因此‘其它’标签单独存在

            if set(y_label[i]) == set(y_predict[i]):
                count += 1
            else:
                print("真实：", y_label[i], "\t预测：", y_predict[i])
                continue
        return count/total

if __name__ == "__main__":
    train_data = '/home/x/helic/pingce/train.txt'
    valid_data = '/home/x/helic/pingce/valid.txt'

    sentence_list, label_list = read_data(valid_data)
    
    # Or with the probability
    classifier = fastText.load_model('model.bin')
    labels, probs = classifier.predict(sentence_list, k=2, threshold=0.08)   # 二维list
    accuracy = compute_accuracy(labels, label_list)
    print("accuracy:", accuracy)   # 0.7861
