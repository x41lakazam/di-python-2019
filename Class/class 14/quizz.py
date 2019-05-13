##### Functions #####
# Defining a function
'''
def <name_of_the_function>(<argument1>, <argument2>):		
	#CODE
	#CODE

	return None
'''

def tokenize(s, splitter=' '):
	# "hello world" -> ['HELLO', 'WORLD']
	words = s.split(splitter)
	lst = []
	for word in words:
		lst.append(word.upper())

	return lst 

# result = tokenize("Hello how are you i am eyal", splitter=' ',)
# print(result)

	
def quizz(question, answer):
	print(question)
	user_answer = input("$ ")
	if user_answer.upper() == answer.upper():
		print("Good!")
		return True
	else:
		print("Sorry, the answer was", answer)
		return False		



def quizz_w_lives(lives, question, answer):
	attempts = 0
	while attempts < lives:
		good_answer = quizz(question, answer)
		if good_answer:
			print("Great!		")
			return True
		print("No, {} lives left".format(lives-attempts))
		attempts += 1
	print("Sorry, the answer was", answer)
	return False

def parse_question_in_one_line(s):
	return {'question':s.split(':::')[0], 'answer': s.split(':::')[1]}

def parse_question(s):
	split_s = s.split(':::')

	# Build a dictionnary
	dic = {
		'question': split_s[0],
		'answer': split_s[1]
	}

	return dic

def ask_from_string(s):
	q_and_a = parse_question(s) 
	return quizz(q_and_a['question'], q_and_a['answer'])


def big_quizz(list_of_s):
    if len(list_of_s) < 10:
        raise ValueError("Please input more than 10 questions")
    for sentence in list_of_s:
        try:
            assert ":::" in sentence
        except AssertionError:
            print("Problem on sentence {}, skipping.".format(sentence))
        else:
            ask_from_string(sentence)


strings = [
	"How old is Eyal?:::20",
	"How old is Mickey Mouse?::89",
	"What is the best language in the world?:::Python"
]

big_quizz(strings)
