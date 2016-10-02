import spotipy
import math as m
from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)
app.debug = True
sp = spotipy.Spotify()

# use method of insertion decribed in http://jsfiddle.net/euQ5n/175/
def buildHtmlString(l_uris):
	
	output_str = '<table align="center" style="width:60%">'
	end_str = '</table>'

	# for every even pass need to close the tr
	for i, uri in enumerate(l_uris):
		if i % 2 == 0:
			output_str += '<tr><td><iframe src=' \
				+ '"https://embed.spotify.com/?uri=' \
				+ uri \
				+ '&view=coverart" frameborder="0" allowtransparency="true">' \
				+ '</iframe></td>'
		else:
			output_str += '<td><iframe src=' \
				+ '"https://embed.spotify.com/?uri=' \
				+ uri \
				+ '&view=coverart" frameborder="0" allowtransparency="true">' \
				+ '</iframe></td></tr>'

	output_str += end_str
	return output_str

@app.route("/")
def index():
	return "Flask App"

# Pass multiple variables to content.html (the artists name, list of top 20 track URI's and a random quote)
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

	# get top 20 track URIs for searched artist and return in list form
	results = sp.search(q=name, limit=20)
	l_res = []
	for i, t in enumerate(results['tracks']['items']):
		l_res.append(str(t['uri']))

	# form htmlString
	htmlString = buildHtmlString(l_res)
	print htmlString

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
