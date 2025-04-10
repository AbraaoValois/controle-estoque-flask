from flask import Blueprint, render_template, redirect, url_for, request, flash
from ..models import db, Client, Purchase
from flask_login import login_required
from datetime import datetime

client_bp = Blueprint('client', __name__)

# Rota para listar todos os clientes
@client_bp.route('/clients')
@login_required
def clients():
    all_clients = Client.query.all()
    return render_template('clients.html', clients=all_clients)

# Rota para cadastrar um novo cliente
@client_bp.route('/clients/new', methods=['GET', 'POST'])
@login_required
def new_client():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        client = Client(name=name, phone=phone)
        db.session.add(client)
        db.session.commit()
        return redirect(url_for('client.clients'))
    return render_template('new_client.html')

# Rota para adicionar uma nova compra fiada a um cliente
@client_bp.route('/clients/<int:client_id>/add_purchase', methods=['GET', 'POST'])
@login_required
def add_purchase(client_id):
    client = Client.query.get_or_404(client_id)

    if request.method == 'POST':
        value = float(request.form['value'])
        description = request.form['description']
        purchase = Purchase(value=value, description=description, client=client)
        db.session.add(purchase)
        db.session.commit()
        flash('Compra adicionada com sucesso!')
        return redirect(url_for('client.client_detail', client_id=client.id))

    return render_template('add_purchase.html', client=client)

# Rota para exibir detalhes de um cliente e suas compras
@client_bp.route('/clients/<int:client_id>')
@login_required
def client_detail(client_id):
    client = Client.query.get_or_404(client_id)
    return render_template('client_detail.html', client=client)

# Rota para marcar uma compra como paga
@client_bp.route('/purchase/<int:purchase_id>/pay')
@login_required
def pay_purchase(purchase_id):
    purchase = Purchase.query.get_or_404(purchase_id)
    purchase.is_paid = True
    db.session.commit()
    flash('Compra marcada como paga.')
    return redirect(url_for('client.client_detail', client_id=purchase.client_id))

# Rota para ver relatório de fiado
@client_bp.route('/relatorio/fiado')
@login_required
def fiado_report():
    fiados = Purchase.query.filter_by(is_paid=False).all()
    return render_template('fiado_report.html', fiados=fiados)

# Rota para excluir um cliente
@client_bp.route('/clients/<int:client_id>/delete', methods=['POST'])
@login_required
def delete_client(client_id):
    client = Client.query.get_or_404(client_id)

    # Remove as compras antes (se não houver cascade no model)
    for purchase in client.purchases:
        db.session.delete(purchase)

    db.session.delete(client)
    db.session.commit()
    flash('Cliente excluído com sucesso!')
    return redirect(url_for('client.clients'))


# Rota para visualizar o relatório diário de compras
@client_bp.route('/relatorio/diario', methods=['GET'])
@login_required
def daily_report():
    selected_date_str = request.args.get('date')
    selected_date = None
    purchases = []

    if selected_date_str:
        try:
            selected_date = datetime.strptime(selected_date_str, "%Y-%m-%d").date()
            purchases = Purchase.query.filter(Purchase.data == selected_date).all()
        except ValueError:
            flash("Data inválida. Use o formato correto YYYY-MM-DD.", "danger")

    return render_template('relatorio_diario.html', purchases=purchases, selected_date=selected_date_str)

