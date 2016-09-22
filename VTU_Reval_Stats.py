import httplib
from httplib import HTTPConnection, HTTPS_PORT
import ssl
import socket
import mechanize
import unirest
import time
import sys
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

pp=PdfPages('multipage.pdf')
httplib.HTTPConnection._http_vsn = 10
httplib.HTTPConnection._http_vsn_str = 'HTTP/1.0'
br=mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_equiv(False)


word=''
BENGALURU_COLLEGE_CODES = ['1ay', '1ap', '1aa', '1ao', '1ah', '1aj', '1ak', '1ac', '1am', '1as', '1ar', '1at', '1au', '1bg', '1bt', '1bc', '1bi', '1bh', '1bs', '1bm', '1by', '1bo', '1ck', '1cr', '1cd', '1cg', '1ce', '1dt', '1ds', '1db', '1da', '1cc', '1gv', '1ec', '1ep', '1ew', '1gs', '1gc', '1ga', '1gd', '1sk', '1gg', '1hk', '1hm', '1ic', '1ii', '1jv', '1js', '1jt', '1ks', '1ki', '1kn', '1me', '1mj', '1mv', '1nj', '1nc', '1nh', '1ox', '1pn', '1pe', '1ri', '1rl', '1rr', '1rg', '1re', '1rn', '1sj', '1va', '1st', '1sz', '1sg', '1sc', '1sp', '1hs', '1sb', '1sv', '1jb', '1sw', '1bn', '1kt', '1kh', '1rc', '1ve', '1tj', '1vi', '1vj', '1vk', '1yd']

for j in range(0,89):
    mgmnt_new=[]
    or_new=[]
    usp_new=[]
    cn_new=[]
    cg_new=[]
    cd_new=[]
    mgmnt_total=0.0
    or_total=0.0
    usp_total=0.0
    cn_total=0.0
    cg_total=0.0
    cd_total=0.0
    for i in range(1,131):
        if i<10:
            word=str(BENGALURU_COLLEGE_CODES[j])+"13CS00%d" %i
        elif i<100:
            word=str(BENGALURU_COLLEGE_CODES[j])+"13CS0%d" %i
        else:
            word=str(BENGALURU_COLLEGE_CODES[j])+"13CS%d" %i 
        br.open("http://results.vtu.ac.in/vitavireval.php") #Open URL
        #br.select_form(nr=0) #Select first form
        br.form = list(br.forms())[0]
        br['rid']=word #Enter the value to be entered into the form field
        response = br.submit()
        stri=response.read()
        #print str
        s = BeautifulSoup(stri,"html.parser")
        for tr in s.find_all('tr'):
            columns = tr.find_all('td')
            if len(columns) == 6:
                if columns[0].text=="Management & Entrepreneurship (10AL61)":
                    mgmnt_total+=1
                    if int(columns[2].text)-int(columns[1].text) != 0:
                        mgmnt_new.append(int(columns[2].text)-int(columns[1].text))
                elif columns[0].text=="Operations Research (10CS661)":
                    or_total+=1
                    if int(columns[2].text)-int(columns[1].text) != 0:
                        or_new.append(int(columns[2].text)-int(columns[1].text))
                elif columns[0].text=="Unix System Programming (10CS62)":
                    usp_total+=1
                    if int(columns[2].text)-int(columns[1].text) != 0:
                        usp_new.append(int(columns[2].text)-int(columns[1].text))
                elif columns[0].text=="Compiler Design (10CS63)":
                    cd_total+=1
                    if int(columns[2].text)-int(columns[1].text) != 0:
                        cd_new.append(int(columns[2].text)-int(columns[1].text))
                elif columns[0].text=="Computer Networks - II (10CS64)":
                    cn_total+=1
                    if int(columns[2].text)-int(columns[1].text) != 0:
                        cn_new.append(int(columns[2].text)-int(columns[1].text))
                elif columns[0].text=="Computer Graphics & Visualization (10CS65)":
                    cg_total+=1
                    if int(columns[2].text)-int(columns[1].text) != 0:
                        cg_new.append(int(columns[2].text)-int(columns[1].text))
        print i # Uncomment this to keep a track of till where the script has reached.

    mgmnt_new.sort()
    or_new.sort()
    usp_new.sort()
    cd_new.sort()
    cn_new.sort()
    cg_new.sort()
    
    try:
        mgmnt_new_max=np.amax(mgmnt_new)
    except ValueError:
        mgmnt_new_max=0

    try:
       or_new_max=np.amax(or_new)
    except ValueError:
        or_new_max=0

    try:
        usp_new_max=np.amax(usp_new)
    except ValueError:
        usp_new_max=0

    try:
        cd_new_max=np.amax(cd_new)
    except ValueError:
        cd_new_max=0

    try:
        cn_new_max=np.amax(cn_new)
    except ValueError:
        cn_new_max=0

    try:
        cg_new_max=np.amax(cg_new)
    except ValueError:
        cg_new_max=0

    mgmnt_total=(mgmnt_total,1)[bool(mgmnt_total==0)]
    or_total=(or_total,1)[bool(or_total==0)]
    usp_total=(usp_total,1)[bool(usp_total==0)]
    cd_total=(cd_total,1)[bool(cd_total==0)]
    cn_total=(cn_total,1)[bool(cn_total==0)]
    cg_total=(cg_total,1)[bool(cg_total==0)]

    plt.plot(mgmnt_new, label="Mgmnt  T.Stu:"+str(len(mgmnt_new))+"  Max:"+str(mgmnt_new_max)+"  Avg:"+str(round(np.average(mgmnt_new),2))+"  %Stu:"+str(round((len(mgmnt_new)/mgmnt_total*100),2)))
    plt.plot(or_new, label='OR  T.Stu:'+str(len(or_new))+'  Max:'+str(or_new_max)+'  Avg:'+str(round(np.average(or_new),2))+'  %Stu:'+str(round((len(or_new)/or_total*100),2)))
    plt.plot(usp_new, label='USP  T.Stu:'+str(len(usp_new))+'  Max:'+str(usp_new_max)+'  Avg:'+str(round(np.average(usp_new),2))+'  %Stu:'+str(round((len(usp_new)/usp_total*100),2)))
    plt.plot(cd_new, label='CD  T.Stu:'+str(len(cd_new))+'  Max:'+str(cd_new_max)+'  Avg:'+str(round(np.average(cd_new),2))+'  %Stu:'+str(round((len(cd_new)/cd_total*100),2)))
    plt.plot(cn_new, label='CN  T.Stu:'+str(len(cn_new))+'  Max:'+str(cn_new_max)+'  Avg:'+str(round(np.average(cn_new),2))+'  %Stu:'+str(round((len(cn_new)/cn_total*100),2)))
    plt.plot(cg_new, label='CG  T.Stu:'+str(len(cg_new))+'  Max:'+str(cg_new_max)+'  Avg:'+str(round(np.average(cg_new),2))+'  %Stu:'+str(round((len(cg_new)/cg_total*100),2)))

    plt.legend()
    pic_header="Reval data of 130 CSE 6th sem VTU students of "+str(BENGALURU_COLLEGE_CODES[j])+" college"
    plt.title(pic_header)
    pp.savefig()
    
pp.close()
