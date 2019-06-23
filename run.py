from app import shell


def main():
    ZenCheckers = shell.Shell()
    ZenCheckers.setup()
    ZenCheckers.run()

if __name__ == '__main__':
    main()
