import os
import os
import subprocess
import re
 
def extractIp(ip):
    result = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip ) #IP 추출 정규식
    return str(result).replace('[]','').replace('[', '').replace(']', '').replace("'",'')#추출시 지저분한것들을 없앤다.
 
cmd = "ipconfig"
f = open('new.txt','w')
sysMsg = subprocess.getstatusoutput(cmd)
f.write(sysMsg[1])
f.close()
 
ip_list = []
f2 = open('new.txt', 'r')
line = []
while True :
    line = f2.readline() #한줄씩 읽습니다.
    getIp = extractIp(line) #정규식으로 ip만 뽑아냅니다.    
    if(getIp != ''): 
        ip_list.append(getIp) # 뽑아낸 IP를 리스트형태로 저장합니다.
    if("" == line) :        
        break
 
f3 = open('new2.txt','w')
f3.write(str(ip_list))
 
f2.close()
f3.close()
 
print(ip_list)
 
print(ip_list[0])
print(ip_list[1])
print(ip_list[2])
print(ip_list[3]) 
print("COMPLTE")
import subprocess
import re
 
def extractIp(ip):
    result = re.findall( r'[0-9]+(?:\.[0-9]+){3}', ip ) #IP 추출 정규식
    return str(result).replace('[]','').replace('[', '').replace(']', '').replace("'",'')#추출시 지저분한것들을 없앤다.
 
cmd = "ipconfig"
f = open('new.txt','w')
sysMsg = subprocess.getstatusoutput(cmd)
f.write(sysMsg[1])
f.close()
 
ip_list = []
f2 = open('new.txt', 'r')
line = []
while True :
    line = f2.readline() #한줄씩 읽습니다.
    getIp = extractIp(line) #정규식으로 ip만 뽑아냅니다.    
    if(getIp != ''): 
        ip_list.append(getIp) # 뽑아낸 IP를 리스트형태로 저장합니다.
    if("" == line) :        
        break
 
f3 = open('new2.txt','w')
f3.write(str(ip_list))
 
f2.close()
f3.close()
 
print(ip_list)
 
print(ip_list[0])
print(ip_list[1])
print(ip_list[2])
print(ip_list[3]) 
print("COMPLTE")
