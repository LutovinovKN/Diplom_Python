from flask import Flask, render_template, request, json


app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/signUp')
def signUp():
    pass
    # create user code will be here !!


@app.route('/signUp',methods=['POST'])
def signUp():
    _name = request.form['inputName']
    _email = request.form['inputEmail']
    _password = request.form['inputPassword']
    
    if _name and _email and _password:
        return json.dumps({'html':'<span>Регистрация прошла успешно</span>'})
    else:
        return json.dumps({'html':'<span>Вы заполнили не все поля</span>'})




if __name__ == "__main__":
    app.run(port=5002)

