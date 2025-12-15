"""
Flask SQLAlchemy定时任务管理包
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="flask-scheduler-manager",
    version="1.0.0",
    author="binger",
    author_email="xuehen_521@126.com",
    description="基于Flask SQLAlchemy和flask_apscheduler的动态定时任务管理系统",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BingerYang/flask-scheduler-manager",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    include_package_data=True,
    zip_safe=False,
)

