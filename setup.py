from setuptools import setup, find_packages

setup(
    name="moodylang",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "moody = moodylang.__main__:main"
        ]
    },
    author="Abdur Rehman Tariq",
    author_email="your-email@example.com",
    description="A polite, emotional programming language interpreter",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/ARTariqDev/moodylang",  # (optional)
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # adjust if needed
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
