from setuptools import setup

def readme():
    with open('README.md','r',encoding = 'utf-8') as f:
        README = f.read()
    return README


setup(
    name='xiaoming-weather',
    version='1.0.2',
    description='Xiaoming weather provides personalized weather data strings for chinese user.',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/dangoms/xiaoming-weather',
    author='zhangyadong',
    author_email='zhangyd@live.com',
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    packages=['xiaoming_weather'],
    include_package_data=True,
    install_requires=['requests', 'chinese_calendar', 'lxml'],
    entry_points={
        'console_scripts': [
            'xiaoming-weather=xiaoming_weather.xiaoming:main',
        ]
    },
)
