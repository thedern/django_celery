from celery import Celery
# this module can be imported into other apps
# create celery instance

# to setup the db:  from shell 'sqlite3 db.sqlite3'
# to see tables:  .tables
# must install sqlalchemy fpr celery to use db backend, just pip install, no configuration needed
# start worker: celery -A proj worker -l INFO

app = Celery('celery',
             broker='pyamqp://guest@localhost',
             backend='db+sqlite:///db.sqlite3',
             include=['proj.tasks'])

if __name__ == '__manin__':
    app.start()
