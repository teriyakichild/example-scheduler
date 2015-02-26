from setuptools import setup
from sys import path

path.insert(0, '.')

NAME = "example_scheduler"

if __name__ == "__main__":

    setup(
        name = NAME,
        version = "0.0.1",
        author = "Tony Rogers",
        author_email = "tony@tonyrogers.me",
        url = "https://github.com/teriyakichild/example_scheduler",
        license = 'internal use',
        packages = [NAME],
        package_dir = {NAME: NAME},
        description = "Example Scheduler",

        install_requires = ['apscheduler',
                            'argparse',
                            'tornado',
                            'ConfigParser'],
        entry_points={
            'console_scripts': [ 'example-scheduler = example_scheduler:main' ],
        }
    )

