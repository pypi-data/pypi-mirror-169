from setuptools import setup, Extension
setup(
    name='pygetkey',
    version='1.0.0',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description='A Python module to get the pressed key',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/getkey',
    project_urls={
        'Documentation': 'https://github.com/donno2048/getkey#readme',
        'Bug Reports': 'https://github.com/donno2048/getkey/issues',
        'Source Code': 'https://github.com/donno2048/getkey'
    },
    ext_modules=[Extension('getkey', ['getkey.c'])],
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3"
    ],
    zip_safe = False
)