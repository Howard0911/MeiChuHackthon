#import os
#os.chdir('D:/python/Pprogram')

f1 = open('./stores_old.csv','r',encoding = 'big5')
f2 = open('./stores_new.csv','w',encoding = 'utf-8')
info = f1.readlines()
f1.close()

for i in range(0,len(info)):
        info[i] = info[i].strip()
        info[i] = info[i].split(',')
        info[i].remove(info[i][1])
        info[i].remove(info[i][1])
        info[i].remove(info[i][2])
        info[i].remove(info[i][4])
        #print(info[i])
        f2.write(','.join(info[i]))
        f2.write(',')
        f2.write('\n')
del info
f2.close()
f2 = open('./stores_new.csv','r',encoding = 'utf-8')
info = f2.readlines()
for i in range(0,len(info)):
        info[i] = info[i].strip()
        #info[i] = info[i].split(',')
        #info[i].append('')
        print(info[i])
f2.close()
     

