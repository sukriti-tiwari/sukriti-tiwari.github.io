from flask import Flask, render_template, flash, request

app = Flask(__name__, template_folder='templates', static_folder='static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/artclass')
def artclass():
    return render_template('artclass.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/products')
def product():
    return render_template('products.html')


@app.route('/contact', methods= ['GET', 'POST'])
def contact():
        return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
