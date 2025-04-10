from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from .models import db, Product
from datetime import datetime

product_bp = Blueprint('product', __name__, url_prefix='/estoque')

# Página principal do estoque
@product_bp.route('/')
@login_required
def estoque():
    produtos = Product.query.all()
    return render_template('estoque.html', produtos=produtos)

# Página para adicionar novo produto
@product_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        novo = Product(nome=nome, quantidade=quantidade, preco=preco)
        db.session.add(novo)
        db.session.commit()

        flash('Produto adicionado com sucesso!')
        return redirect(url_for('product.estoque'))

    return render_template('novo_produto.html')

# Atualizar quantidade de produto (entrada/saída)
@product_bp.route('/<int:produto_id>/movimentar', methods=['POST'])
@login_required
def movimentar_produto(produto_id):
    produto = Product.query.get_or_404(produto_id)
    movimento = request.form.get('movimento')  # 'entrada' ou 'saida'
    quantidade = int(request.form['quantidade'])

    if movimento == 'entrada':
        produto.quantidade += quantidade
    elif movimento == 'saida':
        if produto.quantidade >= quantidade:
            produto.quantidade -= quantidade
        else:
            flash('Quantidade insuficiente em estoque.', 'error')
            return redirect(url_for('product.estoque'))

    db.session.commit()
    flash('Movimentação registrada com sucesso!')
    return redirect(url_for('product.estoque'))

# Deletar um produto
@product_bp.route('/<int:produto_id>/deletar', methods=['POST'])
@login_required
def deletar_produto(produto_id):
    produto = Product.query.get_or_404(produto_id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto removido do estoque.')
    return redirect(url_for('product.estoque'))
