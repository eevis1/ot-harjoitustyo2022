import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):

    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(400)
        self.kortti = Maksukortti(200)

    def test_luodun_kassapaatteen_rahamaara_oikea(self):
        
        self.kassapaate.kassassa_rahaa == 100000

    def test_luodun_kassapaatteen_myytyjen_lounaiden_maara_oikea(self):
        self.kassapaate.edulliset == 0
        self.kassapaate.maukkaat == 0


    def test_kateisosto_toimii_edulliset(self):
        self.kassapaate.syo_edullisesti_kateisella(1000) == 730
        self.kassapaate.kassassa_rahaa == 100240
        self.kassapaate.edulliset == 1

        self.kassapaate.syo_edullisesti_kateisella(200) == 200
        self.kassapaate.kassassa_rahaa == 100000
        self.kassapaate.edulliset == 0


    def test_kateisosto_toimii_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kateisella(1000) == 600
        self.kassapaate.kassassa_rahaa == 100400
        self.kassapaate.maukkaat == 1

        self.kassapaate.syo_maukkaasti_kateisella(200) == 200
        self.kassapaate.kassassa_rahaa == 100000
        self.kassapaate.maukkaat == 0



    def test_korttiosto_toimii_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) == True
        self.maksukortti == 160
        self.kassapaate.edulliset == 1

        self.kassapaate.syo_edullisesti_kortilla(self.kortti) == False
        self.kortti == 200
        self.kassapaate.edulliset == 0

    def test_korttiosto_toimii_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) == True
        self.maksukortti == 0
        self.kassapaate.edulliset == 1

        self.kassapaate.syo_maukkaasti_kortilla(self.kortti) == False
        self.kortti == 200
        self.kassapaate.maukkaat == 0

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_ja_kassassa_oleva_rahamaara_kasvaa_ladatulla_summalla(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100) 
        self.maksukortti == 500
        self.kassapaate.kassassa_rahaa == 100100

        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100) 
        self.maksukortti == 400
        self.kassapaate.kassassa_rahaa == 100000

    





