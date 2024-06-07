from flask import Flask, redirect, render_template, request
from database import * 

app = Flask(__name__)
template_dict = [{"request_id":1,"item":'apples','value':2,'request_date':'2024'},{"request_id":2,"item":'potatoes','value':5,'request_date':'2024'}]

current_user = None

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        global current_user
        email = request.form['email']
        name = request.form['name']
        address = request.form['address']
        current_user = create_user(email,name, address)
        if request.form['role'] == 'donator':
            return redirect('/donate')
        else:
            return redirect('/distributor')
    return render_template('index.html')

@app.route('/donate', methods=['GET','POST'])
def donate():
    print(get_all_requests())
    global current_user
    if current_user:
        if request.method == 'POST':
            request_id = request.form['request_id']
            amount = request.form['amount']
            fulfill_request(request_id, amount)
    return render_template('donator.html', boxes=get_all_requests())
    
@app.route('/process_login', methods=['POST'])
def process_login():
    global current_user
    email = request.form['email']
    name = request.form['name']
    address = request.form['address']
    current_user = create_user(email,name, address)
    if request.form['role'] == 'donator':
        return render_template('donator.html', boxes=get_all_requests())
    else:
        return render_template('distributor.html')


@app.route('/distributor', methods=['GET','POST'])
def distribute():
    global current_user
    if request.method == 'POST':
        foodType = request.form['foodType']
        amount = request.form['quantity']
        process_new_request(current_user, foodType, amount)
    return render_template('distributor.html')

if __name__ == '__main__':
    app.run()
