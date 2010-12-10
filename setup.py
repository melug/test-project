from setuptools import setup, find_packages

setup(name = 'Music Player',
    version = '0.1',
    author = 'Sharavsambuu',
    description = 'Music Player',
    packages = find_packages(),
    include_package_data = True,
    install_requires = [ ],
    entry_points = {
            'console_scripts' : [
                'shmusic = musicplayer:main',
            ]
        }
    )
