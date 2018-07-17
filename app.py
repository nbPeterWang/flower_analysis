from flask import Flask
from flask import request
from pre import p

app = Flask(__name__)
app.config['SERVER_NAME'] = 'www.ml.com:5000' #设置域名
@app.route('/', methods=['GET'])
def home():
    return '''<form action="/" method="post">
              <p><input name="sepal length" >花蕊长度</p>
              <p><input name="sepal width" >花蕊宽度</p>
              <p><input name="pepal length" >花瓣长度</p>
              <p><input name="pepal width" >花瓣宽度</p>
              <p><button type="submit">预测</button></p>
              </form>'''

#点击按钮后的事件
@app.route('/', methods=['POST'])
def predict():
    sl=request.form['sepal length']
    sw=request.form['sepal width']
    pl=request.form['pepal length']
    pw=request.form['pepal width']
    
    return '''<form action="/" method="post">
              <p><input name="sepal length" >花蕊长度</p>
              <p><input name="sepal width" >花蕊宽度</p>
              <p><input name="pepal length" >花瓣长度</p>
              <p><input name="pepal width" >花瓣宽度</p>
              <p><button type="submit">预测</button></p>

              </form>
              <h3>%s</h3>'''%(p.pred(sl,sw,pl,pw))
           
    

if __name__ == '__main__':
    
    app.run()