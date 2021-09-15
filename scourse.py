from src.etl.etl import performETL


class SCOURSE:
    def __init__(self, perFormETL):
        self.perFromETL = perFormETL

    def run(self):
        if self.perFromETL:
            performETL()
        # TODO : rest of the implementation


if __name__ == '__main__':
    scourses = SCOURSE(True)
    scourses.run()
