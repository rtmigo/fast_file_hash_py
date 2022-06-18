from pathlib import Path


from setuptools import setup, find_packages


def load_module_dict(filename: str) -> dict:
    import importlib.util as ilu
    filename = Path(__file__).parent / filename
    spec = ilu.spec_from_file_location('', filename)
    module = ilu.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.__dict__


name = "coarse_hash"

readme = (Path(__file__).parent / 'README.md').read_text(encoding="utf-8")
readme = "# " + readme.partition("\n#")[-1]

setup(
    name=name,
    version="0.2.0",

    author="Artëm IG",
    author_email="ortemeo@gmail.com",
    url='https://github.com/rtmigo/coarse_hash_py',

    packages=find_packages(exclude=['tests']),

    install_requires=[],

    description="",

    long_description=readme,
    long_description_content_type='text/markdown',

    license="MIT",

    keywords="".split(),

    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Typing :: Typed",
     ],
)
