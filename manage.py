from app import create_app
import unittest
from flask_script import Manage, Server


app = create_app('development')

manager = manager(app)
manager.add_command('server', Server)


def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

    
if __name__ == '__main__':
    manager.run()