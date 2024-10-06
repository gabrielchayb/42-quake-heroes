from flask import Flask, render_template

app = Flask(__name__)

# home, index, first page , redirect to receivingcode
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solarsystem')
def solarsystem():
    return render_template('solarsystem.html')

@app.route('/home')
def home ():
    return render_template('home.html')

@app.route('/homemoon')
def homemoon():
    return render_template('homemoon.html')

# scene in mars , second piece of text
@app.route('/homemars')
def homemars():
    return render_template('homemars.html')

# third piece of text moon
@app.route('/hometired')
def hometired():
    return render_template('hometired.html')

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
@app.route('/moonquakes')
def moonquakes():
    return render_template('moonquakes.html')

@app.route('/moonquake1')
def moonquake1():
    return render_template('moonquake1.html')

@app.route('/moonquake2')
def moonquake2():
    return render_template('moonquake2.html')

@app.route('/moonquake3')
def moonquake3():
    return render_template('moonquake3.html')


@app.route('/marsquake1')
def marsquake1():
    return render_template('marsquake1.html')

@app.route('/team')
def team():
    return render_template('team.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html')

if __name__ == '__main__':
    app.run(debug=True)