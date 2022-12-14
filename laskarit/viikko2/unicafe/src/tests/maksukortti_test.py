import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_lataus_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(200)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 12.00 euroa")

    def test_saldo_vahenee_oikein(self):
        self.maksukortti.ota_rahaa(300)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1100)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_ota_rahaa_palauttaa_true(self):
        self.assertEqual(self.maksukortti.ota_rahaa(300), True)

    def test_ota_rahaa_palauttaa_false(self):
        self.assertEqual(self.maksukortti.ota_rahaa(1100), False)
