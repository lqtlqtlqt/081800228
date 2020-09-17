import jieba
import os

path1=os.path.abspath('.')
#读取停用词，创建一个停用词表
stwlist= [line.strip() for line in open(path1+'\\'+'baidu_stopwords.txt',encoding='utf-8').readlines()]

test ={}
test['orig.txt'] = open(path1+'\\'+'orig.txt', 'r', encoding='utf-8').read()
test['orig_0.8_add.txt'] = open(path1+'\\'+'orig_0.8_add.txt', 'r', encoding='utf-8').read()
test['orig_0.8_del.txt'] = open(path1+'\\'+'orig_0.8_del.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_1.txt'] = open(path1+'\\'+'orig_0.8_dis_1.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_3.txt'] = open(path1+'\\'+'orig_0.8_dis_3.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_7.txt'] = open(path1+'\\'+'orig_0.8_dis_7.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_10.txt'] = open(path1+'\\'+'orig_0.8_dis_10.txt', 'r', encoding='utf-8').read()
test['orig_0.8_dis_15.txt'] = open(path1+'\\'+'orig_0.8_dis_15.txt', 'r', encoding='utf-8').read()
test['orig_0.8_mix.txt'] = open(path1+'\\'+'orig_0.8_mix.txt', 'r', encoding='utf-8').read()
test['orig_0.8_rep.txt'] = open(path1+'\\'+'orig_0.8_rep.txt', 'r', encoding='utf-8').read()

def jaccard():
#预处理：去分词，去停用词,去符号
    test_word=[]
    i=0
    for key in test.keys():
        test_word.append([])
        words = jieba.cut(test[key],cut_all =False)
        for word in words:
             if word.strip() not in stwlist:
                  if word !='\t':
                     if word !='\r\n':
                         test_word[i].append(word)
        i=i+1
#jaccard系数的计算    
    j=0
    for key in test.keys():
        temp=0
        for word in test_word[0]:
             if word in test_word[j]:
                temp =temp +1
        fenmu = len(test_word[0]) + len(test_word[j]) -temp
        jaccard_coefficient =float(temp/fenmu)
        print('测试样本为:%s,相似度为：%.2f'%(key,jaccard_coefficient))
        print('-----------------------------------')
        j=j+1

if __name__=='__main__':
    jaccard()