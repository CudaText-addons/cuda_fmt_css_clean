import os
import re
import json
from . import cleancss 
from cuda_fmt import get_config_filename

def do_format(text):
    
    fn = get_config_filename('CSS Clean')
    s = open(fn, 'r').read()
    #del // comments
    s = re.sub(r'(^|[^:])//.*', r'\1', s)
    cleancss.settings = json.loads(s)

    lines = text.split('\n')    
    result = cleancss.CssRule('', lines, [], -1).output()
    result.pop()
    return '\n'.join(result)
