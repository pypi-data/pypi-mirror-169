from distutils.core import setup

setup(
    name='kybra',
    version='0.0.3',
    package_data={
        '': ['compiler/**']
    },
    include_package_data=True,
    packages=['kybra']
)

# TODO seems like I have to do this to upload a new version
