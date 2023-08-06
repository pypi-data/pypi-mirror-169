# -*- coding: utf-8 -*-
from django.urls import re_path, path
from rest_framework import routers

from dvadmin_apscheduler.views.task import TaskViewSet
from dvadmin_apscheduler.views.task_detail import TaskDetailViewSet

system_url = routers.SimpleRouter()
system_url.register(r'task', TaskViewSet)

urlpatterns = [
    path('task/job_list/',TaskViewSet.as_view({'get':'job_list'})),
    path('task/update_status/<str:pk>/',TaskViewSet.as_view({'post':'update_status'})),
    path('task_detail/',TaskDetailViewSet.as_view({'get':'list'})),
]
urlpatterns += system_url.urls
