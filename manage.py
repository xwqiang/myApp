import os
import subprocess

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Shell

from app import create_app, db

app = create_app(os.getenv('ENV_NAME') or 'default')

manager = Manager(app)

migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


#python3 manage.py hello --name xwq
@manager.option('-n', '--name', dest='name')
def hello(name):
    print('hello ', name)


@manager.command
def test():
    """run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.command
def format():
    """Runs the yapf and isort formatters over the project."""
    isort = 'isort -rc *.py .'
    yapf = 'yapf -r -i *.py .'

    print('Running {}'.format(isort))
    subprocess.call(isort, shell=True)

    print('Running {}'.format(yapf))
    subprocess.call(yapf, shell=True)


if __name__ == '__main__':
    manager.run()
