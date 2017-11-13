# Copyright (c) 2017 Red Hat, Inc.
# This file is part of sse2fedmsg.
#
# fegistry is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# fegistry is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Foobar.  If not, see <http://www.gnu.org/licenses/>.
import os

from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(here, 'README.md')) as fd:
    README = fd.read()

setup(
    name='sse2fedmsg',
    version='0.3.0',
    description='Turn Server-Sent Events into fedmsgs.',
    long_description=README,
    license='GPLv2+',
    maintainer='Fedora Infrastructure Team',
    maintainer_email='infrastructure@lists.fedoraproject.org',
    platforms=['Fedora', 'GNU/Linux'],
    url='https://github.com/fedora-infra/sse2fedmsg',
    keywords='fedora',
    packages=find_packages(exclude=('sse2fedmsg.tests', 'sse2fedmsg.tests.*')),
    include_package_data=True,
    zip_safe=False,
    install_requires=['fedmsg[commands,consumers]', 'sseclient'],
    extras_require={
        'secure': ['fedmsg[crypto]']
    },
    tests_require=['flake8'],
    test_suite='sse2fedmsg/tests',
    entry_points={
        'console_scripts': [
            'sse2fedmsg = sse2fedmsg:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
