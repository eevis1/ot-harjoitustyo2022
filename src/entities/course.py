class Course:
    """Luokka, joka kuvaa yksittäistä kurssia
    Attributes:
        content: Merkkijonoarvo, joka kertoo kurssin nimen.
        done: Boolean-arvo, joka kuvastaa, onko kurssi jo suoritettu.
        course_id: Merkkijonoarvo, joku kuvaa kurssin id:tä.
    """
    def __init__(self, name, done=False, course_id=None):
        """Luokan konstruktori, joka luo uuden kurssin.
        Args:
            content: Merkkijonoarvo, joka kertoo kurssin nimen.
            done:
                Vapaaehtoinen, oletusarvoltaan False.
                Boolean-arvo, joka kuvastaa, onko kurssi jo suoritettu.
            course_id:
                Vapaaehtoinen, oletusarvoltaan None.
                Merkkijonoarvo, joku kuvaa kurssin id:tä.
        """
        self.name = name
        self.done = done
        self.id = course_id
