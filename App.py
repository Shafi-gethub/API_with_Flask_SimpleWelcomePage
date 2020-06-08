from flask import Flask


app = Flask(__name__)

@app.route('/<name>')
def welcomeNote(name):
	return 'Hello {}, Welcom to my python with flask API, This is just a project that indicates the creation of virtual enviroment and flask:'.format(name)