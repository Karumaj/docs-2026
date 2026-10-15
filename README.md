# My Projects Repo

A Sphinx documentation site that records key details of completed and active projects, organised by timeline and classified by five binary characteristics:

- Software vs. infrastructure projects
- Remotely managed vs. onsite-managed projects
- Client-initiated vs. internally initiated projects
- End-to-end vs. component-based projects
- Full rollout vs. phased rollout

## Structure

| File | Purpose |
|------|---------|
| `index.rst` | Home page: overview, project timeline, key references |
| `successful-projects.rst` | Matrix of projects that met their objectives, with success factors |
| `unsuccessful-projects.rst` | Matrix of projects that fell short, with causes and lessons learned |
| `conf.py` | Sphinx configuration |

## Getting Started

Install Sphinx:

```bash
pip install sphinx
```

Build the HTML site from the repo root:

```bash
sphinx-build -b html . _build/html
```

Or, if you used `sphinx-quickstart` with a Makefile:

```bash
make html
```

Open `_build/html/index.html` in a browser to view the result.

## Adding a Project

1. Add a row to the relevant matrix in `successful-projects.rst` or `unsuccessful-projects.rst`.
2. Classify it using the five binary characteristics.
3. Rebuild the site and check for warnings.

## Notes

- Use spaces, not tabs, in `.rst` files. RST is indentation-sensitive.
- Section underlines must be at least as long as the title text.