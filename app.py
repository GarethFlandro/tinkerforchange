from flask import Flask, render_template, request
from database import * 
app = Flask(__name__)
template_dict = [{"request_id":1,"item":'apples','value':2,'request_date':'2024'},{"request_id":2,"item":'potatoes','value':5,'request_date':'2024'}]

@app.route('/')
def index():
    return render_template('index.html', boxes=get_all_requests())
@app.route('/donate')
def donate():
    if request.method == 'POST':
        request_id = request.form['request_id']
        amount = request.form['amount']
        fulfill_request(request_id, amount)
    render_template('index.html', boxes=get_all_requests())
    return 'Donation successful'
if __name__ == '__main__':
    app.run()
