from setuptools import setup, find_packages

setup(
    name = 'merchant_uniqueness', 
    version= '0.1',
    description= 'Divergence to determine the merchant uniqueness',
    author= 'Jay Jo',
    packages= find_packages(),
    install_requires = ['scikit-learn', 'scipy','plotly','numpy','pandas','seaborn','matplotlib'],
    zip_safe = False
    )