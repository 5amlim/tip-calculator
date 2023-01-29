from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def render_home():
    return render_template('index.html')

@app.route('/', methods = ["POST"])
def calculate():
    if request.method == 'POST':
        bill = request.form['bill']
        tip = request.form['tip']
        people = request.form['people']
        tip_total = float(bill) * float(tip) / 100
        result = round((float(bill)+tip_total)/float(people), 2)
        total = round(float(bill) + tip_total, 2)
        return render_template('index.html', result = result, total = total)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)