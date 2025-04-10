from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models import Product, db

product_bp = Blueprint('product', __name__, url_prefix='/estoque')

@product_bp.route('/')
@login_required
def estoque():
    produtos = Product.query.order_by(Product.name).all()
    return render_template('estoque.html', produtos=produtos)

@product_bp.route('/novo', methods=['GET', 'POST'])
@login_required
def novo_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = int(request.form['quantidade'])
        preco = float(request.form['preco'])

        novo = Product(name=nome, quantity=quantidade, unit_price=preco)
        db.session.add(novo)
        db.session.commit()

        flash('Produto cadastrado com sucesso!', 'success')
        return redirect(url_for('product.estoque'))

    return render_template('novo_produto.html')

@product_bp.route('/movimentar/<int:produto_id>', methods=['POST'])
@login_required
def movimentar_produto(produto_id):
    produto = Product.query.get_or_404(produto_id)
    movimento = request.form['movimento']
    quantidade = int(request.form['quantidade'])

    if movimento == 'entrada':
        produto.quantity += quantidade
    elif movimento == 'saida':
        if produto.quantity >= quantidade:
            produto.quantity -= quantidade
        else:
            flash('Quantidade insuficiente no estoque.', 'danger')
            return redirect(url_for('product.estoque'))

    db.session.commit()
    flash('Movimentação realizada com sucesso.', 'success')
    return redirect(url_for('product.estoque'))

@product_bp.route('/deletar/<int:produto_id>', methods=['POST'])
@login_required
def deletar_produto(produto_id):
    produto = Product.query.get_or_404(produto_id)
    db.session.delete(produto)
    db.session.commit()
    flash('Produto excluído com sucesso.', 'success')
    return redirect(url_for('product.estoque'))
