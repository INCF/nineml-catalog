import nineml
import os.path

def check_dir(dir_name):
    for fname in os.listdir(dir_name):
        path = os.path.join(dir_name, fname)
        if os.path.isdir(path) and fname not in ('_old_formats', 'randomdistributions'):
            check_dir(path)
        elif fname.endswith('xml'):
            try:
                nineml.read(path)[fname[:-4]]
            except Exception, e:
                print "----\n{}: {}\n".format(fname, e)
                
check_dir(os.getcwd())
# print nineml.read(
#     '/Users/tclose/git/nineml_catalog/neurons/Izhikevich2007.xml')[
#         'IzhikevichClass']
