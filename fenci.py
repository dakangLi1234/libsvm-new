import jieba
import codecs
import time
from multiprocessing import Pool

def readsplit(datafile,resfile):
    fin1 = codecs.open(datafile, 'rb')
    fout1 = open(resfile, "a", encoding="utf-8")
    while True:
        a=fin1.readline()
        if len(a)==0:
            break
        tags = jieba.cut(a)
        output = ' '.join(list(tags)).strip("\n").strip("\r")
        fout1.write(output)
        fout1.write("\n")
    fout1.close()

readsplit("mil.review","milnew.review")



