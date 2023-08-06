from setuptools import find_packages, setup


setup(
    name='BinGame',
    version='0.0.1',
    description="一个基于图片的游戏库",
    long_description="",
    author="小斌",
    author_email="1302371440@qq.com",
    python_requires='>=3.7',
    url='',
    packages=find_packages(),
    install_requires=['pillow'],
    include_package_data=True,
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
