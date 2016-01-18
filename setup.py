from __future__ import print_function

import setuptools
import sys

# Convert README.md to reStructuredText.
if {'bdist_wheel', 'sdist'}.intersection(sys.argv):
    try:
        import pypandoc
    except ImportError:
        print('WARNING: You should install `pypandoc` to convert `README.md` '
              'to reStructuredText to use as long description.',
              file=sys.stderr)
    else:
        print('Converting `README.md` to reStructuredText to use as long '
              'description.')
        long_description = pypandoc.convert('README.md', 'rst')

setuptools.setup(
    name='django-timezone',
    use_scm_version={'version_scheme': 'post-release'},
    author='Interaction Consortium',
    author_email='studio@interaction.net.au',
    url='https://github.com/ixc/django-timezone',
    description='Helper functions for working with datetime objects without '
                'caring if they are timezone aware or not.',
    long_description=locals().get('long_description', ''),
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'coverage',
        'django-nose',
        'django-webtest',
        'mkdocs',
        'nose-progressive',
        'pytz',
        'six',
        'tox',
        'WebTest',
    ],
    extras_require={
        'dev': ['ipdb', 'ipython'],
    },
    setup_requires=['setuptools_scm'],
)
