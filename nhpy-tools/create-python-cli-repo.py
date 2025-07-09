import os

project_name = "mytool"
package_dir = f"src/{project_name}"
test_dir = f"tests"

os.makedirs(package_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# src/mytool/__init__.py
with open(f"{package_dir}/__init__.py", "w") as f:
    f.write('__version__ = "0.0.0"\n')

# src/mytool/cli.py
with open(f"{package_dir}/cli.py", "w") as f:
    f.write('''\
def main():
    print("Hello from mytool!")
''')

# tests/test_cli.py
with open(f"{test_dir}/test_cli.py", "w") as f:
    f.write(f'''\
from {project_name}.cli import main

def test_main(capsys):
    main()
    captured = capsys.readouterr()
    assert "Hello from mytool!" in captured.out
''')

# pyproject.toml
with open("pyproject.toml", "w") as f:
    f.write(f'''\
[build-system]
requires = ["setuptools>=42", "setuptools_scm[toml]>=6.2", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "{project_name}"
dynamic = ["version"]
description = "A modern CLI tool example"
authors = [{{ name = "Your Name", email = "you@example.com" }}]
readme = "README.md"
requires-python = ">=3.7"
dependencies = ["requests", "arrow"]

[project.scripts]
{project_name} = "{project_name}.cli:main"

[tool.setuptools]
package-dir = {{"" = "src"}}

[tool.setuptools.packages.find]
where = ["src"]

[tool.setuptools_scm]
version_file = "src/{project_name}/_version.py"
''')

# README.md
with open("README.md", "w") as f:
    f.write(f'''\
# {project_name}

A simple CLI tool.

## Install from GitHub

```bash
pip install git+https://github.com/your-username/{project_name}.git
