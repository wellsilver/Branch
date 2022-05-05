from flask import Flask,request,make_response,send_file
import api
app = Flask('app')

@app.route('/')
def index():
  cookie = request.cookies.get('Token')
  if api.cookie.valid(cookie):
    return '''
<button style="display:inline;float:left;">Profile</button>
<button style="display:inline;float:right;">Create</button>
<h2 style="text-align:center;">Branch</h2>
<hr noshade/>'''
  else:
    return '''
<button style="display:inline;float:left;">Sign in</button>
<button style="display:inline;float:right">Sign up</button>
<h2 style="text-align:center;">Branch</h2>
<hr noshade/>'''
######################
#resp = make_response(render_template())
#resp.set_cookie('userID', user)
@app.route('/profile')
@app.route('/profile/<ID>')
def profiles(ID=None):
  if ID==None:
    cookie = request.cookies.get('Token')


@app.route('/api/style')
def getstylebecausecool():
  return send_file("html/index.css")
    
app.run(host='0.0.0.0', port=80)