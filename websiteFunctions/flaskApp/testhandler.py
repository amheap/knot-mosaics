import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return """
<h1>Flask Example</h1>
<ul>
<li><a href="decode">Decode</a></li>
<li><a href="form">Form</a></li>
<li><a href="get-example?code=0,0,0,0,0,0,0,0,0">get-example</a></li>
</ul>
"""

@app.route("/decode")
def decode():
    return "Decode"

def makeItHappen(code):
    try:
    	return sum(map(int,code.split(",")))
    except:
        return 0

@app.route("/get-example")
def get_example():
    code = flask.request.args.get("code")
    answer = makeItHappen(code)
    return "The answer for {} is {}.".format(code,answer)

@app.route("/form")
def form():
    return """
<form action="http://137.238.60.166:5000/get-example" method="GET">
<input type="text" name="code">
<input type="submit" value="Hit it!">
</form>
"""

app.run(host="0.0.0.0", port=5000)

