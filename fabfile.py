from fabric.api import local

def init_db():
    local('python manage.py syncdb')
    local('python manage.py migrate')
    local('python manage.py schemamigration hospital --init')
    local('python manage.py migrate')

def migrate_1():
    # python manage.py schemamigration hospital --auto
    local('python manage.py schemamigration hospital --auto')

def migrate_2():
    # python manage.py migrate myapp
    local('python manage.py migrate hospital')

def runserver():
    local('python manage.py runserver')

def erd():
    # python manage.py graph_models -a -o myapp_models.png
    local('python manage.py graph_models -a -e -g -o erd.png')
    # local('python manage.py graph_models -o erd.png hospital')