# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/8/22 022 19:23
@Remark:
"""
import uuid

from django.db import models
from django_apscheduler.models import DjangoJob

from application import settings
from dvadmin.utils.models import CoreModel


class Task(CoreModel):
    STATUS_LIST = (
        (0,"停用"),
        (1,"启用")
    )
    status = models.IntegerField(default=1,choices=STATUS_LIST,verbose_name="任务状态",help_text="任务状态")
    name = models.CharField(max_length=30,verbose_name="任务名称",help_text="任务名称")
    cron = models.CharField(max_length=255,verbose_name="cron表达式",help_text="cron表达式")
    job_id = models.OneToOneField(DjangoJob,db_constraint=False,on_delete=models.CASCADE,verbose_name="关联DjangoJob",help_text="关联DjangoJob",null=True,blank=True)
    job = models.CharField(max_length=255,verbose_name="执行的任务",help_text="执行的任务")

    class Meta:
        db_table = settings.TABLE_PREFIX + "apscheduler_task"
        verbose_name = '定时任务表'
        verbose_name_plural = verbose_name
        ordering = ('create_datetime',)