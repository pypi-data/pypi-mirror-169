from datetime import date

from sqlalchemy.orm import Query

from src.classes.database import Child, sessionSetup, Teacher, Class

session = sessionSetup()


def calculate_age(geboortedatum):
    from datetime import datetime, date

    _date_str = geboortedatum
    _dto = datetime.strptime(_date_str, '%Y-%m-%d').date()
    _today = date.today()
    calculated_age = _today.year - _dto.year - ((_today.month, _today.day) < (_dto.month, _dto.day))
    # self._leeftijd = age
    return calculated_age


def query_class_by_year(child_start_date):
    classes_from_db = Query(Class).with_entities(Class.id, Class.start_date, Class.class_name, Class.teacher, Class.end_date).with_session(session).order_by(Class.start_date.asc())
    classes = []
    for c in classes_from_db:
        if c[1] <= child_start_date <= c[4]:
            _c_teacher = Query(Teacher).with_entities(Teacher.id, Teacher.firstname, Teacher.lastname).with_session(session).filter_by(id=c[3])[0]
            classes.append({
                'class_id': c[0],
                'class_name': f"{c[2]} {c[1][0:4]} - {_c_teacher[1]} {_c_teacher[2]}"
            })
    return classes


def calculate_startyear(date_of_birth):
    from datetime import datetime
    from dateutil.relativedelta import relativedelta

    datetime_object = datetime.strptime(date_of_birth, "%Y-%m-%d").date()
    new_date = datetime_object + relativedelta(years=5)
    return datetime.strftime(new_date, "%m-%Y").replace(' 0', ' ')


def find_class(cid):
    return Query(Class).with_entities(
        Class.class_name,
        Class.teacher,
        Class.start_date,
        Class.end_date,
        Class.id
    ).filter(Class.id == cid).with_session(session)[0]


def find_teacher(tid):
    return Query(Teacher).with_entities(
        Teacher.firstname,
        Teacher.lastname,
        Teacher.id
    ).filter(Teacher.id == tid).with_session(session)[0]


def find_waiting_children():
    _children_from_database = Query(Child).with_entities(
        Child.id,
        Child.firstname,
        Child.lastname,
        Child.date_of_birth,
        Child.date_of_registration,
        Child.class_id
    ).filter(Child.class_id == None).order_by(
        Child.date_of_birth.asc(),
        Child.date_of_registration.asc()
    ).with_session(session).all()

    _w_children = []
    for c in _children_from_database:
        _starts_in_year = calculate_startyear(c[3])
        _w_children.append({
            'id': c[0],
            'firstname': c[1],
            'lastname': c[2],
            'date_of_birth': c[3],
            'class_id': c[4],
            '_starts_in': _starts_in_year
        })
    return _w_children


def stringdate():
    _today = date.today()
    _date_list = str(_today).split('-')
    # build string in format 01-01-2000
    _date_string = _date_list[1] + "-" + _date_list[2] + "-" + _date_list[0]
    return _date_string


def assign_child_to_class():
    pass
#TODO
# vanuit index direct een klas toewijzen, via een popup?