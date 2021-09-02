#시간 확인
def time(x) :
    x=x.split(":")
    hour=int(x[0])*60*60
    minute=int(x[1])*60
    second=int(x[2])

    return hour+minute+second

#출석 채팅만
def formCheck(arr) : 
    x=[]
    for i in arr :
        if len(i[0])==9 and i[0][0:2]=="20":
            x.append(i)
    return x

def frist(arr) :
    for i in arr :
        i.append("X")


import os
import csv

#출석부 open
checkBook=[]
with open('test file.csv',encoding='utf-8-sig') as csvfile:
    f2 = csv.reader(csvfile)
    for i in f2 :
        checkBook.append(i)
frist(checkBook)

#출석 채팅 opne(학번 이름 기준)
f = open("출석 test.txt", 'r',encoding='utf8')


#출석 마감 시간
deadline = time("15:10:00")

#디렉토리 check
print(os.getcwd())

arr=[] #임시 파싱
check=[] #출석 명단
late=[] #지각 채팅
#while(True):

#시간 분리
try :
    for i in range(10000):
        arr.append(f.readline().split())
        if time(arr[i][0])<=deadline :
            check.append([arr[i][len(arr[i])-2],arr[i][len(arr[i])-1]])
        else : 
            late.append([arr[i][len(arr[i])-2],arr[i][len(arr[i])-1],arr[i][0]])

        #print(arr[i]) 전체 표기

        #학번 이름 채팅만 ex) 202012345 홍길동
except :
    late = formCheck(late)
    check = formCheck(check)
f.close()

for i in checkBook :
    for j in check:
        if i[0]==j[0] and i[1]==j[1]:
                i[2]="O"

#지각생
print("------------지각--------------")
for i in late :
    print(i)
print("------------------------------")


with open('output.csv','w', newline='',encoding='utf-8-sig') as csvfile:
    wr = csv.writer(csvfile)
    for i in checkBook : 
        print(i)
        wr.writerow(i)