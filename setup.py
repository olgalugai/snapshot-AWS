from setuptools import setup

setup(

    name = "snapshot_python",
    version = "0.1",
    description = "snapshot_python is a tool to manage AWS EC2 snapshots",
    packages = ['snapshots'],
    url = 'https://github.com/olgalugai/snapshot-AWS',
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
    [console_scripts]
    scnapshots=snapshots.snapshots:cli
    ''',

)