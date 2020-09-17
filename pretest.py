import jieba

txt1='今天是星期天，天气晴，今天晚上我要去看电影'
txt2='今天是周天，天气晴朗，我晚上要去看电影'

all_txt=[]
all_txt.append(txt1)
all_txt.append(txt2)
all_txt_list=[]
for txt in all_txt:
    txt_list=[word for word in jieba.cut(txt)]
    all_txt_list.append(txt_list)
for word in all_txt_list:
    print(word)