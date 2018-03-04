#! python2
#! /usr/bin/env python
#coding=utf-8
from __future__ import division
from svmutil import *
import math

def getlexicon(documents):
    words=[]
    # get the words in train documents
    for document in documents:
        words+=document.words.keys()
    words=set(words)
    
    # create the (word,id) pairs
    lexicon={}
    i=1
    for word in words:
        lexicon[word]=i
        i+=1
    return lexicon
    
# create sentiment classification style svm data
def createData(documents,lexicon):
    x=[];y=[]
    for document in documents:
        if document.polarity==True:
            y.append(1)
        else:
            y.append(-1)
        pairs=dict([(lexicon[word],document.words[word]) for word in document.words.keys() if word in lexicon])

        x.append(pairs)
    return [y,x]
  
def svm_classify(trains,tests,useWeight=False):
    lexicon=getlexicon(trains)
    trainsData,testsData=createData(trains,lexicon),createData(tests,lexicon)
    print(len(trainsData[0]))
    prob = svm_problem(trainsData[0],trainsData[1])
    param = svm_parameter('-t 0')
    model = svm_train(prob, param)
    p_labels, p_acc, p_vals = svm_predict(testsData[0],testsData[1], model)
    output=open('result.output','w')
    for label in p_labels:
        output.write('%d\n' %label)
    
    p=n=tp=tn=fp=fn=0
    for i,label in enumerate(p_labels):
        if tests[i].polarity==True:
            p+=1
            if label==1:
                tp+=1
            else:
                fn+=1
        else:
            n+=1
            if label==-1:
                tn+=1
            else:
                fp+=1
    
    acc=(tp+tn)/(p+n)
    precisionP=tp/(tp+fp)
    precisionN=tn/(tn+fn)
    recallP=tp/(tp+fn)
    recallN=tn/(tn+fp)
    gmean=math.sqrt(recallP*recallN)
    f_p=2*precisionP*recallP/(precisionP+recallP)
    f_n=2*precisionN*recallN/(precisionN+recallN)
    print '{gmean:%s recallP:%s recallN:%s} {precP:%s precN:%s fP:%s fN:%s} acc:%s' %(gmean,recallP,recallN,precisionP,precisionN,f_p,f_n,acc)
    
    #return p_labels

