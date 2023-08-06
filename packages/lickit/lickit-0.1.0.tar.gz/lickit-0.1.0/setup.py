from setuptools import setup, find_packages
from lickit import version

install_requires = [
]
setup(
    name = 'lickit',
    version=version,
    author='Aunity',
    author_email='maohuay@hotmail.com',
    description=('A toolkit for breaking licensing restrictions.'),
    url='https://github.com/Aunity/lickit',
    license=None,
    keywords='License',
    install_requires=install_requires,
    packages=find_packages(),
    zip_safe = False,
    #packages=packages,
    entry_points={'console_scripts': [
         'mmxsaparse = lickit.CLI:GMXMMPBSA_cli',
     ]},
    include_package_data=True
)
