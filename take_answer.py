from ans_check import per_cal
import os
# take answers and make a file answers.txt or update if exist!
def no_question(Q):
	os.system("cls")
	count = 1
	print(f"there are total {Q} questions")
	print(f"you can not edit the answer if once given all {Q} questions are necessary")
	f = open("answers.txt",'w')
	for i in range(Q):
		ans = input(f"question {count}  give your answwer in [a/b/c/d] only => : ")
		if ans == 'a' or ans == 'b' or ans == 'c' or ans == 'd':
			print(f"done, your answer is {ans}")
		else:
			print("answer can't be anything else \nyour answer is set to be NULL ()")
			ans = ''

		f.writelines(f"{count}.({ans})\n")
		count += 1

# que = int(input("enter no of question :"))
# len(open('key.txt','r').readlines()) return total numbers of questions to take answers
no_question(len(open('key.txt','r').readlines()))
# give results after completing the answers 	
per_cal()


# for hard testing on every wrong answers you get -0.5 marks ans rigth one 1 
# per_cal(type='hard')
