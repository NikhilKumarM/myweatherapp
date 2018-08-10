from flask import Flask, redirect, url_for, render_template, session, request, jsonify, json

app = Flask(__name__, template_folder='./views')


@app.route('/create_alert')
def start():
    """
    This is the short description of the
    Args:
        arg1:
        arg2:
        arg3:

    Returns:

    """
    return render_template('create_alert.html',
                           name='Nikhil',
                           image_url="https://lh4.googleusercontent.com/-g0zxj7crYds/AAAAAAAAAAI/AAAAAAAAAAA/AAnn"
                                     "Y7rwKx350ZsmgPOcLreV2QZ_YqiRqw/s96-c/photo.jpg")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET','POST'])
def login_page():
    if request.method == 'GET':
        return render_template('index.html')
    data = request.get_json()
    print(data)
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, Nikhil!</h1>
    </body>
</html>'''


@app.route('/get_post_json', methods=['GET','POST'])
def get_post_json():
    if request.method == 'GET':
        return render_template('create_alert.html',name=session['name'],image_url=session['image_url'])
    data = request.get_json()
    session['name'] = data['name']
    session['image_url'] = data['image_url']
    return "success"
    #return jsonify(status="success", data=data)


if __name__ == '__main__':
    print("Hello Programmer")
    app.secret_key = 'super secret key'
    app.run()

