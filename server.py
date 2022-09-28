from flask import Flask
import random

random_number = random.randint(0,9)

app = Flask(__name__)

@app.route('/')
def main_page():
    return '<h1 style ="text-align: center">Guess a number between 0 and 9</h1>\
        <p style="text-align:center;"><img src="https://media2.giphy.com/media/A06UFEx8jxEwU/giphy.gif?cid=ecf0\
        5e47nzff6ymrc7687izqtdcsf3snhzwp99pih04gcquz&rid=giphy.gif&ct=g" width=500px>\
        </p>'


@app.route('/<int:number>')
def number_guess(number):
    
    if number > random_number:
        return '<h1 style ="text-align: center">The number is too high!</h1>\
        <p style="text-align:center;"><img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" width=500px>\
        </p>'
        
    elif number < random_number:
        return '<h1 style ="text-align: center">The number is too low!</h1>\
        <p style="text-align:center;"><img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" width=500px>\
        </p>'

    else:
        return '<h1 style ="text-align: center">The number is correct!</h1>\
        <p style="text-align:center;"><img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" width=500px>\
        </p>'

    

if __name__ == "__main__":

    app.run(debug=True)


