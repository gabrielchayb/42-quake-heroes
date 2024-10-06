from flask import Flask, render_template

app = Flask(__name__)

# home, index, first page , redirect to receivingcode
@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/solarsystem')
def solarsystem():
    return render_template('solarsystem.html')

@app.route('/home')
def home ():
    return render_template('home.html')

# scene in mars , second piece of text
@app.route('/mars')
def mars():
    return render_template('mars.html')

# second piece of text moon
@app.route('/home2')
def home2():
    return render_template('home2.html')

# third piece of text moon
@app.route('/home1')
def home1():
    return render_template('home1.html')

# from home1, redirect to poscode , that is the video page 
@app.route('/receivingcode')
def receivingcode():
    return render_template('receivingcode.html')

# from receivingcode, redirect to choose mission
@app.route('/poscode')
def poscode():
    return render_template('poscode.html')

# from explaining, redirect to : apollo OR mars insight lander
@app.route('/choosemission')
def choosemission():
    return render_template('choosemission.html')

# from posreceivied, redirect to choosemission
@app.route('/explaining')
def explaining():
    return render_template('explaining.html')



if __name__ == '__main__':
    app.run(debug=True)