from celery import Celery
import os

# 读取Django的配置
# os.environ["DJANGO_SETTINGS_MODULE"] = "celery_demo_project.settings"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "celery_demo_project.settings")

# 通过app对象加载配置
app = Celery("CeleryDemo")

# 通过app加载配置
app.config_from_object('celery_tasks.config')

# 加载可用的任务
app.autodiscover_tasks([
    'celery_tasks.sms',
])
