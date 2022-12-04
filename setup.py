from setuptools import find_packages, setup

setup(name='TSMtester',
      version='0.0.4',
      description='Traveling salesman problem for testing and benchmarking optimization algorithms',
      author='Tommer Rissin',
      author_email='tommerrissin@gmail.com',
      url='https://github.com/Tommer-R/Traveling-salesman',
      packages=find_packages('src'),
      package_dir={'': 'src'},
     )