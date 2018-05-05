from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
	return render_template("index.html", times = 10)
@app.route("/<idx>/")
def limited(idx):
	return render_template("index.html", times = int(idx))

if __name__ == "__main__":
	app.run(debug=True)