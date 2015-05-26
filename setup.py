import setuptools

from timezone import __version__

setuptools.setup(
    name='timezone',
    version=__version__,
    packages=setuptools.find_packages(),
    install_requires=[
        'coverage',
        'django-nose',
        'django-webtest',
        'mkdocs',
        'nose-progressive',
        'pytz',
        'tox',
        'WebTest',
    ],
    extras_require={
        'dev': ['ipdb', 'ipython'],
    },
)
