import flask

#create an instance of Flask
app = flask.Flask('Earthquake Model Deployment')
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def home():
    return "Halo dunia tipu tipu!"

if __name__ == "__main__":
    app.run(port=int(os.environ.get("PORT", 5000)),host='0.0.0.0',debug=True)
