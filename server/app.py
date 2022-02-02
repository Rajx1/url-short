from flask import Flask, jsonify, request, redirect, abort
from flask_cors import CORS
from controllers import urls
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200


@app.route('/all')
def index():
    res, code = urls.get_all()
    return jsonify(res), code

@app.route('/<url>')
def url(url):
    redirect_path = urls.find_by_short_url(url)
    return redirect(redirect_path)

@app.route('/create/<url>', methods=['POST'])
def create(url):
    res, code = urls.create_short_url(url)
    return jsonify(res), code


@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us - {err}"}, 500

if __name__ == "__main__":
    app.run(debug=True)
