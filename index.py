from flask import Flask,render_template,redirect,request,jsonify
import sys
sys.path.insert(0, 'scrapper')
from ScrapperFactory import ScrapperFactory
from flask_cors import CORS,cross_origin
import datetime,json
app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def index():
	return redirect("https://marcosorive.github.io/torky/")

@app.route('/api/search/<query>/<store>', methods = ['GET'])
@cross_origin()
def search_games(query,store):
	try:
		s=ScrapperFactory()
		result=s.buildScrapper(query,store).get_price()
		return jsonify(	status=200,
						price=result[0],
						url=result[1],
						gamename=result[2])
	except Exception as e:
		return jsonify(status=500,error=str(e))

@app.errorhandler(404)
def page_not_found(e):
	return redirect("https://marcosorive.github.io/torky/")

