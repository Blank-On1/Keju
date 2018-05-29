from flask import Flask,request,Response,jsonify
from peneliti import sasa as sa 
from peneliti import sasa as aww
import scholarly,json

app = Flask(__name__)

@app.route('/<gurih>')
def hello_world(gurih):
    return gurih

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/crot', methods=['POST'])
def login():
	return request.form['anu']

@app.route('/peneliti/afiliasi/<kental>',methods=['GET'])
def coba(kental):
	data = sa.search(kental)
	return str (data)

@app.route('/peneliti/afiliasi/<kental>',methods=['GET'])
def geulis(kental):
	data =  aww.search(kental)
	return jsonify(data)

