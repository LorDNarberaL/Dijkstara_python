from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import SubmitField, TelField
from Controllers.Dijkstra import Dijkstra
from Controllers.Sphero import *
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'
dijk = Dijkstra()

class MyForm(FlaskForm):
    startNode = TelField("Input Start Node")
    endNode = TelField("Input End Node")
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
    startNode = ""
    endNode = ""
    if form.validate_on_submit() :
        startNode = form.startNode.data
        endNode = form.endNode.data
        form.startNode.data = ""
        form.endNode.data = ""

        vList = dijk.getterVList()
        iStart = 0
        for iStart in range(len(vList)) :
            if startNode.lower() == vList[iStart].lower() :
                break
        
        iEnd = 0
        for iEnd in range(len(vList)) :
            if endNode.lower() == vList[iEnd].lower() :
                break
        
        dist = dijk.dijkstra(iStart)
        dijkText = dijk.printDijkstra(dist, iStart, iEnd)
        
        model = {   
                    "startNode": startNode, 
                    "endNode": endNode,
                    "dist": dist,
                    "dijkText": dijkText,
                    "vList": vList,
                    "iStart": iStart,
                    "iEnd": iEnd
                }

        json.dump(model, open("./Model/model.json", "w"))

    jobj = json.load(open('./Model/model.json', "r"))

    if (jobj == None) :
        flash("Please Input Node")
        return redirect(url_for('index'))  
    else :
        return render_template("dijkstra.html", form = form, nodes = {"start":jobj['startNode'], "endNode":jobj['endNode']}, dist = jobj['dist'], distLength = len(jobj['dist']), dijk = jobj['dijkText'], vList = jobj["vList"], iStart = jobj['iStart'])

@app.route("/sendBName", methods = ['GET', 'POST'])
def sendBName():
    form = MyForm()
    if form.validate_on_submit() :
        bName = form.bName.data
        sphero(bName)
    return redirect(url_for('dijkstra'))

if __name__ == "__main__" :
    app.run(debug=True)