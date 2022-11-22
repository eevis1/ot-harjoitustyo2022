class Course:
    def __init__(self, content, done=False, user=None, course_id=None):

        self.content = content
        self.done = done
        self.user = user
        self.id = course_id