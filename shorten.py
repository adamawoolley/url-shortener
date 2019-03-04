from flask import Flask, redirect, request, render_template
from pymongo import MongoClient


db = MongoClient('mongodb://localhost:27017/')['url-shortener']['urls']
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        id = db.insert_one({'_id': db.count() + 1, 'url': request.form['url']}).inserted_id
        return render_template('url_shortener.html', id=id)
    return render_template('url_shortener.html')

@app.route('/<int:id>', methods=['GET'])
def reroute(id):
    print(db.find({}, {'_id': id}))
    for x in db.find({'_id': id}):
        return redirect(x['url'])

if __name__ == "__main__":
    app.run(debug=True)
