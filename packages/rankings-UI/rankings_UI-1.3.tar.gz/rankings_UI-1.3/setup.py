from setuptools import setup, find_packages


setup(
    name='rankings_UI',
    version='1.3',
    license='MIT',
    author="Haoqiang Kang",
    author_email='haoqik@cs.washington.edu',
    packages=find_packages(),
    url='https://github.com/mk322/Rankings-UI',
    description="This is the first version of the package of Rankings UI, which helps visualize the rankings and ratings for comparison.",
    keywords=['GUI'],
    install_requires=[
          'toml==0.10.2',
          'pandas==1.3.4',
          'numpy==1.22.2']
    )
