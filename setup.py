from setuptools import setup

#http://docs.python.org/2/distutils/setupscript.html

setup(
    name='weixin_pay',
    version='0.0.1',

    author='dev',
    author_email='dev@agutong.com',
    url='http://git.agutong.com:3007/OpenSource/weixin_pay',

    license='LICENSE',
    description='weixin pay',
    long_description=open('README.md').read(),

    packages=[
      'weixin_pay',
    ],

    package_data = {
    },

    data_files=[
    ],

    scripts=[
    ],

    install_requires=[
        "requests",
        "wsgiref",
    ],

    dependency_links=[
    ]
)

