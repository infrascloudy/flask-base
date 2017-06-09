from flask import render_template, Blueprint
from app.models import EditableHTML

main_blueprint = Blueprint('main', __name__)


@main_blueprint.route('/')
def index():
    return render_template('main/index.html')


@main_blueprint.route('/about')
def about():
    editable_html_obj = EditableHTML.get_editable_html('about')
    return render_template('main/about.html',
                           editable_html_obj=editable_html_obj)
