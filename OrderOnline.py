from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        order = []
        if 'burger' in request.form:
            order.append('漢堡')
        if 'fries' in request.form:
            order.append('薯條')
        if 'coke' in request.form:
            order.append('可樂')
        return render_template('index.html', submitted=True, order=order)
    return render_template('index.html', submitted=False)

if __name__ == '__main__':
    app.run(debug=True)