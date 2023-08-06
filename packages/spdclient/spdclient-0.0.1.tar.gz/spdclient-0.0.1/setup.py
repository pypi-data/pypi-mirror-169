from setuptools import setup

setup(
    name="spdclient",
    version="0.0.1",
    description="Python Wrapper for Scrapyd WebService",
    long_description="It is a Python Wrapper for Scrapyd WebService for easy use of Scrapyd API",
    author="Kanchan Sapkota",
    author_email="kanchansapkota27@gmail.com",
    license="MIT",
    install_requires=[
        "httpx>=0.23.0",
        "pytest>=7.1.3",
        "pytest-html>=3.1.1",
    ],
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "Programming Language :: Python :: 3.10",
    ],
    keywords="scrapyd scrapy python scrapydapi scrapyd-client api",
    packages=["spdclient"],
    zip_safe=False,
)
