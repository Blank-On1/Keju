from flask import Flask,request,Response,jsonify
from flaskext.mysql import MySQL
from peneliti import sasa as sa 
from peneliti import sasa as aww
import scholarly,json

app = Flask(__name__)
mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'latihan'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'

mysql.init_app(app)

@app.route('/a')
def get():
    cur = mysql.connect().cursor()
    cur.execute('''select * from latihan.coba''')
    r = [dict((cur.description[i][0], value)
              for i, value in enumerate(row)) for row in cur.fetchall()]
    return jsonify({'myCollection' : r})


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

# @app.route('/peneliti/afiliasi/<kental>',methods=['GET'])
# def geulis(kental):
# 	data =  aww.search(kental)
# 	return jsonify(data)


