from flask import Flask, jsonify, render_template

application = Flask(__name__)

@application.route('/')
def hello():
    return render_template('index.html')

@application.route('/health')
def health():
    return jsonify(status='ok'), 200

if __name__ == '__main__':
    application.run()
