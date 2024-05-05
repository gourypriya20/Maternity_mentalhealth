from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['POST','GET'])
@app.route('/main', methods=['POST','GET'])
def service():
    return render_template('main.html')

@app.route('/shop', methods=['POST','GET'])
def shop_menu():
    return render_template('shop.html')

@app.route('/articles', methods=['POST','GET'])
def display_menu():
    return render_template('articles.html')

@app.route('/article_1st', methods=['POST','GET'])
def display_1st_article():
    return render_template('article_1st.html')

@app.route('/article_2nd', methods=['POST','GET'])
def display_2nd_article():
    return render_template('article_2nd.html')

@app.route('/custom', methods=['POST','GET'])
def display_custom_menu():
    return render_template('custom.html')

@app.route('/pre', methods=['POST','GET'])
def prenatal():
    return render_template('pre.html')

@app.route('/post', methods=['POST','GET'])
def postpartum():
    return render_template('post.html')