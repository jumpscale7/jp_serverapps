def main(j,jp):

    jp=j.packages.findNewest("jumpscale","osis")
    # jp.load("$(oss.portal.instance)")
    jp.restart()


    jp=j.packages.findNewest("jumpscale","portal")
    jp.load("$(oss.portal.instance)")
    jp.restart()

