class Course:
    """Luokka, joka kuvaa yksittäistä kurssia
    Attributes:
        content: Merkkijonoarvo, joka kuvaa kurssin sisältöä.
        done: Boolean-arvo, joka kuvastaa, onko kurssi jo suoritettu.
        student: Student-olio, joka kuvaa kurssin suorittajaa.
        course_id: Merkkijonoarvo, joku kuvaa kurssin id:tä.
    """
    def __init__(self, content, done=False, student=None, course_id=None):
        """Luokan konstruktori, joka luo uuden kurssin.
        Args:
            content: Merkkijonoarvo, joka kuvaa kurssin sisältöä.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko kurssi jo suoritettu.
            student:
                Vapaaehtoinen, oletusarvoltaan None.
                Student-olio, joka kuvaa kurssin suorittajaa.
            course_id:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joku kuvaa kurssin id:tä.
        """
        self.content = content
        self.done = done
        self.student = student
        self.id = course_id
