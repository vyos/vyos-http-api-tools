# vyos-http-api-tools — AI coding context

## Project purpose
Debian packaging wrapper that bundles the Python runtime dependencies of the VyOS HTTP API (FastAPI, uvicorn, ariadne, etc.) as a single `.deb` installed on VyOS images. **Contains no application logic** — the actual HTTP API implementation lives in `vyos-1x/src/services/`. Maintained as a separate package so that not-yet-Debian-packaged Python libraries can ship and update independently of VyOS releases.

## Tech stack
- Python — runtime dependency staging. `setup.py` + `requirements.in`/`requirements.txt`.
- Debian packaging with `dh-virtualenv` (≥1.0). `debian/control` build-depends: `debhelper (>= 10)`, `python3`, `python3-setuptools`, `dh-virtualenv (>= 1.0)`, `python3-pip`, `python3-venv`.
- Top-level `vyos-http-api-tools` directory is the install root copied into the venv.

## Build / test / run
```
dpkg-buildpackage -uc -us -tc -b
# Update pinned versions from requirements.in:
pip-compile requirements.in  # writes requirements.txt by default
```
No application-level test runner — the package is exercised at runtime by `vyos-1x`'s API services.

## Repository layout
- `vyos-http-api-tools/` — payload directory copied into the dh-virtualenv venv.
- `requirements.in` — un-pinned top-level deps.
- `requirements.txt` — pinned full graph (regenerate via `pip-compile`).
- `setup.py` — packaging shim.
- `debian/` — packaging files (`control`, `rules`, etc.).
- `README.md` — explains the wrapper-only nature and lists upstream packages.

## Cross-repo context
- The actual HTTP API server code lives in `vyos/vyos-1x` (`python/vyos/`, `src/services/`, supporting Jinja2 templates and op-mode definitions). This repo only stages the runtime libs.
- Built into ISOs by `vyos/vyos-build`; listed in an internal repository as one of the 14 canonical source repos.
- Bundled libraries (per `README.md`): FastAPI, uvicorn, ariadne, makefun, sgqlc, pyjwt, python-pam, python-multipart, wsproto.

## Conventions
- Commit/PR title: `component: T12345: description` (Phorge task ID at https://vyos.dev). Enforced by `check-pr-message.yml` reusable.
- Workflows: `pr-mirror-repo-sync.yml`, `trigger-rebuild-repo-package.yml`, `codeql.yml`, `cla-check.yml` (all `vyos/.github@production` reusables).
- Bumping `requirements.in` → regenerate `requirements.txt` via `pip-compile` (`pip-tools`) in the same PR. Pin full graph for reproducible builds.

## Notes for future contributors
- Do **not** add application logic here. Anything API-related goes in `vyos-1x`.
- Any new library required by the HTTP API: append to `requirements.in`, regenerate `requirements.txt`, validate that the version installs cleanly inside `dh-virtualenv` (Python 3 + Debian bookworm).
- After merge, `trigger-rebuild-repo-package.yml` fires REST `workflow_dispatch` into `$REMOTE_OWNER/vyos-build-packages` (REMOTE_OWNER = the private side) to rebuild the `.deb` as `vyosbot`.
- Watch FastAPI/uvicorn version pins for compat with the VyOS Python release (currently 3.11/3.12 on bookworm).
