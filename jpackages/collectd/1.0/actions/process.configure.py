def main(j,jp):
   
    #configure the application to autostart
    
    # jp.log("set autostart $(jp.name)")

    # #example start osis
    cmd = 'cd /opt/collectd;sh start.sh'
    args = ''
    workingdir = ""
    name = jp.name
    domain = "serverapps"
    ports = []
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=50, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports)
    
    import psutil
    arg=""
    for part in psutil.disk_partitions():
        device=part.device[0:8]
        arg+="%s,"%device
    arg=arg.rstrip(",")

    cmd="killall hddtemp;cd /opt/collectd/bin;./hddtemp -d -f /opt/collectd/cfg/hddtemp.db -F %s"%arg
    args = ''
    workingdir = "/tmp"
    name = "hddtemp"
    domain = "serverapps"
    ports = [7634]
    j.tools.startupmanager.addProcess(name=name, cmd=cmd, args=args, env={}, numprocesses=1, priority=50, \
       shell=False, workingdir=workingdir,jpackage=jp,domain=domain,ports=ports,processfilterstr="./hddtemp -d",isJSapp=0)
    # 