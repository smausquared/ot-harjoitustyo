import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti
class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_alustus_toimii(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa,100000)
        self.assertEqual(self.kassapaate.edulliset+self.kassapaate.maukkaat,0)
    
    def test_kateisosto_maukkaasti_toimii(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450),50)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200),200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)
        self.assertEqual(self.kassapaate.maukkaat,1)

    def test_kateisosto_edullisesti_toimii(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(280),40)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200),200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
        self.assertEqual(self.kassapaate.edulliset,1)

    def test_korttimaksu_maukkaasti_toimii(self):
        self.kortti = Maksukortti(500)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),True)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kortti.saldo,100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.kortti),False)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kortti.saldo,100)

    def test_korttimaksu_edullisesti_toimii(self):
        self.kortti = Maksukortti(300)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),True)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kortti.saldo,60)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.kortti),False)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kortti.saldo,60)
    
    def test_kortin_lataus_toimii(self):
        self.kortti = Maksukortti(300)
        self.kassapaate.lataa_rahaa_kortille(self.kortti,400)
        self.assertNotEqual(self.kortti.saldo,300)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
        self.kassapaate.lataa_rahaa_kortille(self.kortti,-500)
        self.assertEqual(self.kassapaate.kassassa_rahaa,100400)
