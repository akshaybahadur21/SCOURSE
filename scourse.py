from src.etl.etl import performETL
from src.algo.course_similarity import course_sim


class SCOURSE:
    def __init__(self, perFormETL):
        self.perFromETL = perFormETL

    def run(self):
        if self.perFromETL:
            performETL()
        course_sim("Machine Learning")
        course_sim("Product Management")
        course_sim("Software Engineer")
        course_sim("Consultant")


if __name__ == '__main__':
    scourses = SCOURSE(False)
    scourses.run()
