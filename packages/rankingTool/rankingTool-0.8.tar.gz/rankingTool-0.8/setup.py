from setuptools import setup, find_packages

setup(
    name='rankingTool',
    version='0.8',
    license='MIT',
    author="Haoqiang Kang",
    author_email='haoqik@cs.washington.edu',
    packages=find_packages(),
    url='https://github.com/mk322/Rankings-UI',
    description="This is the first version of the package of Rankings UI, which helps visualize the rankings and ratings for comparison.",
    keywords=['GUI', "Rankings", "Ratings"],
    install_requires=[
          'toml',
          'pandas',
          'numpy',
          "xlrd >= 1.0.0"]
    )
