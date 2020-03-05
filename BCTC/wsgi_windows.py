activate_this = 'C:/Users/Administrator/Envs/videoportal/Scripts/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/Administrator/Envs/videoportal/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/Users/Administrator/Desktop/Django_project/BCTC')
sys.path.append('C:/Users/Administrator/Desktop/Django_project/BCTC/BCTC')

os.environ['DJANGO_SETTINGS_MODULE'] = 'BCTC.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BCTC.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()