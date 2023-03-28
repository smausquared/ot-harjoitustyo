import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.kortti = Maksukortti(1000)

    def test_syo_maukkaasti_ei_vie_saldoa_negatiiviseksi(self):
        kortti = Maksukortti(200)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_negatiivinen_lataus_ei_muuta_mitaan(self):
        kortti = Maksukortti(200)
        kortti.lataa_rahaa(-500)

        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_voi_maksaa_edullisen_tasarahalla(self):
        kortti = Maksukortti(250)
        kortti.syo_edullisesti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

    def test_voi_maksaa_maukkaan_tasarahalla(self):
        kortti = Maksukortti(400)
        kortti.syo_maukkaasti()

        self.assertEqual(str(kortti), "Kortilla on rahaa 0.00 euroa")

