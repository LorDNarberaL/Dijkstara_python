from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, TelField
from Controllers.Dijkstra import Dijkstra
from Controllers.Sphero import *
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
dijk = Dijkstra()

class MyForm(FlaskForm):
    startNode = IntegerField("Input Start Node")
    endNode = IntegerField("Input End Node")
    submit = SubmitField("Submit")
    bName = TelField("Sphero Buletooth Name")

@app.route("/")
def index():
    form = MyForm()
    graphList = dijk.printGraph()
    return render_template("index.html", form = form, graph = graphList, graphLenght = len(graphList))

@app.route("/dijkstra", methods = ['GET', 'POST'])
def dijkstra():
    form = MyForm()
    startNode = None
    endNode = None
    if form.validate_on_submit() :
        startNode = form.startNode.data
        endNode = form.endNode.data
        form.startNode.data = ""
        form.endNode.data = ""

        dist = dijk.dijkstra(startNode)
        dijkText = dijk.printDijkstra(dist, startNode, endNode)
        
        model = {   
                    "startNode": startNode, 
                    "endNode": endNode,
                    "dist": dist,
                    "dijkText": dijkText
                }

        json.dump(model, open("./Model/model.json", "w"))

    jobj = json.load(open('./Model/model.json', "r"))

    if (jobj == None) :
        flash("Please Input Node")
        return redirect(url_for('index'))  
    else :
        return render_template("dijkstra.html", form = form, nodes = {"startNode":jobj['startNode'], "endNode":jobj['endNode']}, dist = jobj['dist'], distLength = len(jobj['dist']), dijk = jobj['dijkText'])

@app.route("/sendBName", methods = ['GET', 'POST'])
def sendBName():
    form = MyForm()
    if form.validate_on_submit() :
        bName = form.bName.data
        sphero(bName)
    return redirect(url_for('dijkstra'))

if __name__ == "__main__" :
    app.run(debug=True)