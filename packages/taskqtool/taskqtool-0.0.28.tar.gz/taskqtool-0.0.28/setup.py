from setuptools import setup

with open(r"/mnt/d/Users/ZH/Desktop/tasks/requirements.txt") as fd:
    requires = fd.read().split("\n")
setup(
    install_requires=requires,
    data_files=[]
)
