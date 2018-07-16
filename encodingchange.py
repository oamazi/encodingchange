"""
=======================================================
encodingchange.py Version 1.1
Osama Mazi (www.osa.ma)
Last Update: 16/7/2018
=======================================================
Python 2
Dependencies:
libmagic: https://linux.die.net/man/3/libmagic
    brew install libmagic
python-magic: https://github.com/ahupp/python-magic
    pip install python-magic
-------------------------------------------------------
This module scans a directory and convert the encoding
of all files with the specified extensions:
=======================================================
"""
import argparse, os, magic,time
def strbool(v):
    """changes the argument string to boolean
    Args:
        param1 (string): The expected boolean string.
    Returns:
        bool: The return value. True for success, False otherwise.
    """
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

def convert(file, backup=True,to=None, base=None):
    """converts a file's encoding from a specified
        type into a new one, with the ability to 
        keep the original file with .old extension
    Args:
        file (string): The file to be converted
        backup (boolean): keep a backup of the original file
        to (string): new file encoding
        base (string): original file encoding
    Returns:
        void
    """
    data = open(file).read()
    m = magic.Magic(mime_encoding=True)
    encoding=m.from_buffer(data)
    if(to == encoding):
        return
    if(to != base):
        source_file=file+".old"
        os.rename(file,source_file)
        destination_file=file
        print("Converting "+file+ " From: "+base+" To: "+to)
        cmd = "iconv -f " + base + " -t " + to + " \"" + source_file + "\" >> \"" + destination_file+"\""
        os.system(cmd)
        time.sleep(1)        
        if(backup==False):
            os.remove(source_file)

parser = argparse.ArgumentParser()
parser.add_argument("p", help="The path of the directory you want to search")
parser.add_argument("e", help="The extension of the file to convert (without .")
parser.add_argument("-b", "--backup", type=strbool, default=True, help="do you want to create a backup of the file")
parser.add_argument("-s", "--source", default="windows-1256", help="The source encoding of the file")
parser.add_argument("-t", "--to", default="utf-8", help="The new encoding of the file")
args = parser.parse_args()

for root, dirs, files in os.walk(args.p):
    for filename in files:
        file = os.path.join(root, filename)
        if filename.endswith("."+args.e):
            convert(file,args.backup,args.to, args.source)
print("Task Completed")
