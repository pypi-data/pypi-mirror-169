from distutils.core import setup

setup(
    name="chainweb.py",
    packages=["chainwebpy"],
    version="0.1.5",
    license="MIT",
    description="High level Python bindings for the Kadena Chainweb REST API.",
    author="Mert Köklü",
    author_email="mert@yuugen.art",
    readme="README.md",
    url="https://github.com/justmert/chainweb.py",
    download_url="https://github.com/justmert/chainweb.py/archive/refs/tags/0.1.5.tar.gz",
    keywords=["Kadena", "Rest", "Chainweb", "API"],
    install_requires=[
        "requests",
        "typing",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",  # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        "Intended Audience :: Developers",  # Define that your audience are developers
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",  # Again, pick a license
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
