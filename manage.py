from app import create_app, db
import unittest
from app.models import User
from flask_script import Manage, Server


app = create_app('development')

manager = manager(app)
manager.add_command('server', Server)


def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)



@manager.shell
def make_shell_context():
    return dict(app = app, db = db, User = User)


if __name__ == '__main__':
    manager.run()