from flask import Flask, jsonify, request, render_template, redirect, abort
from flask_cors import CORS
from controllers import cats
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hello from Flask!'}), 200

@app.route('/index')
def index():
    return index_with('unkown')

@app.route('/index/<name>')
def index_with(name):
    return render_template('index.html', title='Welcome', username=name)

@app.route('/bounce/<url>')
def bounce(url):
    if url == 'beeb':
        return redirect('https://bbc.co.uk')
    else:
        abort(404)


@app.route('/api/cats', methods=['GET', 'POST'])
def cats_handler():
    fns = {
        'GET': cats.index,
        'POST': cats.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/api/cats/<cat_name>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def cat_handler(cat_name):
    fns = {
        'GET': cats.show,
        'PATCH': cats.update,
        'PUT': cats.update,
        'DELETE': cats.destroy
    }
    resp, code = fns[request.method](request, cat_name)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Oops! {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Oops! {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"It's not you, it's us"}, 500

if __name__ == "__main__":
    app.run(debug=True)
