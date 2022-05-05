from flask import Flask,render_template,request
import api
app = Flask('app')

@app.route('/')
def index():
  cookie = request.cookies.get('Token')
  if api.cookie.valid(cookie):
    return '''
<button style="display:inline;float:left;"></button>
<button style="display:inline;float:right;">{buttonr}</button>
<h2 style="text-align:center;">Branch</h2>
<hr noshade/>'''

app.run(host='0.0.0.0', port=80)