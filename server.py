from flask import Flask, render_template, request, redirect
import test, random, json

app = Flask(__name__)

names = test.get_names()

@app.route('/')
def index():
    names = test.get_names()
    namesLength = len(names)
    oponent1 = names["n" + str(random.randint(0, namesLength))]
    oponent2 = names["n" + str(random.randint(0, namesLength))]
    return render_template("index.html", oponent1=oponent1, oponent2=oponent2)

@app.route("/info/<id>")
def info(id):
    person = names[id]
    the_same_persons = []
    for key, other in names.items():
        if other["name"].lower() == person["name"].lower():
            the_same_persons.append(other)
    repeatings = len(the_same_persons)
    return render_template("info.html", person=person, the_same_persons=the_same_persons, repeatings=repeatings)

@app.route("/search", methods=["POST", "GET"])
def search():
    name = request.form['name'].strip()
    results = []
    for key, other in names.items():
        if other["name"].lower() == name.lower():
            results.append(other)
    repeatings = len(results)
    return render_template("search.html",results=results, repeatings=repeatings)

@app.route("/vote/<id>")
def vote(id):
    names[id]["likes"] += 1
    test.save(names)
    return redirect("/")

@app.route("/vote_person/<id>")
def vote_person(id):
    names[id]["likes"] += 1
    test.save(names)
    return redirect("/info/" + id)

if __name__ == '__main__':
    app.run()