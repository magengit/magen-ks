from setuptools import setup
import sys
import pip

if sys.version_info < (3, 5, 2):
    sys.exit("Sorry, you need Python 3.5.2+")

pip_version = int(pip.__version__.replace(".", ""))
if pip_version < 901:
        sys.exit("Sorry, you need pip 9.0.1+")

setup(
    name='magen_key_service',
    version='1.6a1',
    install_requires=[
        'aniso8601>=1.2.1',
        'boto3>=1.4.4',
        'datadog>=0.16.0',
        'PyJWT>=1.5.2',
        'Flask>=0.12.2',
        'flake8>=3.3.0',
        'pymongo>=3.4.0',
        'pytest>=3.1.3',
        'magen_utils==1.2a2',
        'magen_rest_service==1.2a2'
      ],
    scripts=['ks_server/ks_server.py'],
    package_dir={'': '..'},
    packages={'ks', 'ks.settings', 'ks.ks_server', 'ks.ks_api', 'ks.ks_api.kms_apis', 'ks.ks_api.key_service_api'},
    include_package_data=True,
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        '': ['*.txt', '*.rst']
    },
    test_suite='tests',
    url='',
    license='Proprietary License',
    author='Paul Quinn',
    author_email='paulq@cisco.com',
    description='Magen Key Service Package',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 2 - Pre-Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Education',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Legal Industry',
        'Topic :: Security',

        # Pick your license as you wish (should match "license" above)
        'License :: Other/Proprietary License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.5',
    ],
)
