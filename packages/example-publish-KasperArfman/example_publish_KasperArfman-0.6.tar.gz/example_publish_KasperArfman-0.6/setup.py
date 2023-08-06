from setuptools import setup, find_packages


setup(
    name='example_publish_KasperArfman',
    version='0.6',
    license='MIT',
    author="Kasper Arfman",
    author_email='kasper.arf@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Kasper-Arfman/wrappers',
    keywords='example project',
    install_requires=[
          'numpy',
      ],

)