import os
import shutil
import subprocess
import sys
from typing import Any, ClassVar

from setuptools import Command, Extension, setup
from setuptools.command.build_ext import build_ext

try:
    from setuptools.command.bdist_wheel import bdist_wheel as _bdist_wheel
except ImportError:
    from wheel.bdist_wheel import bdist_wheel as _bdist_wheel
from setuptools.command.build_py import build_py
from setuptools.command.develop import develop
from setuptools.command.install import install

file_dir = os.path.abspath(os.path.dirname(__file__))
os.chdir(file_dir)

sys.path.insert(0, file_dir)
sys.path.insert(0, os.path.join(file_dir, "camb"))
_compile: Any = __import__("_compilers")

if _compile.is_windows:
    DLLNAME = "cambdll.dll"
else:
    DLLNAME = "camblib.so"


def get_forutils():
