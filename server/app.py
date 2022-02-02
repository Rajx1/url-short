from flask import Flask, jsonify, request, redirect
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
def bounce(url):
    redirect_path = urls.find_by_short_url(url)
    return redirect(redirect_path)

@app.route('/create', methods=['POST'])
def create():
    res, code = urls.create_short_url(request.get_json())
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
