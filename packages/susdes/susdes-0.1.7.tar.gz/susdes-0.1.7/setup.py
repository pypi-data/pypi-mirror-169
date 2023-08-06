from setuptools import setup

version = "0.1.7"

setup(
    name='susdes',
    version=version,
    py_modules=['susdes', 'test_system_wrapper'],
    url="https://github.com/maksloboda/susdes",
    author="Maks Loboda",
    author_email="mloboda@edu.hse.ru",
    install_requires=[
        'click',
        'python-jenkins',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'susdes = susdes:cli',
        ],
    },
)
