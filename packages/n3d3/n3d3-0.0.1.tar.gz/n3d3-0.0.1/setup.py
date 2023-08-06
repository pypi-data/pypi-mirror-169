#!/usr/bin/env python3
""" New Neural Network Design, Deployment & Discovery

N3D3 is a Python package to use the new N2D2 engine.
"""

DOCLINES = (__doc__ or '').split("\n")

VERSION="0.0.1"

import sys
import os

# Python supported version checks
if sys.version_info[:2] < (3, 7):
    raise RuntimeError("Python version >= 3.7 required.")



CLASSIFIERS = """\
Development Status :: 3 - Alpha
Intended Audience :: Developers
Intended Audience :: Education
Intended Audience :: Science/Research
License :: OSI Approved :: CEA CNRS Inria Logiciel Libre License, version 2.1 (CeCILL-2.1)
Programming Language :: C++
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.7
Programming Language :: Python :: 3.8
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3 :: Only
Topic :: Scientific/Engineering
Topic :: Scientific/Engineering :: Artificial Intelligence
Topic :: Software Development
Topic :: Software Development :: Libraries
Topic :: Software Development :: Libraries :: Python Modules
Typing :: Typed
Operating System :: POSIX
"""

import shutil
import pathlib
import subprocess
import multiprocessing

from setuptools import setup, Extension
from setuptools import find_packages
from setuptools.command.build_ext import build_ext


def test_installed_libraries():
    lib = ["make", "cmake"]
    for x in lib:
        try:
            out = subprocess.check_output([x, '--version'])
        except OSError:
            raise RuntimeError(f"{x} must be installed to build n3d3")


class CMakeExtension(Extension):
    def __init__(self, name):
        super().__init__(name, sources=[])

class CMakeBuild(build_ext):

    def run(self):

        test_installed_libraries()

        # This lists the number of processors available on the machine
        # The compilation will use half of them
        max_jobs = str(int(multiprocessing.cpu_count() / 2))

        cwd = pathlib.Path().absolute()

        build_temp = cwd / "build"
        if not build_temp.exists():
            build_temp.mkdir(parents=True, exist_ok=True)

        build_lib = pathlib.Path(self.build_lib)
        if not build_lib.exists():
            build_lib.mkdir(parents=True, exist_ok=True)

        os.chdir(str(build_temp))

        self.spawn(['cmake', str(cwd)])
        if not self.dry_run:
            self.spawn(['make', '-j', max_jobs])
  
        os.chdir(str(cwd))

        ext_lib = build_temp / "lib"

        # Copy all shared object files from build_temp/lib to build_lib
        for root, dirs, files in os.walk(ext_lib.absolute()):
            for file in files:
                if file.endswith('.so') or file.endswith('.pyd'):
                    currentFile=os.path.join(root, file)
                    shutil.copy(currentFile, str(build_lib.absolute() / "n3d3"))           


if __name__ == '__main__':
    packages = find_packages(where=".", exclude="n3d3/_libN3D3")

    setup(
        name='n3d3',
        version=VERSION,
        url='https://github.com/CEA-LIST/N2D2',
        license='CECILL-2.1',
        author='N2D2 Team',
        author_email='n2d2-contact@cea.fr',
        python_requires='>=3.7',
        description=DOCLINES[0],
        long_description_content_type="text/markdown",
        long_description="\n".join(DOCLINES[2:]),
        keywords=['n3d3', 'machine', 'learning'],
        project_urls={
            "Bug Tracker": "https://github.com/CEA-LIST/N2D2/issues",
            "Documentation": "https://cea-list.github.io/N2D2-docs/",
            "Source Code": "https://github.com/CEA-LIST/N2D2",
        },
        classifiers=[c for c in CLASSIFIERS.split('\n') if c],
        platforms=["Linux"],
        packages=packages,
        package_dir={
            "n3d3": "n3d3",
        },
        ext_modules=[CMakeExtension('libN3D3')],
        cmdclass={
            'build_ext': CMakeBuild,
        },

    )
