from flask import Flask, render_template

app = Flask(__name__)
template_dict = {'1':{"Item":'apples','value':2,'request_date':'2024'}}
@app.route('/')
def index():
    return render_template('index.html', )


if __name__ == '__main__':
    app.run()
