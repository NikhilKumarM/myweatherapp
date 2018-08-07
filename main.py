from flask import Flask, redirect, url_for, render_template, session, request, jsonify

app = Flask(__name__, template_folder='./views')


@app.route('/create_alert')
def start():
    return render_template('create_alert.html', name='Nikhil',image_url='https://lh4.googleusercontent.com/-g0zxj7crYds/AAAAAAAAAAI/AAAAAAAAAAA/AAnnY7rwKx350ZsmgPOcLreV2QZ_YqiRqw/s96-c/photo.jpg')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/_get_post_json/', methods=['POST'])
def get_post_json():
    data = request.get_json()
    d = dict(data)
    #print(d['name'],d['id'])
    print(type(data))
    print(jsonify(status="success", data=data))
    return jsonify(status="success", data=data)


if __name__ == '__main__':
    print("Hello Programmer")
    app.run()

