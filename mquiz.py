import random
import operator #  operator module for using various operations in our quiz
ops={'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}  #define operators dictionary with key:value
#    ops.keys() alone includes output 'dict_keys' which causes errors, therefore must use in list()

print ("Mad Minutes Quiz. Bienvenue.")
print ("***To end the quiz, type 'end'.***")
score = 0 #    if these go in the while loop, they get reset to zero for every question
total_q=0
name=input('Our examinee is: ')
while True:
	print("Select the range of numbers you would like to be quizzed on.")
	try:
		min=int(input('Smallest number: '))
		max=int(input("Largest number: "))
		print ("Let's begin.")
	except ValueError:
		print ("Please enter two numbers.")
		continue #return to start of loop
	else:
		break #no Value Error, we can exit the loop

while True: #   'while True' loop allows a block of code to be repeated indefinitely.
	try:
		r1=random.randint(min, max)
		r2=random.randint(min, (r1-1))
	except ValueError:
		continue
	opr=random.choice(list(ops.keys())) 
	if opr=='-':
		ans=r1-r2	
	elif opr=='+':
		ans=r1+r2
	elif opr=='/':
		ans=r1//r2
	else:
		ans=r1*r2

	quest=input(f'{r1}{opr}{r2}= ') #use f-string to embed {variables} into a string #was going to use int() directly in quest but will cause error if not a numerical input...
	wrong = ["Ha. Try again.", "No.", f"That's not {ans}.", f"That's not {ans}.", f"How don't you know that it's {ans}?", "Can we get a competent test taker for once?", "My bird's brain is bigger than yours.", "Monkey see, monkey cannot do.", f"Time for {name}'s nap."]
	#  making list for wrong answer responses to be randomly chosen from random.choice(list)
	try: #line sthat could produce error in here = anything checking the input value
		if quest=='end':
			print ("End of Quiz.")
			print (f"{name}'s Grade: {score}/{total_q}")
			break
		total_q += 1
		if ans==int(quest):
			print("...correct.")
			score += 1
		else:
			print(random.choice(wrong))
	except ValueError:#non numerical answer input will cause ValeuError
		print("This is not imaginary math. Numbers only, please.")
		continue

