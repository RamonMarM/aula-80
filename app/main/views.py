from flask import render_template, session, redirect, url_for
from . import main
from .. import db
from ..templates.models import User  # Importação ajustada para a nova localização
from .forms import NameForm
from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
        else:
            session['known'] = True
        session['name'] = form.name.data
        return redirect(url_for('.index'))
    usuarios = User.query.all()
    return render_template('index.html', form=form, name=session.get('name'),
                           known=session.get('known', False), usuarios=usuarios)
