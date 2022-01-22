import os
from celery import Celery


# set env for the Celery app
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_test_proj.settings')

# create celery instance, takes project name as argument
app = Celery('celery_test_proj')

# allows the celery app to use the django settings file,
# keeps all settings centrally located and django-centric
app.config_from_object('django.conf:settings', namespace='CELERY')

# allows to autodiscover tasks in other apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

# NOTE:  START CELERY WORKER FROM django project dir (celery_test_proj)
# NOTE:  TO TEST, START PYTHON3 console from project dir (celery_test_proj)
# NOTE:  UNLESS CELERY IS SPECIFICALLY CONFIGURED TO USE BACKEMD, CANNOT CAPTURE RESULT
