from celery import shared_task
from time import sleep
from todo.models import Task


# @shared_task
# def sendEmail():
#     sleep(3)
#     print("tasks deleted")


@shared_task
def deleteTask():
    sleep(5)
    Task.objects.filter(is_done=True).delete()
    print("done tasks deleted successfully")
