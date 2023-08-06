# -*- coding: utf-8 -*-

"""
@author: 猿小天
@contact: QQ:1638245306
@Created on: 2021/8/23 023 21:56
@Remark:
"""
import time

from django_apscheduler.models import DjangoJobExecution
from rest_framework import serializers

from dvadmin.utils.serializers import CustomModelSerializer
from dvadmin.utils.viewset import CustomModelViewSet
import django_filters

class  TaskDetailSerializer(CustomModelSerializer):
    """定时任务详情 序列化器"""
    finished = serializers.SerializerMethodField()

    def get_finished(self, instance):
        local = time.localtime(instance.finished)
        local = time.strftime("%Y-%m-%d %H:%M:%S", local)
        return local

    class Meta:
        model = DjangoJobExecution
        fields = "__all__"


class TaskDetailFiterSet(django_filters.FilterSet):
    run_time = django_filters.BaseRangeFilter(field_name="run_time")
    duration = django_filters.NumberFilter(field_name="duration")
    class Meta:
        model = DjangoJobExecution
        fields = "__all__"



class TaskDetailViewSet(CustomModelViewSet):
    """
    定时任务
    """
    queryset = DjangoJobExecution.objects.all()
    serializer_class = TaskDetailSerializer
    filter_class = TaskDetailFiterSet
