import setuptools

ver = '3.0.0'
url = "https://github.com/alex-pancho/randominfo"
with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='rndinfo',
    version=ver,
    packages=['rndinfo'],
    author="Alex Panchenko based on Bhuvan Gandhi",
    author_email="pan.pan.4it@gmail.com",
    description="Random data generator for IDs, names, emails, passwords, dates, numbers, addresses, "
                "images, OTPs etc. for dummy entries.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_data={
        'rndinfo': ['data.csv', 'images/people/*.jpg']
    },
    url=url,
    download_url=f'{url}/dist/rndinfo-{ver}.tar.gz',
    python_requires='>=3',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)