# PHPUnit Documentation with Sphinx

The goal of this project is to come up with a proof-of-concept
for migrating PHPUnit's documentation from DocBook XML to
reStructuredText in order to achieve:

- an more streamlined process for contributing to the documentation
- better support for translations
- an easier build process

As this is a work in progress, the repository only contains the
documentation for PHPUnit 6.1.

## Converting DocBook XML to ReStructuredText

### Requirements

- Python

Running the `conversion/DockbookToReST` Bash script will take all XML files from
`src/6.1/en/`, convert them to `.rst` files with the help of
`dockbookToRst.py` and write them to `src/en/source`.

## Building the HTML Documentation

### Requirements

- Python
- [Sphinx](http://www.sphinx-doc.org/)

To build the complete documentation use:

    cd src/en
    make html

Afterwards you will find the HTML files in `src/en/build/html`.