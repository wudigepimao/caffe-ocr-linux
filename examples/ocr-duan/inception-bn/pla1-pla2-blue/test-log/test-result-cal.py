import sys
import os
from os import path, access, R_OK
import logging

def file_exit(file_path):
    if path.exists(file_path) and path.isfile(file_path) and access(file_path,R_OK):
        return 1
    else:
        return 0

if __name__ == "__main__":

    test_count=0
    alright_count=0

    count=0
    label_map={}
    for l in open("label.txt"):
        label_map[count]=l
        count+=1


    log = raw_input("Inout Your Test Log: ")
    while file_exit(log)==0 :
        print "Either file is missing or is not readable"
        log = raw_input("Inout Your Test Log(exit to exit this program): ")
        if log=="exit":
            sys.exit(0)

    data_label = raw_input("Inout Your Data Label: ")
    while file_exit(data_label)==0:
        print "Either file is missing or is not readable"
        data_label = raw_input("Inout Your Data label(exit to exit this program): ")
        if data_label=="exit":
            sys.exit(0)


    logging.basicConfig(level=logging.INFO,
                    filename="cal_log-"+log+"_vs_"+data_label+".txt",
                    filemode='w',
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

    find_log=0
    for line in open(log):

        elem_log=line.split(":")
        if elem_log[0]!="labels" and find_log==0:
            continue

        if elem_log[0]=="labels":
            find_log=1
            continue

        if elem_log[0]=="Test Point End\n":
            print "All In"
            print str(test_count)+" images in all"
            break

        test_count+=1

        res_test=elem_log[2]
        #print res_test
        path=line.split("]")
        path=path[1].split("[")
        path=path[0]
        #print path[0]

        for line2 in open(data_label):
            elem=line2.split(" ")
            #print str(elem[0])+" "+str(path)
            if str(elem[0]) in str(path):
                #print path+" "+str(elem[0])
                label_num=len(elem)
                res=""
                i=1
                while i<label_num:
                    res='%s%s'%(res,label_map[int(elem[i])])
                    i+=1
                res=res.replace("\n","")
                res_test=res_test.replace("\n","")
                res_test=res_test.strip()
                res=res.strip()

                if str(res)==str(res_test):
                    alright_count+=1
                else:
                    logging.info("Wrong "+str(elem[0])+" "+res+" "+res_test)
                    print "Wrong "+str(elem[0])+" "+res+" "+res_test


    logging.info("Correct Counts: " +str(alright_count))
    logging.info("Wrong Counts: " +str(int(test_count)-int(alright_count)))
    logging.info("Cal End")

    print "Correct Counts: " +str(alright_count)
    print "Wrong Counts: " +str(int(test_count)-int(alright_count))
    print "Cal End"
