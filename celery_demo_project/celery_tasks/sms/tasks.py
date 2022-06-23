from celery_tasks.main import app
import time


@app.task
def send(mobile, code):
    print('调用开始')
    print(mobile)
    print(code)
    time.sleep(5)
    print('调用结束')

    return {'message': 'success'}
