from flask import Flask
import api
app = Flask('app')

@app.route('/')
def index():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=80)