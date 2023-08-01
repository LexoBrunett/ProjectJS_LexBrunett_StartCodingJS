import random as rd

excuse = 'The dog eat my homework when I finished'

who = ['The dog', 'My grandma', 'His turtle', 'My bird'];
action = ['ate', 'peed', 'crushed', 'broke'];
what = ['my homework', 'the keys', 'the car'];
when = ['before the class', 'right on time', 'when I finished', 'during my lunch', 'while I was praying'];

def excusegenerator():
	word_who = rd.range(len(who))
	word_action = rd.range((action))
	word_what = rd.range(len(what))
	word_when = rd.range(len(when))

	excuse = who[word_who] + " "+ action[word_action]+ " "+ what[word_what]+ " "+ when[word_when]
	return excuse

print(excusegenerator)