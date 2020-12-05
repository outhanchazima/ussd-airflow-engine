from setuptools import setup, find_packages
from ussd import VERSION


setup(
    name='ussd_airflow',
    version=VERSION,
    packages=find_packages(exclude=('ussd_airflow',)),
    url='https://github.com/mwaaas/ussd_airflow',
    install_requires=[
        'Django>=2.2,<3.2',
        'djangorestframework>=3.10,<4.0',
        'structlog<20.2.0',
        'jinja2<2.12',
        'PyYAML>=5.1,<5.4',
        'PyStaticConfiguration==0.10.5',
        'requests<2.25',
        'PyConfigure==0.5.9',
    ],
    extras_require={
        'test': [
            'pytest-django>=3.5,<4.1',
            'freezegun',
            'psycopg2-binary',
            'pytest-cov>=2.7,<2.11',
        ],
        'docs': [
            'sphinx>=2.2,<3.3',
            'sphinx-autobuild>=0.7,<2020.10',
            'sphinx_rtd_theme>=0.4,<0.6',
        ]
    },
    include_package_data=True,
    license='MIT',
    author='Mwas',
    author_email='mwasgize@gmail.com',
    description='Ussd Airflow Library'
)
