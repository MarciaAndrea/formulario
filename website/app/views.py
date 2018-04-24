from flask import render_template, url_for, redirect, request
from app import app
from app.models import Prod, Categ, Estoq

usuario_logado = False

categs= [
    Categ(1, 'Ervas medicinais'),
    Categ(2, 'Especiarias e temperos'),
    Categ(3, 'Grãos e sementes'),
    Categ(4, 'Frutas Cristalizadas'),
    Categ(5, 'Cereais'),
    Categ(6, 'Castanhas'),
    Categ(7, 'Méis'),
    Categ(8, 'azeites e óleos')
]
prods=[

    Prod(1,'Mel de Caju', 15.50, '2018-04-25','Mel de Fruta','Disponível', True, 7),
    Prod(2,'Azeite de Oliva', 28.60, '2018-03-28','Extra Virgem', 'Disponível',True, 8),
    Prod(3,'Pêssego', 10.65, '2018-03-18','Em Calda','Disponível',True, 4),
    Prod(4,'Aveia', 6.20, '2018-03-20','Flocos Grossos','Disponível', True, 5),
    Prod(5,'Castanha de Caju', 18.00, '2018-03-25', 'Salgada', 'Disponível',True, 6),
    Prod(6,'Linhaça', 28.00, '2018-03-04', 'Dourada','Indisponível', True, 3),
    Prod(7,'Boldo', 2.85, '2018-03-14','Sachê', 'Indisponível',True, 1),
    Prod(8,'Louro', 3.50, '2018-03-24','Seco', 'Indisponível',True, 2)
]

estoqs=[
    Estoq(1, 15, 1),
    Estoq(2, 10, 2),
    Estoq(3, 12, 3),
    Estoq(4, 20, 5),
    Estoq(5, 10, 4)
]

@app.route('/categorias/inserir', methods=['GET', 'POST'])
def inserir_categorias():
    global categs
    if request.method == 'GET':
        return render_template('inserir_categorias.html',
        categs = categs,
        msg_nome = "Digite a Categoria")
    elif request.method == 'POST':
        nome = request.form.get('tNome')
        if nome.strip() != '':
            last_id = categs[-1].id if len(categs) > 0 else 0
            categs.append(Categ(last_id+1,nome))
        return redirect(url_for('listar_categorias'))



@app.route('/categorias/listar')
def listar_categorias():
    return render_template('listar_categorias.html',
    categs = categs)


@app.route('/categorias/editar/<int:id>', methods=['GET', 'POST'])
def editar_categorias(id):
    if request.method == 'GET':
        for categoria in categs:
            if categoria.id == id:
                return render_template('editar_categorias.html',categoria_selecionada = categoria, categs = categs)
    elif request.method == 'POST':
        novoNome = request.form.get('nome')
        for index in range(len(categs)):
            if categs[index].id == id:
                categs[index].nome = novoNome
                break
        return redirect(url_for('listar_categorias'))

@app.route('/categorias/deletar/<int:id>', methods=['GET'])
def deletar_categoria(id):
    for categoria in categs:
        if categoria.id == id:
            categs.remove(categoria)
            break
    return redirect(url_for('listar_categorias'))


@app.route('/produto/inserir', methods=['GET', 'POST'])
def inserir_produtos():
    global produto_selecionada
    if request.method == 'GET':
        return render_template('inserir_produtos.html',
        categs = categs,
        msg_nome = "Digite o Nome do Produto",
        msg_preco = "Digite o preço",
        msg_data = "dd/mm/aaaa",
        msg_descr = "Descreva o Produto",
        status = " ",
        notifq = " ",
        id_categs_selecionada = 1)
    elif request.method == 'POST':
        nome = request.form.get('tNome')
        preco = request.form.get('tPreco')
        data = request.form.get('tFab')
        descr = request.form.get('tdescr')
        status = request.form.get('tstatus')
        notifq = request.form.get('tnotifq')
        categ = request.form.get('tCategoria')
        if nome.strip() != '' and preco.strip() != '':
            last_id = prods[-1].id if len(prods) > 0 else 0
            prods.append(Prod(last_id+1,nome,preco,data,descr,status,notifq,categ))
        return redirect(url_for('listar_produtos'))


@app.route('/produto/listar')
def listar_produtos():
    return render_template('listar_produtos.html',
    prod = prods
    )

@app.route('/produto/editar/<int:id>', methods=['GET', 'POST'])
def editar_produtos(id):
    if request.method == 'GET':
        for prod in prods:
            if prod.id == id:
                return render_template('editar_produtos.html',prod_selecionado = prod)
    elif request.method == 'POST':
        nome = request.form.get('tNome')
        preco = request.form.get('tPreco')
        data = request.form.get('tFab')
        categ = request.form.get('tCategoria')
        descr = request.form.get('tdescr')
        status = request.form.get('tstatus')
        notifq = request.form.get('tnotifq')
        for index in range(len(prods)):
            if prods[index].id == id:
                prods[index].nome = nome
                prods[index].preco = preco
                prods[index].data = data
                prods[index].id_categ = categ
                prods[index].descr = descr
                prods[index].status = status
                prods[index].notifq = notifq
                break
        return redirect(url_for('listar_produtos'))


@app.route('/produtos/deletar/<int:id>', methods=['GET'])
def deletar_produtos(id):
    for produto in prods:
        if produto.id == id:
            prods.remove(produto)
            break
    return redirect(url_for('listar_produtos'))

@app.route('/estoque/inserir', methods=['GET', 'POST'])
def inserir_estoques():
    global estoqs
    aux = 1
    if request.method == 'GET':
        return render_template('inserir_estoques.html',
        prods = prods,
        msg_qtde = "Quantidade do estoque")
    elif request.method == 'POST':
        qtde = request.form.get('tQuantidade')
        id_prod = request.form.get('tProd')
        #Adicionar na quantidade do estoque
        for index in range(len(estoqs)):
            if estoqs[index].id_prod == int(id_prod):
                estoqs[index].qtde = estoqs[index].qtde + int(qtde)
                aux = 0
                break
        #Cadastrar novo Estoque na lista
        if qtde.strip() != '' and aux == 1:
            last_id = estoqs[-1].id if len(prods) > 0 else 0
            estoqs.append(Estoq(last_id+1,iint(qtde),id_prod))
        return redirect(url_for('listar_estoques'))

@app.route('/estoques/listar')
def listar_estoques():
    return render_template('listar_estoques.html',
    estoqs = estoqs)

@app.route('/estoques/editar/<int:id>', methods=['GET', 'POST'])
def editar_estoques(id):
    if request.method == 'GET':
        for estoque in estoqs:
            if estoque.id == id:
                return render_template('editar_estoques.html',estoque_selecionada = estoque, estoqs = estoqs)
    elif request.method == 'POST':
        qtde = request.form.get('tQuantidade')
        for index in range(len(estoqs)):
            if estoqs[index].id == id:
                estoqs[index].qtde = qtde
                break
        return redirect(url_for('listar_estoques'))

@app.route('/estoques/deletar/<int:id>', methods=['GET'])
def deletar_estoque(id):
    for estoque in estoqs:
        if estoque.id == id:
            estoqs.remove(estoque)
            break
    return redirect(url_for('listar_estoques'))

@app.route('/')
def home():
    return render_template('index.html', list_categs = categs)
    return redirect(url_for('home'))
