import setuptools

setuptools.setup(
    name='deephide',
    description='Python tool to hide information in media files',
    author='waldemar',
    author_email='helldoge@tuta.io',
    packages=['deephide'],
    entry_points={
        'console_scripts': [
            'deephide = deephide.__main__:main',
        ],
    },
)
