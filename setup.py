from setuptools import setup, find_packages

setup(
    name='rest_api_demo',
    version='0.0.1',
    description='Rest API Demo',
    url=',
    author='Erick Alvarez',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='',

    packages=find_packages(),

    install_requires=['flask-restplus==0.9.2'],
)
