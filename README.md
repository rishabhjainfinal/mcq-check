# This python project is to check mcqs from a file collect from a source 

## how its work..

* file **key.txt** cointain all answers of the questions

* **take_answers.py** take answers and make a file **answers.txt** of your given answers and show **percentage** (you can give answers in [a/b/c/d] or leave it blank, code can be update for negative markings later)

#un-comment these line in **take_ans.py** for hard checking
```
per_cal()

# for hard testing on every wrong answers you get -0.5 marks ans rigth one 1 
# per_cal(type='hard')
```

* **ans_check.py** check ans from **answers.txt** file and provide results in **percentage**
