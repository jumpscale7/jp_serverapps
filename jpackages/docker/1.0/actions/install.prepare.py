def main(j,jp):
   
#     cmd="""
# [ -e /usr/lib/apt/methods/https ] || {
#   apt-get update
#   apt-get install apt-transport-https
# }

# sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 36A1D7869245C8950F966E92D8576A8BA88D21E9
# sh -c "echo deb https://get.docker.io/ubuntu docker main /etc/apt/sources.list.d/docker.list"

# """

    cmd="""
sh -c "echo deb https://get.docker.io/ubuntu docker main > /etc/apt/sources.list.d/docker.list"
apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys
    """

    j.system.process.executeWithoutPipe(cmd)

    print "update apt"
    j.system.process.executeWithoutPipe("apt-get update -y")

    print "install lxc docker"
    j.system.platform.ubuntu.install("lxc-docker")

    
    j.system.process.executeWithoutPipe("pip install docker-py")

    j.system.process.executeWithoutPipe("sudo service docker restart")
    