from flask import Flask, render_template

app = Flask(__name__)

# home, index, first page , redirect to receivingcode
@app.route('/')
def home():
    return render_template('home.html')

# second piece of text
@app.route('/home1')
def home1():
    return render_template('home1.html')

# from home1, redirect to posreceivied 
@app.route('/receivingcode')
def receivingcode():
    return render_template('receivingcode.html')

# from receivingcode, redirect to explaining
@app.route('/posreceivied')
def posreceivied():
    return render_template('posreceivied.html')

# from posreceivied, redirect to choosemission
@app.route('/explaining')
def explaining():
    return render_template('explaining.html')

# from explaining, redirect to : apollo OR mars insight lander
@app.route('/choosemission')
def choosemission():
    return render_template('choosemission.html')




if __name__ == '__main__':
    app.run(debug=True)