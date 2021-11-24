from flask import Blueprint, render_template, session, redirect
from app import db
from app.models import Post 
from app.db import get_db

bp = Blueprint('home', __name__, url_prefix='/')

@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()

  return render_template(
  'homepage.html',
  posts=posts,
  loggedIn=session.get('loggedIn')
)


@bp.route('/login')
def login():
  # not logged in yet
  if session.get('loggedIn') is None:
    return render_template('login.html')

  return redirect('/dashboard')

@bp.route('/post/<id>')
def single(id):
  # get single post by id
  db = get_db()
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template(
  'single-post.html',
  post=post,
  loggedIn=session.get('loggedIn')
)

@bp.route('/users/logout', methods=['POST'])
def logout():
  # remove session variables
  session.clear()
  return '', 204

@bp.route('/users/login', methods=['POST'])
def login():
 data = request.get_json()
 db = get_db()

try:
    user = db.query(User).filter(User.email == data['email']).one()
except:
   print(sys.exc_info()[0])
return jsonify(message = 'Incorrect credentials'), 400
