__author__ = 'Liangliang Li'
import os
import operator
import time
#-*- coding: utf-8 -*-
u=""
stime=time.time()
for filename in os.listdir(r'data1'):
    filedir="data1/"+filename
    f=open(filedir)


#f=open("data/01010101.txt")

    u=u+ f.read().decode("gbk").encode("utf-8")
    f.close()
print "file ready"
dict={}
u=u.replace("\n","")
u=u.split("  ")
tf=1
list={}

for i in range(len(u)-1):
    each_word=u[i]
    next_word=u[i+1]

    if each_word.find("/") and each_word!="":
        try:
            word,prob=each_word.split("/")
            if prob =='w' or prob =='u':
                continue
            n_word,n_prob=next_word.split("/")
            #print word,prob
            #scan word's prob
            if word not in dict:
                list={}
                dict_new={"prob":prob,"tf":1,"list":list}
                dict[word]=[dict_new]

            kindofword=len(dict[word])
            findprob=0
            for i in range(kindofword):
                if prob == dict[word][i]["prob"]:
                    findprob=1
                    dict[word][i]["tf"]=dict[word][i]["tf"]+1

                    #word_list is a dict,to make a dict
                    word_list=dict[word][i]["list"]
                    if n_word in word_list:
                        word_list[n_word]=word_list[n_word]+1
                        #update list
                    else:
                        if n_prob!="w" and n_prob!="u":
                            word_list[n_word]=1

                #add a new kindofword
                else:
                    continue
            #if prob is not found, add a new prob
            if findprob==0:
                if n_prob=="w" or n_prob=="u":
                    list={}
                else:
                    list={n_word:1}
                dict_new={"prob":prob,"tf":1,"list":list}
                dict[word].insert(kindofword,dict_new)

                    #add word list, to make a dict


            #update word's information

        except ValueError:
            print "could not split each_word:"+each_word
            continue
'''
for i in dict.keys():
    if dict[i]!=[]:
        kindofword=len(dict[i])
        for k in range(kindofword):
            print "||word:"+str(kindofword)+i+" "+str(dict[i][k]["tf"])+" "+dict[i][k]["prob"]+"-->",
            word_list=dict[i][k]["list"]
            s_word_list=sorted(word_list.items(), key=lambda word_list:word_list[1],reverse=True)
            for s in s_word_list:
                print s[0],s[1],
            print ""

print "----"
'''

fw=open("result-by-frequency.txt","w")
ss=""
for i in dict.keys():
    kindofword=len(dict[i])
    for k in range(kindofword):
        word_list=dict[i][k]["list"]
        s_word_list=sorted(word_list.items(), key=lambda word_list:word_list[1],reverse=True)

        sw=""
        for s in s_word_list:
            sw+="["+s[0]+" frq:"+str(s[1])+"]"
        sw+="\n"
        ss+="[word]"+i+"\t[prop. num]:"+str(kindofword)+"\t[prop. name]"+dict[i][k]["prob"]+"\t[collocation list]:"+sw
#    print ss

'''
s_in=raw_input("input a word.\n")
kindofword=len(dict[s_in])

for k in range(kindofword):
    print str(dict[s_in][k]["tf"])
    word_list=dict[s_in][k]["list"]
    s_word_list=sorted(word_list.items(), key=lambda word_list:word_list[1],reverse=True)
    for s in s_word_list:
        print "as a "+dict[s_in][k]["prob"]+":",s[0],s[1],
    print ""

'''
fw.write(ss)
fw.close

etime=time.time()
print etime-stime