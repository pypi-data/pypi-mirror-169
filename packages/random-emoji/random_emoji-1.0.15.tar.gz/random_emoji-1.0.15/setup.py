from setuptools import setup

setup(
    name="random_emoji",
    version="1.0.15",
    description="Get Random Emoji",
    url="https://github.com/cobanov/random_emoji",
    author="Mert Cobanov",
    author_email="mertcobanov@gmail.com",
    license="MIT",
    packages=["random_emoji"],
    install_requires=[
        "urllib3",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
    ],
)
