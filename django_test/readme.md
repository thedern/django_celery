### Purpose
have django send tasks to celery for celery to execute asynchronously on django's behalf
- the tasks are executed on a schedule or as resources become available
### Tutorial
https://www.youtube.com/watch?v=fBfzE0yk97k&t=932s

### Order of Operations
Client --> Django --> Messages (tasks) --> Message Broker (RabbitMQ) --> Celery (execution)

### EXECUTION
#### NOTE:  START CELERY WORKER FROM django project dir (celery_test_proj)
#### NOTE:  TO TEST, START PYTHON3 console from project dir (celery_test_proj)
####NOTE:  UNLESS CELERY IS SPECIFICALLY CONFIGURED TO USE BACKEMD, CANNOT CAPTURE RESULT