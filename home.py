from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html')
@app.route('/profile')
def profile():
    return render_template('profile.html')
@app.route('/action')
def action():
    return render_template('action.html')
@app.route('/comedy')
def comedy():
    return render_template('comedy.html')
@app.route('/love')
def love():
    return render_template('love.html')
@app.route('/horror')
def horror():
    return render_template('horror.html')
@app.route('/fantasy')
def fantasy():
    return render_template('fantasy.html')
@app.route('/history')
def history():
    return render_template('historical.html')
@app.route('/mystery')
def mystery():
    return render_template('mystery.html')
@app.route('/sci-fi')
def sci_fi():
    return render_template('sci-fi.html')
@app.route('/streem')
def stree():
    return render_template('streempage.html')


if __name__ == '__main__':
    app.run(debug=True , port= 1212)
