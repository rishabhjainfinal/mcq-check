import os

def per_cal(type='simple',ansfile='answers.txt',keyfile="key.txt"):	
	ans = [(i.replace('\n','').split('.')[1]) for i in open(ansfile,'r').readlines()]		
	key = [(i.replace('\n','').split('.')[1]) for i in open(keyfile,'r').readlines()]
	per = 0
	for i in range(len(key)):
		if ans[i]  == key[i]:
			per +=1
		else:
			if type != 'simple':
				per -= 0.5
			else :
				pass

	os.system("cls")
	marks=round((per/len(key))*100,4)
	print(f"your percentage is :{marks}% {'pass' if marks > 33 else 'fail'}")
	print()
	input('enter to end task !!! ')

# per_cal()
