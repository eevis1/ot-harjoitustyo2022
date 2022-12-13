class Student:
    """Luokka, joka kuvaa yksittäistä opiskelijaa.
    Attributes:
        username: Merkkijonoarvo, joka kuvaa opiskelijan käyttäjätunnusta.
        password: Merkkijonoarvo, joka kuvaa opiskelijan salasanaa.
    """
    def __init__(self, username, password):
        """Luokan konstruktori, joka luo uuden opiskelijan.
        Args:
            username: Merkkijonoarvo, joka kuvaa opiskelijan käyttäjätunnusta.
            password: Merkkijonoarvo, joka kuvaa opiskelijan salasanaa.
        """

        self.username = username
        self.password = password
