from setuptools import setup, find_packages

setup(
    name='werfklas',
    version='0.0.1',
    packages=['src', 'src.classes', 'src.modules', 'static', 'static.js', 'frontend', 'frontend.children',
              'frontend.children.templates', 'frontend.families', 'frontend.families.templates', 'frontend.teachers',
              'frontend.teachers.templates', 'frontend.classrooms', 'frontend.classrooms.templates', 'werfklas'],
    install_requires=[
                        "chardet==5.0.0",
                        "Click==8.1.3",
                        "dominate==2.7.0",
                        "Flask==2.2.2",
                        "Flask-Bootstrap4==4.0.2",
                        "Flask-SQLAlchemy==2.5.1",
                        "itsdangerous==2.1.2",
                        "Jinja2==3.1.2",
                        "MarkupSafe==2.1.1",
                        "requests==2.28.1",
                        "SQLAlchemy==1.4.41",
                        "urllib3==1.26.12",
                        "visitor==0.1.3",
                        "Werkzeug==2.2.2",
                        "Flask-WTF==1.0.1",
                        "WTForms==2.2.1",
                        "python-dateutil",
                        "flask-assets"
    ],
    url='',
    license='',
    author='Yves van Elk',
    author_email='',
    description=''
)