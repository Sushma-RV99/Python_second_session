from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')

def hello_world():
    return render_template("index.html")

@app.route ('/about', methods=['GET'])
def about():
    return render_template("about.html")

@app.route ('/vision', methods=['GET'])
def vision():
    return render_template("vision.html")

@app.route ('/messages', methods=['GET'])
def messages():
    return render_template("messages.html")

@app.route ('/academics', methods=['GET'])
def academics():
    return render_template("academics.html")

@app.route ('/academics_overview', methods=['GET'])
def academics_overview():
    return render_template("academics_overview.html")

@app.route ('/academics_civil', methods=['GET'])
def academics_civil():
    return render_template("academics_civil.html")

@app.route ('/academics_mechanical', methods=['GET'])
def academics_mechanical():
    return render_template("academics_mechanical.html")

@app.route ('/admission', methods=['GET'])
def admission():
    return render_template("admission.html")

@app.route ('/scholarship', methods=['GET'])
def scholarship():
    return render_template("scholarship.html")

@app.route ('/Research', methods=['GET'])
def Research():
    return render_template("Research.html")

@app.route ('/contact', methods=['GET'])
def contact():
    return render_template("contact.html")

@app.route ('/placement', methods=['GET'])
def placement():
    return render_template("placement.html")

@app.route ('/recruiters', methods=['GET'])
def recruiters():
    return render_template("recruiters.html")

@app.route ('/records', methods=['GET'])
def records():
    return render_template("records.html")

if __name__=='__main__':
    app.run(debug=True)