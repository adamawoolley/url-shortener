from flask import Flask, redirect, request, render_template
from pymongo import MongoClient

db = MongoClient('mongodb://localhost:27017/')['url-shortener']['urls']
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print('bob')
        print(request.form['url'])
        print({'url':request.form['url']})
        id = db.insert_one({'url': request.form['url']}).inserted_id
        return render_template('url_shortener.html', url=id)
    return render_template('url_shortener.html')

@app.route('/<int:id>')
def reroute(id):
    return redirect(db.find({}, {'_id': id})['url'])

if __name__ == "__main__":
    app.run(debug=True)
