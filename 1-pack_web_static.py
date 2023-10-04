#!/usr/bin/python3
from fabric.api import local
from datetime import datetime
# setting the time to use in archive naming
stand_time = datetime.now.strftime("%Y%m%d%H%M%S")
# setting the name of the archive
archive_name = 'versions/web_static_{}.tgz'.format(stand_time)
#creating folder if not exixt using fabric
local("mkdir -p versions")
archived = local('tar -cvzf {} web_static'.format(archive_name))
# archive creating and showing it's status
if archived.return_code != 0:
    return None
else:
    return archive_path
