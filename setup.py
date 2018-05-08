from setuptools import setup, find_packages

setup(name='camera',
    version='0.0',
    description='This can take pictures with PC camera.',
    author='appBana',
    url='https://howmuch515.github.io/',
    packages=find_packages(),
    entry_points="""
        [console_scripts]
        camera = camera.camera:main
    """,)
