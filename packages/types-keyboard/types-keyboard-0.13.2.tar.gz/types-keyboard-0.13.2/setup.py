from setuptools import setup

name = "types-keyboard"
description = "Typing stubs for keyboard"
long_description = '''
## Typing stubs for keyboard

This is a PEP 561 type stub package for the `keyboard` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `keyboard`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/keyboard. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `48e76e8a5696797929fe6fcdd782de7ab1dc5f90`.
'''.lstrip()

setup(name=name,
      version="0.13.2",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/keyboard.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['keyboard-stubs'],
      package_data={'keyboard-stubs': ['__init__.pyi', '_canonical_names.pyi', '_generic.pyi', '_keyboard_event.pyi', '_mouse_event.pyi', 'mouse.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
