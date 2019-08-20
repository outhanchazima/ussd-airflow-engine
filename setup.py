from setuptools import setup, find_packages
from ussd import VERSION


setup(
    name='ussd_airflow',
    version=VERSION,
    packages=find_packages(exclude=('ussd_airflow',)),
    url='https://github.com/mwaaas/ussd_airflow',
    install_requires=[
        'Django>=2.2,<2.3',
        'djangorestframework>=3.10,<4.0',
        'structlog<19.2.0',
        'jinja2<2.9',
        'PyYAML>=5.1,<5.2',
        'PyStaticConfiguration==0.10.4',
        'requests<2.13',
        'PyConfigure==0.5.9',
        'django-annoying==0.10.3',
    ],
    extras_require={
        'test': [
            'pytest-django>=3.5,<3.6',
            'freezegun',
            'psycopg2-binary',
            'pytest-cov>=2.7,<2.8',
        ],
        'docs': [
            'sphinx==1.5.1',
            'sphinx-autobuild==0.6.0',
            'sphinx_rtd_theme==0.1.9',
        ]
    },
    include_package_data=True,
    license='MIT',
    author='Mwas',
    author_email='mwasgize@gmail.com',
    description='Ussd Airflow Library'
)
