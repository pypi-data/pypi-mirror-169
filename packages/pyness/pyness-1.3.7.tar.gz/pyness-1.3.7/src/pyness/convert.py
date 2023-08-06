from PIL import Image
from pyness.key import key
from pyness.getfileformat import getfileformat

def photo(filename,format):
    file = getfileformat(filename)
    img = Image.open(filename)
    img = img.convert('RGB')
    img.save(f'{key(5,number=5)}{format}')
    print(f"{file} is been converted to {format}")