from setuptools import setup


setup(
    name='github_webhook_app',

    version='1',

    description='Quickly create github webhook apps',
    long_description='',

    author='Josh Ghiloni',
    author_email='ghiloni@gmail.com',

    license='MIT',

    packages=['github_webhook_app.app', 'github_webhook_app.decorators', 'github_webhook_app.generator_utils'],
    zip_safe=False,
)