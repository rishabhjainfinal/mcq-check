import time 
import os



def per_cal(ansfile='answers.txt',keyfile="key.txt"):	
	ans = [(i.replace('\n','').split('.')[1]) for i in open(ansfile,'r').readlines()]
	key = [(i.replace('\n','').split('.')[1]) for i in open(keyfile,'r').readlines()]
	per = 0
	for i in range(len(key)):
		if ans[i]  == key[i]:
			per +=1

	os.system("cls")
	print(f"print your percentage is :{round((per/len(key))*100,2)}%")

	time.sleep(5)

per_cal()