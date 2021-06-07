#import dependencies
import shutil

# shutil.make_archive('new', 'zip', 'files')
#('name','file type', 'directory')

shutil.unpack_archive('new.zip', 'new')
#('name of zipfile','directory')

# FILE TYPES

# zip - ZIP file
# tar - uncompressed tar file
# gztar - gzip'ed tar-file
# bztar - bzip'ed tar-file
# xztar - xz'ed tar-file
