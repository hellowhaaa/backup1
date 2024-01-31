from flask import Flask, request, render_template

app = Flask(__name__)

app.secret_key = 'sdfjiohdgssdkghnlsdhs'

@app.route('/da', methods=['GET'])
def after():
    name = request.values.get('name')
    # name = request.args.get('name')
    # 都可以
    
    #  ? 後面的部分，包含以 key=value 形式
    return render_template('after_test.html', name= name)


@app.route('/da2',methods = ['GET','POST'])
def after2():
    if request.method == 'POST':
        if request.values['send'] =='submit':
        # 表特定送出鍵 <input type="submit" name="send" value="送出">所在html寫這這樣, 擔心有兩個 button
    #    request.form['nm'] == 求的是送出的值
    
            # user = request.form['user']
            # user = request.form.get('user')
            user = request.values.get('user')
            
            return render_template('after_test.html', user=user)
    return render_template('after_test.html')
if __name__=='__main__':
    app.run(debug=True,port=1500)
    