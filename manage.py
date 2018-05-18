from app import create_app, db
from flask_script import Manager,Server
from flask_migrate import Migrate, MigrateCommand

# instances for the create_app
app = create_app('development')

manager = Manager(app)
manager.add_command('server',Server,port=4200)

# migrate = Migrate(app)
# manager.add_command('db',MigrateCommand)

if __name__=='__main__':
    manager.run()
