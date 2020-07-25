def no_question(Q):
	count = 1
	print(f"therse are total {Q} questions")
	f = open("answers.txt",'w')
	for i in range(Q):
		ans = input(f"question {count}  give your answwer in [a/b/c/d] only => : ")
		if ans == 'a' or ans == 'b' or ans == 'c' or ans == 'd':
			print(f"done, your answer is {ans}")
		else:
			print("answer can't be anything else @@@")
			ans = ''
			print("your answr is NULL")

		f.writelines(f"{count}.({ans})\n")
		count += 1




que = int(input("enter no of question :"))
no_question(que)
