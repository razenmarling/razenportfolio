"""My Portfolio."""


from flask import Flask, render_template

# Initialize flask
app = Flask(__name__, static_url_path='')

# get config
app.config.from_object('config')

@app.route('/')
def index():
	return render_template('index.html')
