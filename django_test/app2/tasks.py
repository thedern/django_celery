
# import the email configuration and have task send it, will log to stdout
# celery.decorators will be avaliavle at runtime
from celery.decorators import task
from celery.utils.log import get_task_logger
from .email import send_review_email


logger = get_task_logger(__name__)


# task to send the email to the message broker, then execute via celery
@task(name="send_review_email_task")
def send_review_email_task(name, email, review):
    # log to screen
    logger.info("Sent Review Email")
    # email function from email.py, task will execute this function when message broker relays msg
    return send_review_email(name, email, review)
