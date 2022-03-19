# program on dynamic html templates
# importing libraries
from flask import Flask, render_template

# creating flask object
app=Flask(__name__)

# this is the dynamic html example
# whatever the hold variable you search on search bar that will display on the page
@app.route('/<hold>')
def hello(hold):
    return render_template('home.html', hold=hold)


@app.route('/joker/<name>')
def ok(name):
    return render_template('home.html', name=name)

if __name__ == "__main__":
    app.run(debug=True)

