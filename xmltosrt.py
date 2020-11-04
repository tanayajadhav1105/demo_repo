import re, sys
from bs4 import BeautifulSoup
import math

if len(sys.argv) < 2:
    print("Need file name!")
    sys.exit(2)

f = open(sys.argv[1],"r")
s = f.read()
srt = open("output.srt","w")

#s = s.replace('<br />', '\n')
soup = BeautifulSoup(s,"xml")


def c_time(st):
	fr=0
	h=0
	m=0
	s=0
	fr,i=math.modf(st)
	s=int(i)
	if i>=60:
		m=int(i//60)
		s=int(i%60)
		if m>=60:
			h=int(m//60)
			m=int(m%60)
		
	if h<=9:
		hr="0"+str(h)
	else:
		hr=str(h)
	if m<=9:
		mi="0"+str(m)
	else:
		mi=str(m)
	if s<=9:
		sec="0"+str(s)	
	else:
		sec=str(s)
	fr=fr*1000
	fr=int(fr)
	if fr<=9:
		fo="00"+str(fr)	
	elif fr<=99:
		fo="0"+str(fr)
	else:
		fo=str(fr)
	final=hr+":"+mi+":"+sec+","+fo
	return final	

c=0
for text_tag in soup.find_all('text'):
		
	st=float(text_tag.get('start'))
	stime=c_time(st)
	et=float(text_tag.get('dur'))
	et=et+st
	etime=c_time(et)	
	sen = text_tag.text
		
	c=c+1	
	sentence=str(c)+"\n"+stime+" --> "+etime+"\n"+sen+"\n\n"
	srt.write(sentence)
	
		



f.close()
srt.close()
