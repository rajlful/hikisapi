#!F:\learn_python\Hikvision\hikenv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Babel==2.9.1','console_scripts','pybabel'
__requires__ = 'Babel==2.9.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Babel==2.9.1', 'console_scripts', 'pybabel')()
    )
