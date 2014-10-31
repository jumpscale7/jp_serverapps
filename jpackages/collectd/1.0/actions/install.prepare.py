def main(j,jp):
   
    do=j.system.installtools

    do.execute("/etc/init.d/collectd stop",dieOnNonZeroExitCode=False)
    do.execute("sudo service collectd stop",dieOnNonZeroExitCode=False)
    j.system.platform.ubuntu.remove("collectd")

    do.execute("apt-get autoremove -y",dieOnNonZeroExitCode=False)    

    j.system.fs.removeDirTree("/etc/init.d/collectd")
    j.system.fs.removeDirTree("/etc/collectd")
    j.system.fs.removeDirTree("/var/lib/collectd")

    
    pass