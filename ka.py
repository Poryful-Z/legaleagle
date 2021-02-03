import flask,threading
app = flask.Flask('')
@app.route('/')
def home():
  return 'Alive!'
def run():
  app.run(host='0.0.0.0',port=8080)
def ka():  
    t = threading.Thread(target=run)
    t.start()