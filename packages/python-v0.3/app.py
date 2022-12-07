from flask import Flask, redirect, url_for, render_template, request, make_response

app = Flask(__name__)


@app.route('/admin')
def hello_admin():
    return 'Hello admin'


@app.route('/guest/<guest>')
def hello_guest(guest):
    return render_template('hello.html', guest=guest)


@app.route("/user/<name>")
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest=name))


@app.route('/login', methods=['get', 'post'])
def login():
    print('request method', request.method)
    if request.method == 'POST':
        form = request.form
        print('request form', form)
        resp = make_response(render_template(
            'user.html', username=form['username']))
        resp.set_cookie('username',  form['username'])
        return resp
    else:
        print('user cookie', request.cookies)
        username = request.cookies.get('username')

        if not username:
            return redirect(url_for('hello_guest', guest="guest"))
        return render_template('user.html', username=username)


# with app.test_request_context():
#     print(url_for('hello_admin'))
#     print(url_for('hello_guest', guest="xiejun"))

if __name__ == '__main__':
    app.run(debug=True)
