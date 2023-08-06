from setuptools import setup, find_packages


setup(
    name='Cuke',
    version='0.0.1',
    license='MIT',
    author="Tom Grek",
    author_email='tom.grek@gmail.com',
    packages=find_packages('cuke'),
    package_dir={'': 'cuke'},
    url='https://github.com/tomgrek/cuke',
    keywords='python;machine learning;docker;platform',
    install_requires=[
          'docker',
      ],

)