import setuptools

# Reads the content of your README.md into a variable to be used in the setup below
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='xlsxColumnRow',                           # should match the package folder
    packages=['xlsxColumnRow'],                     # should match the package folder
    version='2.0.0',                                # important for updates
    license='MIT',                                  # should match your chosen license
    description='xlsx Package',
    long_description=long_description,              # loads your README.md
    long_description_content_type="text/markdown",  # README.md is of type 'markdown'
    author='codingChamp',
    author_email='codingChamp@gmail.com',
    install_requires=["pandas"],                  # list all packages that your package uses
    keywords=["pypi"], #descriptive meta-data
    classifiers=[                                   # https://pypi.org/classifiers
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Documentation',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ]
)