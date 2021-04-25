
# import time
# start = time.time()
# # hour = int(input("please input hour:"))
# # minute = int(input("please input minute:"))
# # second = int(input("please input second:"))
# # second += 1
# # if(second==60):
# #     minute+=1
# #     second=0
# # if(minute==60):
# #     hour+=1
# #     minute=0
# # if(hour==24):
# #     hour=0
# # print("hour",hour,"minute:",minute,"second:",second)
#
#
def erfen_find(x,list,len):
    begin = 0
    end = len-1
    while begin <= end:
        mid = ( begin + end )//2
        if x > list[mid]:
            begin = mid + 1
        elif x < list[mid]:
            end = mid - 1
        else:
            return mid
    return -1
# # #
# import time
# start = time.time()
# openfile=open("D:\笔记，PDF\Python计算实验一\words.txt",mode="r")
# outfile=open("D:\笔记，PDF\Python计算实验一\wwwords.txt",mode="w")
# list=[]
# relist=[]
# start = time.time()
# line = openfile.readline()
# while line:
#     list.append(line)
#     relist.append(line[::-1])
#     line = openfile.readline().strip()
# len=len(relist)
# print(len)
# # relist = set(relist)
# for w in relist:
#     sign=erfen_find(w,list,len)
#     # if sign!=None:
#     #     print(list[sign])
# print(time.time()-start)

# import time
# start = time.time()
# openfile=open("D:\笔记，PDF\Python计算实验一\words.txt",mode="r")
# outfile=open("D:\笔记，PDF\Python计算实验一\wwwords.txt",mode="w")
# list=[]
# relist=[]
# start = time.time()
# line = openfile.readline()
# while line:
#     list.append(line)
#     relist.append(line[::-1])
#     line = openfile.readline().strip()
# len=len(relist)
# print(len)
# # relist = set(relist)
# for w in relist:
#      for rew in list:
#          ''
#     #     if(w==rew):print(w)
# print(time.time()-start)
#
# # # reverse pair
# words = { w.strip() for w in openfile }
# result = { w for w in words if w[::-1] in words }
# print(time.time() - start)
# # print(sorted(list(result)))
# import time
# start = time.time()
# punctuation=r''',./;'[]\`~!@#$%^&*()_+-={:>?<|"} '''
# SrcFile=open(r"D:\笔记，PDF\Python计算实验一\NeverGiveUp.txt",'r',encoding="UTF-8")
# Text=list(SrcFile.read())
# Word=''
# WordList=[]
# Wordnumber=[]
# for x in Text:
#     if (x not in punctuation):
#         Word+=x
#     else:
#         if Word not in WordList:
#             WordList.append(Word)
#             Wordnumber.append(1)
#         else:
#             Wordnumber[WordList.index(Word)] += 1
#         Word=""
# for i in range(len(WordList)):
#     # print(WordList[i],Wordnumber[i],sep=' ')
#     ''
# print(time.time() - start)

# # #
# import time
# start = time.time()
# fuhao=r''',./;'[]\`~!@#$%^&*()_+-={:>?<|"} '''
# File=open(r"D:\笔记，PDF\Python计算实验一\NeverGiveUp.txt",'r',encoding="UTF-8")
# Text=list(File.read().strip())
# Word=''
# WordDict={}
#
# for x in Text:
#     if (x not in fuhao):
#         Word+=x
#     else:
#         if Word not in WordDict.keys():
#             if Word!='':
#                 WordDict[Word]=1
#         else:
#             WordDict[Word]+=1
#         Word=""
# order_WordDict=sorted(WordDict.items(),key=lambda x:x[1],reverse=True)
# # print (order_WordDict)
# print(time.time()-
# def jieChen(n):
#     if n==0:
#         return 1
#     else: return n*jieChen(n-1)
#
#
# import math # 先导入math模块
# x=2*math.sqrt(2)/9801
# k=0
# answer =0
# try:
#     while (k<10000):
#             y = jieChen(4*k)*(1103+26390*k)
#             z = (394**(4*k))*(jieChen(k)**4)
#             answer = answer+(y/z)
#             k=k+1
#             print('%.51f' %(1.0/(x*answer)))
# except:
#     ''
#
#
#
# #
# import random
# INF=float('inf')
# try:
#     #M=int(input("请输入班级数量"))
#     #N=int(input("请输入班级同学数量"))
#     M=1000
#     N=70
#     while M>=1000:
#         # while N>=1:
#             Q = 0
#             for x in range(0,M):
#                 bir=[(random.randint(1,365))for i in range(N)]
#                 sbir=set(bir)
#                 if(len(sbir)<len(bir)):Q+=1
#             mydict={}
#             mydict[N]=Q/M
#             print(mydict)
#
#             # print(Q)
#             # print(Q/M)
#             # N+=1
#     M += 1
# except:
#     ''

from bisect import bisect_left
from random import randint

def make_word_list():
    """Reads lines from a file and builds a list using append."""
    word_list = []
    fin = open(r'D:\笔记，PDF\Python计算实验一\words.txt','r')
    for line in fin:
        word = line.strip()
        word_list.append(word)
    return word_list


def in_bisect(word_list, word):
    """Checks whether a word is in a list using bisection search.

    Precondition: the words in the list are sorted

    word_list: list of strings
    word: string
    """
    i = bisect_left(word_list, word)
    if i != len(word_list) and word_list[i] == word:
        return True
    else:
        return False

def delletter(word_list, word,flag):
    '''如果单词的剩余字母数高于1则继续减少一个单词'''
    delword = word
    if len(delword)==1:
        if delword=='a' or delword =='i':
            flag[0]=1
        return
    else:
      for i in range(0,len(delword)):
        reword=delword[:i]+delword[i+1:]
        if(in_bisect(word_list,reword) or len(reword)==1):
            delletter(word_list,reword,flag)

if __name__ == '__main__':
    word_list = make_word_list()
    lista=[]
    for word in word_list:
        flag=[0]
        delletter(word_list, word,flag)
        if(flag[0]==1):
            lista.append(word)
    lista.sort(reverse=True,key=len)
    print(lista)












