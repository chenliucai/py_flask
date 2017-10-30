#encoding=utf-8
from flask import Flask,render_template,redirect,request,url_for
import  config
app = Flask(__name__)
app.config.from_object(config)


@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login/',methods=['POST','GET'])
def login():
    if(request.method== 'GET'):
        return render_template('login.html')
    else:

        if(request.form.get('name') == '1' and request.form.get('password') == '2'):
            # return render_template('login.html')
            return render_template('loginsusses.html',name=1)
        else:
            # redirect( url_for('login'))
            return '你不好'

@app.route('/regist/')
def regist():
    return render_template('regist.html')
    # return  redirect( url_for('login'))
@app.route('/loginout/')
def loginout():
    return  render_template('login.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0' )
