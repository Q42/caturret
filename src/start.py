from motion_detector import monitor


def main():
    monitor(on_target)


def on_target(target):
    print "target=%s" % str(target)


if __name__ == "__main__":
    main()
