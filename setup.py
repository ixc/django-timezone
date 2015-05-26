import setuptools

from timezone import __version__

setuptools.setup(
    name='timezone',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'django-dynamic-fixture',
        'django-nose',
        'django-webtest',
        'mkdocs',
        'nose-progressive',
        'tox',
        'WebTest',
    ],
    extras_require={
        'dev': ['ipdb', 'ipython'],
        'postgres': ['psycopg2'],
    },
)
