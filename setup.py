from distutils.core import setup

setup(name='craigsgenerator',
    author='Thomas Levine',
    author_email='_@thomaslevine.com',
    description='Iterate through Craig\'s list',
    url='https://github.com/tlevine/craigsgenerator.git',
    classifiers=[
        'Intended Audience :: Developers',
    ],
    packages=['craigsgenerator'],

    install_requires = ['requests','lxml'],
    tests_require = ['nose'],

    version='0.0.10',
    license='AGPL'
)
