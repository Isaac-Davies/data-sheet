from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def render_home_page():  # put application's code here
    return render_template('index.html')

@app.route('/webtags')
def render_webtags_page():  # put application's code here
    return render_template('webtags.html')

@app.route('/styles')
def render_styles_page():  # put application's code here
    return render_template('styles.html')


if __name__ == '__main__':
    app.run()
