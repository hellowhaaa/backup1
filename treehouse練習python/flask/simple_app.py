from flask import Flask, render_template, url_for

#  in order to have use's request object

app = Flask(__name__)
# namespace -> always refer to yourself


@app.route('/')  # take this index() into app decorator
@app.route('/<name>')
def index(name='Treehouse'):
    # args holds the all arguments in request
    # 使用 get method
    return "Hello from {} ".format(name)


@app.route('/add/<int:num1>/<int:num2>')# These are sting by default
def add(num1, num2):
    return render_template("add.html", num1=num1, num2=num2)


if __name__ == '__main__':
    app.run(debug=True)
#   因為有 debug = True 所以讓 reload changes
# host -> listen to all addresses that can get to here