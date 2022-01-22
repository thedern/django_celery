import os

os.chdir(r"/home/thedern/code/python/celery/venv/bin")
activate_cmd = "source activate"
os.system(activate_cmd)

celery_cmd = "celery -A  celery_test_proj worker --loglevel=info"

os.chdir(r"/home/thedern/code/python/celery/django_test")
os.system(celery_cmd)
