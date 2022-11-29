class Course:
    def __init__(self, content, done=False, student=None, course_id=None):

        self.content = content
        self.done = done
        self.student = student
        self.id = course_id
