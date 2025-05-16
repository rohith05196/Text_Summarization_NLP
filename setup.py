import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_desctption = f.read()


    __version__ = "0.0.0"

    REPO_NAME = "Text_SUMMARIZATION_NLP"
    AUTHOR_USER_NAME = "rohith05196"
    SEC_REPO = "textsummarizer"
    AUTHOR_EMAIL = "rohithmijar.go@gmail.com"

    setuptools.setup(
        name=SEC_REPO,
        version=__version__,
        author=AUTHOR_USER_NAME,
        author_email=AUTHOR_EMAIL,
        description="An app for CNN",
        long_description=long_desctption,
        long_description_content_type="text/markdown",
        url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
        project_urls = {"Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues"},
        package_dir = {"": "src"},
        packages=setuptools.find_packages(where = "src")
    )