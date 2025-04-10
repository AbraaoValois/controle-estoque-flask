from flask import Blueprint, render_template
from flask_login import login_required, current_user
from .models import Client, Purchase, db
from sqlalchemy import func

main = Blueprint('main', __name__)

@main.route('/')
@login_required
def home():
    total_clients = Client.query.count()
    total_purchases = Purchase.query.count()
    total_fiado = db.session.query(func.sum(Purchase.value)).filter_by(is_paid=False).scalar() or 0.0

    return render_template(
        'home.html',
        total_clients=total_clients,
        total_purchases=total_purchases,
        total_fiado=total_fiado,
        current_user=current_user
    )
