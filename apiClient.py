from flask import Flask, redirect, render_template, request, make_response

app = Flask(__name__,
            static_folder='/home/kill/Desktop/Scripts/xssAttack/',
            static_url_path='')

users = [
    'Usuario Default'       
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/mesalvar' , methods=['POST', 'GET'])
def novoUsuario():
    if request.method == 'POST':
        usuario = request.form['nome']
        users.append('\n') 
        users.append(usuario) 
        
        biscoito = request.form['biscoito'] 
        resp = make_response(redirect("/"))
        resp.set_cookie('Cookie', biscoito)
        
    return resp
        

@app.route('/usuarios.html', methods=['GET', 'POST'])

@app.route('/memostre' , methods=['GET'])
def mostrarUsuario():
    for usuarios in users:
        yield(usuarios)             

if __name__ == '__main__':
    app.run(host="192.168.1.13" , debug=True)

