# vyos-http-api-tools
Debian files for wrapping FastAPI and supporting tools as a deb package,
using dh_virtualenv

This is a dependency of vyos-1x; maintaining it as a separate package, for
now, allows tools that are not yet available in the Debian distros and quick
updating for bugs/security fixes.

To build:

    dpkg-buildpackage -uc -us -tc -b

To update dependency versions from un-versioned packages names:
(Install pip-compile from 'pip-tools')

    pip-compile requirements.in > requirements.txt

Main packages, not including dependencies; cf. requirements.txt:

FastAPI
https://github.com/tiangolo/fastapi

Uvicorn
https://github.com/encode/uvicorn

Ariadne
https://github.com/mirumee/ariadne

makefun
https://github.com/smarie/python-makefun
