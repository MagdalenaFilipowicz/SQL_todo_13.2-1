from flask import Flask
from flask import request, render_template, redirect, url_for
from forms import TodoForm
from models import todossqlite
import os

app = Flask(__name__)
app.config["SECRET_KEY"] = os.urandom(24)

@app.route("/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm() 
    tasks = todossqlite.show()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit(): 
            todossqlite.create()
            task_id = todossqlite.add_task(form.data)
            return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form, tasks=tasks, error=error)


@app.route("/<int:todo_id>/", methods=["GET", "POST"])
def todo_details(todo_id):
    todo = todossqlite.get(todo_id)
    data_todo = {}
    data_todo['title'] = todo[0][1]
    data_todo['description'] = todo[0][2]
    data_todo['status'] = todo[0][3]
    form_todo = TodoForm(data=data_todo)
   
    if request.method == "POST":
        if request.form["btn"] == "Save":
            todossqlite.update(todo_id=todo_id, data=form_todo.data)
        if request.form["btn"] == "Delete":
            todossqlite.delete(todo_id)
        return redirect(url_for("todos_list"))

    return render_template("todo.html", form=form_todo, todo_id=todo_id)


if __name__ == "__main__":
    app.run(debug=True)