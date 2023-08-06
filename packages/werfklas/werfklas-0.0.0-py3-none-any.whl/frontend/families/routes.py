from flask import render_template, Blueprint, request, flash
from sqlalchemy.orm import Query

from src.classes.base import RearrangeDate
from src.classes.family import AddFamily, EditFamily, find_children
from src.classes.database import Child, Family, sessionSetup
from src.modules.common import stringdate

session = sessionSetup()
rearrange_date = RearrangeDate()


# Blueprint Configuration
families_bp = Blueprint(
    'families_bp', __name__,
    template_folder='templates'
)


@families_bp.route('/index_families')
def index_families():
    # get a list of unique values in the style column
    _families_from_database = Query([
        Family.id,
        Family.lastname,
        Family.parent1,
        Family.parent2,
        Family.parent2_lastname,
        Family.divorced
    ]).with_session(session).order_by(
        Family.lastname.asc(),
    )
    _families = []
    for _family in _families_from_database:
        _families.append({
            'id': _family[0],
            'lastname': _family[1],
            'parent1': _family[2],
            'parent2': _family[3],
            'parent2_lastname': _family[4],
            'children': _family[5]
        })
    return render_template('index_families.html',
                           Families=_families,
                           _PageTitle='Familie Overzicht')


@families_bp.route('/details_family/<fid>')
def details_family(fid):
    try:
        _family_from_database = Query([
            Family.lastname,
            Family.parent1,
            Family.parent2,
            Family.parent2_lastname,
            Family.divorced,
            Family.id,
        ]).filter_by(id=fid).with_session(session)
        _family = []
        for _f in _family_from_database:
            _family.append({
                'lastname': _f[0],
                'parent1': _f[1],
                'parent2': _f[2],
                'parent2_lastname': _f[3],
                'children': find_children(fid),
                'id': _f[5]
            })
        return render_template('details_family.html',
                               Family=_family,
                               _PageTitle='Gezins details')
    except Exception as e:
        # e holds description of the error
        error_text = "<p>The error:<br>" + str(e) + "</p>"
        hed = '<h1>Something is broken.</h1>'
        return hed + error_text


@families_bp.route('/edit_family/<fid>')
def edit_family(fid):
    _family_from_database = Query([
        Family.parent1,
        Family.parent2,
        Family.parent2_lastname,
        Family.lastname,
        Family.id,
        Family.divorced
    ]).with_session(session).filter(Family.id == fid).first()
    # two forms in this template
    _familyToEdit = {'lastname': _family_from_database.lastname,
                     'parent1': _family_from_database.parent1,
                     'parent2': _family_from_database.parent2,
                     'parent2_lastname': _family_from_database.parent2_lastname,
                     'id': _family_from_database.id,
                     'divorced': _family_from_database.divorced}
    return render_template('edit_family.html',
                           familyToEdit=_familyToEdit,
                           form1=EditFamily(),
                           _PageTitle='Gezin wijzigen')


@families_bp.route('/add_family', methods=['GET', 'POST'])
def add_family():
    _form1 = AddFamily()
    if _form1.validate_on_submit():
        id_field = request.form['id_field']
        lastname = request.form['lastname']
        parent1 = request.form['parent1']
        parent2 = request.form['parent2']
        parent2_lastname = request.form['parent2_lastname']
        divorced = request.form['divorced']
        # the data to be inserted into Sock model - the table, socks
        record = Family(id_field, lastname, parent1, parent2, parent2_lastname, divorced)
        # Flask-SQLAlchemy magic adds record to database
        session.add(record)
        session.commit()
        # create a message to send to the template
        _message = f"Gezin {lastname} is aangemaakt."
        return render_template('add_family.html',
                               message=_message,
                               _PageTitle='Gezin toevoegen')
    else:
        # show validaton errors
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('add_family.html',
                               form1=_form1,
                               _PageTitle='Gezin toevoegen')



@families_bp.route('/remove_family/<fid>')
def remove_family(fid):
    _child_to_delete = Query(Child).with_session(session).filter(Child.parents == fid).delete()
    _family_to_delete = Query(Family).with_session(session).filter(Family.id == fid).delete()
    session.commit()
    message = f"De gegevens zijn verwijderd."
    return render_template('remove_family_result.html',
                           message=message,
                           _PageTitle='Gezin verwijderen')


@families_bp.route('/edit_family_result', methods=['POST'])
def edit_family_result():
    fid = request.form['id_field']
    _familyToEdit = {"id": fid,
                    "lastname": request.form['lastname'],
                    "parent1": request.form['parent1'],
                    "parent2": request.form['parent2'],
                    "parent2_lastname": request.form['parent2_lastname'],
                    "updated": stringdate()}
    _form1 = EditFamily()
    if _form1.validate_on_submit():
        lastname = _form1.lastname.data
        parent1 = _form1.parent1.data
        parent2 = _form1.parent2.data
        parent2_lastname = _form1.parent2_lastname.data
        _family_to_edit = Query(Family).with_session(session).filter(Family.id == fid).update(dict(
            lastname=lastname,
            parent1=parent1,
            parent2=parent2,
            parent2_lastname=parent2_lastname))
        session.commit()
        print(_familyToEdit)
        message = f"De gegevens voor {_familyToEdit['lastname']} zijn bijgewerkt."
        return render_template('result.html',
                               message=message,
                               redirect=f'details_family/{fid}',
                               _PageTitle='Resultaat')
    else:
        # show validaton errors
        _familyToEdit["id"] = fid
        # see https://pythonprogramming.net/flash-flask-tutorial/
        for field, errors in _form1.errors.items():
            for error in errors:
                flash("Error in {}: {}".format(
                    getattr(_form1, field).label.text,
                    error
                ), 'error')
        return render_template('edit_family.html',
                               form1=_form1,
                               familyToEdit=_familyToEdit,
                               redirect=f'details_family/{fid}',
                               choice='edit',
                               _PageTitle='Resultaat')
