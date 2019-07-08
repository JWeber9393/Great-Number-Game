from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = "number_guess"


@app.route("/")
def index():
    print('*'*100)
    print("root route working")

    if 'message' not in session:
        session["message"]=""

    if 'number' not in session:
        session['number'] = random.randint(1, 100)

    print("The random number is", session['number'])
    
    return render_template('gng_index.html')

@app.route("/guess", methods= ["POST"])
def guess():
    print('*'*100)
    print("guess proccesseing")
    if int(request.form['guess']) == session['number']:
        session['message'] = "You win!!!"

    if int(request.form['guess']) > session['number']:
        session['message'] = "Lower"

    if int(request.form['guess']) < session['number']:
        session['message'] = "Higher"
    
    return redirect('/')

@app.route("/reset", methods=['POST'])
def reset():
    print('*'*100)
    print("resetting")
    session.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)