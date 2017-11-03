from motion_detector import monitor


def main():
    monitor(on_target)


def on_target(target):
    print "target=%s" % str(target)
    # lightUpEyes()
    # moveSteppers(x, y)
    # releaseRelais()
    # makeNoise("mwuHahaha")
    # closeRelais()
    # returnSteppers()
    # closeEyes()


if __name__ == "__main__":
    main()
