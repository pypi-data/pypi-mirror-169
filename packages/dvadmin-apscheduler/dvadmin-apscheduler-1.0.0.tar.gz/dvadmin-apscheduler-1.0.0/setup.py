import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="dvadmin-apscheduler",
    version="1.0.0",
    author="DVAdmin",
    author_email="liqiang@django-vue-admin.com",
    description="适用于 django-vue-admin 的apscheduler同步插件",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/huge-dream/dvadmin-apscheduler",
    packages=setuptools.find_packages(),
    python_requires='>=3.7, <4',
    install_requires=["django-apscheduler>=0.6.2",
                      "django-redis>=5.0.0",],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[
        ('', ['./dvadmin_apscheduler/fixtures/init_menu.json']),
    ],
    packace_data={
        '': ['*.json'],
        'fixtures': ['*.json'],
    },
    include_package_data=True,
)
