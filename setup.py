import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rndinfo',
    version='1.0.0',
    packages=['rndinfo'],
    author="Alex Panchenko based on Bhuvan Gandhi",
    author_email="pan.pan.4it@gmail.com",
    description="Random data generator for IDs, names, emails, passwords, dates, numbers, addresses, images, OTPs etc. for dummy entries.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={
        'rndinfo': ['data.csv', 'images/people/*.jpg']
    },
    url="https://github.com/alex-pancho/randominfo",
    download_url = f'{url}/dist/rndinfo-{version}.tar.gz',
    python_requires='>=3',
    install_requires=["pytz>=2018.5"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)