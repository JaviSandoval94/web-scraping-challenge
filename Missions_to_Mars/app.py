# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

# MongoDB config
mongo = PyMongo(app, uri = 'mongodb://localhost:27017/mars_app')

# Home: return data saved in DB
@app.route('/')
def home():
    mars = mongo.db.mars.find_one()
    return render_template('index.html', mars = mars)

# /scrape: scrape data, save to DB and redirect to home
@app.route('/scrape')
def scrape():
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape()
    mars.update({}, mars_data, upsert = True)
    return redirect('/', code = 302)

if __name__ == "__main__":
    app.run(debug=True)