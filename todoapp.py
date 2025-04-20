from flask import Flask, render_template, request, redirect
import re

app = Flask(__name__)

todo_list = []

VALID_PRIORITIES = ['Low', 'Medium', 'High']

@app.route('/')
def index():
    return render_template('index.html', todo_list=todo_list)

@app.route('/submit', methods=['POST'])
def submit():
    task = request.form.get('task', '').strip()
    email = request.form.get('email', '').strip()
    priority = request.form.get('priority', '')


    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return redirect('/')


    if priority not in VALID_PRIORITIES:
        return redirect('/')


    todo_list.append({
        'task': task,
        'email': email,
        'priority': priority
    })

    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    todo_list.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
