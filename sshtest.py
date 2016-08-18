#
#!/usr/bin/env python3
#

#from subprocess import PIPE, Popen

import subprocess
import sys

for octet2 in range(101, 199):
  for octet4 in range(2, 9):
    HOST="10.%d.250.%d" %(octet2, octet4)
    print(HOST)
 
    cmd = 'uname -a'
    ssh = subprocess.Popen(["ssh", "root@%s" % HOST, cmd], universal_newlines=True, close_fds=True, shell=False, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    rsp = ssh.stdout.readlines()
    if rsp == []:
      error = ssh.stderr.readlines()
      print ("ERROR: %s" %error, file=sys.stderr)
    else:
      print (rsp)
    ssh.kill()
