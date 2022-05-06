from flask import Flask,request,make_response,send_file,redirect
import api
app = Flask('app')
"""draft for profile------
<button class="button" style="display:inline;float:left;">Profile</button>
<button class="button" style="display:inline;float:right;">Create</button>
<h2 style="text-align:center;">Branch</h2>
<hr noshade/>
<div class="Profile">
	<div class="profile-top">
    	<p style="text-decoration:bold;">{username}</p>
        <p>{shortdesc}</p>
    </div>
    <hr/>
    <p>{longdesc}</p>
    <hr/>
    <div class="mod_embed">
    	<p class="ting">{mod1}</p>
    	<p class="ting">{mod1short}</p>
    </div>
    <div class="mod_embed">
    	<p class="ting">{mod2}</p>
        <p class="ting">{mod2short}</p>
    </div>
    <div class="mod_embed">
    	<p class="ting">{mod3}</p>
        <p class="ting">{mod3short}</p>
	</div>
</div>"""
@app.route('/')
def index():
  cookie = request.cookies.get('Token')
  if api.cookie.valid(cookie):
    return '''
    <link rel="stylesheet" href="api/style">
<button class="button" style="display:inline;float:left;">Profile</button>
<button class="button" style="display:inline;float:right;">Create</button>
<h2 style="text-align:center;">Branch</h2>
<hr noshade/>'''
  else:
    return '''
<link rel="stylesheet" href="api/style">
<button class="button" style="display:inline;float:left;">Sign in</button>
<button class="button" style="display:inline;float:right">Sign up</button>
<h2 style="text-align:center;">Branch</h2>
<hr noshade/>'''
######################
#resp = make_response(render_template())
#resp.set_cookie('userID', user)
#<link rel="stylesheet" href="api/style">
@app.route('/login')
def login():
  return 'cool'

@app.route('/profile')
@app.route('/profile/<ID>')
def profiles(ID=None):
  if ID==None:
    cookie = request.cookies.get('Token')
    if cookie == None:
      return redirect("/login",302)

@app.route('/api/<s>')
def getstylebecausecool(s):
  if s=="style":
    return send_file("src/html/index.css")
  return send_file("src/html/"+str(s))

#@app.route('/favicon.ico')
app.run(host='0.0.0.0', port=80)