#coding:utf8
#python利用结巴分词关键词自动提取 请确认安装jieba，安装方法pip install jieba 参考网址https://github.com/fxsjy/jieba
__author__="liyatao"
def cutword(word):
     import jieba
     tags=[]
     seg_list = jieba.cut_for_search(word)
     # seg_list = jieba.cut(word)
     seg_list={}.fromkeys(seg_list).keys()  #去除列表中重复的元素
     for x in seg_list:
          if len(x)>=2:        #如果分出来的词的元素大于等于2个字
             tags.append(x)    #添加到新的列表中
          else:
               pass

     tags.sort(key=lambda x:len(x))   #按列表中元素字符串的长度从小到大排序
     print tags
     for each in tags:
         print each
     # if 1<=len(tags)<=4:   #如果列表中元素大于1 小于或等于4个元素
     #      tag=(",".join(tags))
     #      return tags,tag   #返回列表和关键词
     # elif len(tags)>4:
     #      tag=(",".join(tags[(len(tags)-4):]))  #如果列表元素大于4个。比如是5个就取第1个元素到最后一个元素
     #      return tags,tag  #返回列表和关键词
     # else:
     #      pass

if  __name__=="__main__":
     word="不花1分钱,关键词快速排名到百度首页"
     cutword(word)
