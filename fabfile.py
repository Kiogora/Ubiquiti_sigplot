from fabric.api import run
from fabric.api import env

env.hosts = ['ubnt@192.168.1.1']
env.warn_only=True
env.shell="/bin/sh -c"

def host_type():
    pass
    run("iwconfig ath0 | grep Signal")


