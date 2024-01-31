from flask import Flask, render_template, url_for, redirect, request, make_response, flash
from options import DEFAULTS
import json

app = Flask(__name__)

# When a user makes choices, we create or update their cookie to reflect these changes, and when a user requests our
# site, we check to see whether a cookie exists and read as much of the unspecified information from this as possible.
def get_saved_data():
    # Check if a cookie already exists & retrieve it
    try:
        data = json.loads(request.cookies.get('character'))
    #     json.loads() -> converts/decodes JSON string into Python dictionary
    except TypeError:
        data = {}  # Return empty dictionary if cookie does not exist.
    return data


@app.route('/')
def index():
    data = get_saved_data()
    return render_template('index.html', saves=data)


@app.route('/builder')
def builder():
    return render_template(
            'builder.html',
            saves=get_saved_data(),
            options=DEFAULTS
    )


@app.route('/save', methods=['POST'])
def save():
    response = make_response(redirect(url_for('builder')))
    # 此function 將發送回客戶端的整個 response object，會將其儲存在變數中以進行進一步操作。
    # 我們的Jinja templates將被渲染，所有佔位符將被替換為正確的值，但我們不會將此回應直接傳回給我們的用戶，
    # 而是將其載入到一個變數中，以便我們可以對其進行更多添加。
    data = get_saved_data()
    data.update(dict(request.form.items()))  # update data if anything is changed, send back
    # get all of the key & value pairs from the form
    # set cookies, call cookie character
    response.set_cookie('character', json.dumps(dict(data)))
    # json.dumps()-> This method turns a Python data structure (list, string, dictionary) into a JSON string.(key,value)
    # The request.form object is an immutable dictionary.
    # response.set_cookie(): Sets a cookie on the response object. Takes name for the cookie and a value.
    return response


if __name__ == "__main__":
    app.run(debug=True)
