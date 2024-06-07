from flask import Flask, render_template

app = Flask(__name__)
template_dict = {'1':{"item":'apples','value':2,'request_date':'2024'},'2':{"item":'potatoes','value':5,'request_date':'2024'}}
@app.route('/')
def index():
    return render_template('index.html', boxes=template_dict)


if __name__ == '__main__':
    app.run()
