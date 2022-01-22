# importing celery app in init ensures that celery loads when django starts
# shared_task will always use this app
from .celery import app as celery_app
__all__ = ('celery_app')