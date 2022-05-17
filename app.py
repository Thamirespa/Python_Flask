from flask import Flask, render_template, request, url_for, redirect, flash, Response, jsonify
from flask_restful import reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object('config_db')
app.config['SECRET_KEY'] = "inmetrics"
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class Clientes(db.Model):
    __tablename__ = "clientes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    nome = db.Column(db.String(100))
    email = db.Column(db.String(100))
    cpf = db.Column(db.String(15))
    telefone = db.Column(db.String(16))
    #endereco = db.relationship('Enderecos', backref='Clientes', lazy=True)
    #endereco = db.Column(db.String(200))
    #def __init__(self, nome, email, cpf, telefone , endereco):
    def __init__(self, nome, email, cpf, telefone):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.telefone = telefone
        #self.endereco = endereco


class Enderecos(db.Model):
    __tablename__ = "endereco"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    rua = db.Column(db.String(100))
    numero = db.Column(db.String(100))
    complemento = db.Column(db.String(200))
    cep = db.Column(db.String(15))
    bairro = db.Column(db.String(100))
    cidade = db.Column(db.String(16))
    estado = db.Column(db.String(200))
    #cliente_id = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    def __init__(self, rua, numero,complemento, cep,bairro, cidade, estado):
        self.rua = rua
        self.numero = numero
        self.complemento = complemento
        self.cep = cep
        self.bairro = bairro
        self.cidade = cidade
        self.estado = estado
        #self.cliente_id = cliente_id


#Construção dos métodos de cliente
@app.route('/clientes')
def lista_clientes():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    todos_clientes = Clientes.query.paginate(page, per_page)
    return render_template("clientes.html", clientes=todos_clientes)

@app.route('/cria_cliente', methods=["GET", "POST"])
def cria_cliente():
    nome = request.form.get('nome')
    email = request.form.get('email')
    cpf = request.form.get('cpf')
    telefone = request.form.get('telefone')


    if request.method == 'POST':
        if not nome or not email or not cpf or not telefone :
            flash("Preencha todos os campos do formulário", "erro")
        else:
            cliente = Clientes(nome, email, cpf, telefone, )
            db.session.add(cliente)
            db.session.commit()
            return redirect(url_for('lista_clientes'))
    return render_template("novo_cliente.html")


@app.route('/<int:id>/atualiza_cliente', methods=["GET", "POST"])
def atualiza_cliente(id):
    cliente = Clientes.query.filter_by(id=id).first()
    if request.method == "POST":
        nome = request.form["nome"]
        email = request.form["email"]
        cpf = request.form["cpf"]
        telefone = request.form["telefone"]


        Clientes.query.filter_by(id=id).update({"nome": nome, "email": email, "cpf": cpf, "telefone": telefone })
        db.session.commit()
        return redirect(url_for('lista_clientes'))
    return render_template("atualiza_cliente.html", cliente=cliente)

@app.route('/<int:id>/remove_cliente')
def remove_cliente(id):
    cliente = Clientes.query.filter_by(id=id).first()
    db.session.delete(cliente)
    db.session.commit()
    return redirect(url_for('lista_clientes'))

#Construção dos métodos de endereço
@app.route('/endereco')
def lista_enderecos():
    page = request.args.get('page', 1, type=int)
    per_page = 10
    todos_enderecos = Enderecos.query.paginate(page, per_page)
    return render_template("enderecos.html", enderecos=todos_enderecos)

@app.route('/cria_endereco', methods=["GET", "POST"])
def cria_endereco():
    rua = request.form.get('rua')
    numero = request.form.get('numero')
    complemento = request.form.get('complemento')
    cep = request.form.get('cep')
    bairro = request.form.get('bairro')
    cidade = request.form.get('cidade')
    estado = request.form.get('estado')


    if request.method == 'POST':
        #if not rua or not numero or not complemento or not cep or not bairro or not cidade or not estado:
            #flash("Preencha todos os campos do formulário", "erro")
        #else:
            endereco = Enderecos(rua, numero,complemento, cep, bairro, cidade, estado)
            db.session.add(endereco)
            db.session.commit()
            return redirect(url_for('lista_enderecos'))
    return render_template("novo_endereco.html")


@app.route('/<int:id>/atualiza_endereço', methods=["GET", "POST"])
def atualiza_endereco(id):
    endereco = Enderecos.query.filter_by(id=id).first()
    if request.method == "POST":

        rua = request.form["rua"]
        numero = request.form["numero"]
        complemento = request.form["complemento"]
        cep = request.form["cep"]
        bairro = request.form["bairro"]
        cidade = request.form["cidade"]
        estado = request.form["estado"]

        Enderecos.query.filter_by(id=id).update({"rua": rua , "numero": numero,"complemento": complemento, "cep": cep, "bairro": bairro, "cidade": cidade, "estado": estado})
        db.session.commit()
        return redirect(url_for('lista_enderecos'))
    return render_template("atualiza_endereco.html", endereco=endereco)

@app.route('/<int:id>/remove_endereco')
def remove_endereco(id):
    endereco = Enderecos.query.filter_by(id=id).first()
    db.session.delete(endereco)
    db.session.commit()
    return redirect(url_for('lista_enderecos'))


if __name__ =="__main__":
	db.create_all()
app.run(debug=True)



