import os
from distutils.core import setup
from typing import List

from setuptools import find_packages


def find_stub_files(name: str) -> List[str]:
    result = []
    for root, dirs, files in os.walk(name):
        for file in files:
            if file.endswith('.pyi'):
                if os.path.sep in root:
                    sub_root = root.split(os.path.sep, 1)[-1]
                    file = os.path.join(sub_root, file)
                result.append(file)
    return result


with open('README.md', 'r') as f:
    readme = f.read()

dependencies = [
    'mypy>=0.760,<0.770',
    'typing-extensions',
]

setup(
    name="attrdict-stubs",
    version="0.1",
    description='MyPy stubs for attrdict',
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    url="https://github.com/typeddjango/django-stubs",
    author="Anton Linevych",
    author_email="anton@linevich.net",
    py_modules=[],
    python_requires='>=3.6',
    install_requires=dependencies,
    packages=['attrdict-stubs', *find_packages(exclude=['scripts'])],
    package_data={'attrdict-stubs': find_stub_files('attrdict-stubs')},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ]
)
