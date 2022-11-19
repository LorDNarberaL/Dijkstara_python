from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from controllers import Dijkstra
from controllers import Graph

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mykey'

class MyForm(FlaskForm):
    startNode = IntegerField("Input Start Node")
    endNode = IntegerField("Input End Node")
    submit = SubmitField("Submit")

@app.route("/")
def index():
    form = MyForm()
    return render_template("index.html", form = form)

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
    
    if (startNode == None or endNode == None) :
        flash("Please Input Node")
        return redirect(url_for('index'))  
    else :
        return render_template("dijkstra.html", data = {"startNode":startNode, "endNode":endNode})

if __name__ == "__main__" :
    app.run(debug=True)