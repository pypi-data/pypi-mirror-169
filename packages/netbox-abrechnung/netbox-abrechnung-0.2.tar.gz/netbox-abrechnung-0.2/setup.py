from setuptools import find_packages, setup

setup(
    name='netbox-abrechnung',
    version='0.2',
    download_url='',
    description='Manage Leistungsscheine in Netbox',
    install_requires=[],
    packages=['netbox_abrechnung','netbox_abrechnung.api'],
    include_package_data=True,
    zip_safe=False,
)
