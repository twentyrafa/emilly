from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # O HTML alterado estará aqui

if __name__ == '__main__':
    app.run(debug=True)
