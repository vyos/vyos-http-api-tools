# vyos-http-api-tools
Debian files for wrapping FastAPI and supporting tools as a deb package, using dh_virtualenv

To build:

    dpkg-buildpackage -uc -us -tc -b

To update dependency versions from un-versioned packages names:
(Install pip-compile from 'pip-tools')

    pip-compile requirements.in > requirements.txt
