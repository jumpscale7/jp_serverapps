def main(j,jp):
   
    jp=j.packages.findNewest("jumpscale","portal")
    jp.load("$(cloudrobot.portal.instance)")
    jp.restart()
