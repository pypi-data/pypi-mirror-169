# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/8/22 022 10:16
@Remark:
"""
import json
import uuid

from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from dvadmin.utils.json_response import SuccessResponse, ErrorResponse
from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet
from dvadmin_apscheduler.models import Task

scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), 'default')
scheduler.start()

# 删除任务
# scheduler.remove_job(job_name)
# 暂停任务
# scheduler.pause_job(job_name)
# 开启任务
# scheduler.resume_job(job_name)
# 修改任务
# scheduler.modify_job(job_name)

# 获取所有APP下的tasks任务
def get_job_list():
    from application import settings
    tasks_list = []
    tasks_dict_list=[]
    for app in settings.INSTALLED_APPS:
        try:
            exec(f"""
from {app} import tasks
for ele in [i for i in dir(tasks) if not i.startswith('__')]:
    task_dict = dict()
    task_dict['label']="{app}.tasks." + ele
    task_dict['value']="{app}.tasks." + ele
    tasks_list.append("{app}.tasks." + ele)
    tasks_dict_list.append(task_dict)
                            """)
        except ImportError:
            pass
    return {"tasks_list":tasks_list,"tasks_dict_list":tasks_dict_list}


#将cron表达式进行解析
def CronSlpit(cron):
    cron = cron.split(" ")
    result = {
        "second":cron[0],
        "minute":cron[1],
        "hour":cron[2],
        "day":cron[3],
        "month":cron[4],
        "week":cron[5],
        "year":cron[6]
    }
    return result


class TaskSerializer(CustomModelSerializer):
    """定时任务 序列化器"""
    class Meta:
        model = Task
        fields = "__all__"



class TaskViewSet(CustomModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_fields = ['job']

    def job_list(self,request,*args, **kwargs):
        """获取所有任务的路径"""
        result = get_job_list()
        tasks_list = result.get('tasks_dict_list')
        return SuccessResponse(msg="获取成功", data=tasks_list,total=len(tasks_list))

    def create(self, request, *args, **kwargs):
        body_data = request.data
        # {'name': '2222', 'cron': '0/1 0/1 0/1 1/1 1/1 1/1 2022/1', 'job': 'dvadmin_apscheduler.tasks.task2', 'description': '2222'}
        cron = body_data.get('cron')
        cron_lisr = CronSlpit(cron)
        second = cron_lisr["second"]
        minute = cron_lisr["minute"]
        hour = cron_lisr["hour"]
        day = cron_lisr["day"]
        month = cron_lisr["month"]
        week = cron_lisr["week"]
        year = cron_lisr["year"]
        job = body_data.get('job')
        result = None
        tasks_list = get_job_list()
        tasks_list = tasks_list.get('tasks_list')
        if job in tasks_list:
            job_name = job.split('.')[-1]
            path_name = '.'.join(job.split('.')[:-1])
            job_id = uuid.uuid4()
            exec(f"""
from {path_name} import {job_name}
django_job=scheduler.add_job({job_name}, 'cron', id='{job_id}' , second='{second}', minute='{minute}', hour='{hour}', day='{day}', month='{month}', week='{week}', year='{year}')
body_data['job_id'] = django_job.id
serializer = TaskSerializer(data=body_data)
serializer.is_valid(raise_exception=True)
self.perform_create(serializer)
result = serializer.data
            """)
            return SuccessResponse(msg="添加成功", data=result)
        else:
            return ErrorResponse(msg="添加失败,没有该任务", data=None)

    def destroy(self, request, *args, **kwargs):
        """删除定时任务"""
        instance = self.get_object()
        self.perform_destroy(instance)
        job_id = instance.job_id_id
        job = scheduler.pause_job(job_id)
        scheduler.remove_job(job_id)
        return SuccessResponse(data=[], msg="删除成功")

    def update_status(self,request,*args,**kwargs):
        """开始/暂停任务"""
        instance = self.get_object()
        job_id = instance.job_id_id
        body_data = request.data
        status = body_data.get('status')
        if status == 0:
            scheduler.pause_job(job_id)
        else:
            scheduler.resume_job(job_id)
        instance.status = body_data.get('status')
        instance.save()
        return SuccessResponse(msg="修改成功", data=None)