from setuptools import find_packages, setup

setup(
    name="nose_logger",
    version="1.0.0",
    author="Your Name",
    author_email="your_email@example.com",
    description="A short description of your package",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["psutil", "nose"],
    entry_points={"nose.plugins.0.10": ["nose_logger = nose_logger:NoseLoggerPlugin"]},
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
    ],
)
