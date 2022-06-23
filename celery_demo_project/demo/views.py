import http.client
from django.views import View
from celery_tasks.sms.tasks import send
from django import http
from datetime import datetime, timedelta


class TestCeleryView(View):

    @staticmethod
    def get(request):
        # 异步任务
        result = send.delay('18888888888', '123456')
        return http.HttpResponse(
            f"任务ID: {result}"
        )


class TestCeleryView2(View):
    @staticmethod
    def get(request):
        # 定时任务
        p_now_time = datetime.now()
        # 默认uct
        p_uct_time = datetime.utcfromtimestamp(p_now_time.timestamp())
        p_time_delay = timedelta(seconds=20)
        p_task_time = p_uct_time + p_time_delay

        result = send.apply_async(['18888888888', '123456'], eta=p_task_time)

        return http.HttpResponse(
            f"任务ID: {result}"
        )
