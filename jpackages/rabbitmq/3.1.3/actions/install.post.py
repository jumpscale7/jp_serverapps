def main(j,jp):
   
    #copying of files is not done in this step
    # the order is:
    # first do prepare
    # then the system automatically copies (if not in debug) starting from the files section of the jpackage
    # then do this tasklet (postinstall)

    #shortcut to some usefull install tools
    #do=j.system.installtools

    #configuration is not done in this step !!!!!
    #preparation like system preps like ubuntu deb installs also not done here
    
    j.dirs.replaceFilesDirVars("$base/apps/rabbitmq/sbin")
    j.dirs.replaceFilesDirVars("$base/cfg/rabbitmq")
    

    j.system.fs.createDir("$base/cfg/rabbitmq")
    j.system.fs.createDir("$base/var/log/rabbitmq")
    j.system.fs.createDir("$base/var/rabbitmq")
    j.system.fs.createDir("$base/cfg/rabbitmq/enabled_plugins")


