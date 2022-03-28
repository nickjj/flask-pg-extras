from setuptools import setup


setup(
    name="Flask-PG-Extras",
    version="0.2.0",
    author="Nick Janetakis",
    author_email="nick.janetakis@gmail.com",
    url="https://github.com/nickjj/flask-pg-extras",
    description="Flask extension to obtain useful information from your PostgreSQL database.",
    license="MIT",
    long_description=__doc__,
    package_data={"Flask-PG-Extras": ["VERSION"]},
    packages=["flask_pg_extras", "flask_pg_extras.queries"],
    platforms="any",
    python_requires=">=3.6",
    zip_safe=False,
    install_requires=[
        "Flask>=1.0",
        "SQLAlchemy>=1.3",
        "tabulate"
    ],
    entry_points={
        "flask.commands": [
            "pg-extras=flask_pg_extras.cli:pg_extras"
        ],
    },
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Database"
    ]
)
