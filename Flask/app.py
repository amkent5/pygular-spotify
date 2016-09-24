import math as m
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)
app.debug = True

@app.route("/")
def index():
	return "Flask App"

"""
@app.route("/<string:name>/")
def hello(name):
	return render_template(
		'content.html', name=name)
"""

# Pass multiple variables to content.html (the name and a random quote)
@app.route("/<name>")
def appCode(name):

	quotes = [ "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
		"'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
		"'To understand recursion you must first understand recursion..' -- Unknown",
		"'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
		"'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
		"'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"
		]
	randomNumber = randint(0,len(quotes)-1) 
	rand_quote = quotes[randomNumber] 

	# locals returns all local variables within the function to the content.html page
	return render_template(
		'content.html', **locals()
		)

# Extention gives the user the primes below a specified number
@app.route("/<name>")
@app.route("/<name>/<int:integer>")
def primesBelow(name, integer):
	#return "hey primes " + str(integer)
	
	l_primes = [2, 3]
	for n in range(4, integer):
		isPrime = True
		for d in range(2, int(m.ceil(m.sqrt(n) + 1))):
			if n % d == 0:
				isPrime = False
		if isPrime == True:
			l_primes.append(n)
	prime_string = ''
	for p in l_primes:
		str_p = str(p)
		prime_string += str_p
		prime_string += ' '

	return prime_string

if __name__ == "__main__":
	app.run()
