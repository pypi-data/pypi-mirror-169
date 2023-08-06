from application import settings

# 注册app
# app = 'django_apscheduler'
# if app not in settings.INSTALLED_APPS:
#     settings.INSTALLED_APPS += [app]

# app = 'plugins.dvadmin_apscheduler_backend'
# if app not in settings.INSTALLED_APPS:
#     settings.INSTALLED_APPS += [app]

# if getattr(settings, 'PLUGINS_LIST', {}).get('dvadmin_tenant_backend', None):
#     settings.SHARED_APPS = [
#                                'django_apscheduler',
#                                'plugins.dvadmin_apscheduler_backend',
#                            ] + list(getattr(settings, 'SHARED_APPS', []))


# ================================================= #
# ***************** 插件配置区开始 *******************
# ================================================= #
# 路由配置
plugins_url_patterns = [
    {"re_path": r'api/dvadmin_apscheduler/', "include": 'dvadmin_apscheduler.urls'}
]
# app配置
apps = ['django_apscheduler', 'dvadmin_apscheduler']
# 租户模式中，public模式共享app配置
tenant_shared_apps = []
# ================================================= #
# ******************* 插件配置区结束 *****************
# ================================================= #

settings.INSTALLED_APPS += [app for app in apps if app not in settings.INSTALLED_APPS]
settings.TENANT_SHARED_APPS += tenant_shared_apps


# ********** 注册路由 **********
settings.PLUGINS_URL_PATTERNS += plugins_url_patterns
