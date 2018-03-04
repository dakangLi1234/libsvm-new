#! python2
#! /usr/bin/env python
#coding=utf-8
from __future__ import division
from document import createDomain
from svmclassify import svm_classify 

domain=createDomain('mine')
trains=domain[0][50:]+domain[1][50:]
tests=domain[0][:50]+domain[1][:50]
svm_classify(trains,tests)