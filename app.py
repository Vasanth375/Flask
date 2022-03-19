# program on dynamic html templates

# importing libraries
from flask import Flask, render_template

# creating flask object
app=Flask(__name__)

# home link 
# @app.route('/')
# def hello():
#     return "hello this is main page <h1> hello </h1>"

# this is the dynamic html example
# whatever the 
@app.route('/<hold>')
def hello(hold):
    return render_template('home.html', hold=hold)

@app.route('/joker/<name>')
def ok(name):
    return render_template('home.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)

