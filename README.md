# encodingchange
This module scans a directory and convert the encoding of all files with the specified extensions in mac os

# Language
python 2

# Dependencies
libmagic: https://linux.die.net/man/3/libmagic
    brew install libmagic
python-magic: https://github.com/ahupp/python-magic
    pip install python-magic
    
# Usage
python encodingchange.py PAHT_TO_DIR FILE_Extension -b BOOL -s SOURCE_ENCODING -d NEW_ENCODING
