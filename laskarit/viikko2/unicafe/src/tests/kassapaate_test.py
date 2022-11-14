import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.paate = Kassapaate()
        self.kortti = Maksukortti(1000)


    def test_luotu_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.paate, None)

    def test_alkusaldo(self):
        self.assertEqual(self.paate.kassassa_rahaa, 100000)

    def test_edulliset_alkuvarvot(self):
        self.assertEqual(self.paate.edulliset, 0)

    def test_maukkaat_alkuvarvot(self):
        self.assertEqual(self.paate.maukkaat, 0)

    def test_kateisosto_tasaraha_edulliset(self):
        vaihto=self.paate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+240)
        self.assertEqual(vaihto, 0)
        self.assertEqual(self.paate.edulliset, 1)

    def test_kateisosto_edulliset(self):
        vaihto=self.paate.syo_edullisesti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+240)
        self.assertEqual(vaihto, 500-240)
        self.assertEqual(self.paate.edulliset, 1)

    def test_kateisosto_tasaraha_maukkaat(self):
        vaihto=self.paate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+400)
        self.assertEqual(vaihto, 0)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_kateisosto_maukkaat(self):
        vaihto=self.paate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+400)
        self.assertEqual(vaihto, 500-400)
        self.assertEqual(self.paate.maukkaat, 1)

    def test_kateisto_edulliset_raha_ei_riita(self):
        vaihto = self.paate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+0)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(vaihto, 200)

    def test_kateisto_maukkaat_raha_ei_riita(self):
        vaihto = self.paate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+0)
        self.assertEqual(self.paate.maukkaat, 0)
        self.assertEqual(vaihto, 200)

    def test_korttiosto_edulliset(self):
        osto_onnistui = self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(osto_onnistui, True)
        self.assertEqual(self.paate.edulliset, 1)
        self.assertEqual(self.kortti.saldo, 1000-240)

    def test_korttiosto_maukkaat(self):
        osto_onnistui = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(osto_onnistui, True)
        self.assertEqual(self.paate.maukkaat, 1)
        self.assertEqual(self.kortti.saldo, 1000-400)

    def test_korttiosto_edulliset_saldo_ei_riita(self):
        self.kortti = Maksukortti(200)
        osto_onnistui = self.paate.syo_edullisesti_kortilla(self.kortti)
        self.assertEqual(osto_onnistui, False)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.kortti.saldo, 200)


    def test_korttiosto_maukkaat_saldo_ei_riita(self):
        self.kortti = Maksukortti(200)
        osto_onnistui = self.paate.syo_maukkaasti_kortilla(self.kortti)
        self.assertEqual(osto_onnistui, False)
        self.assertEqual(self.paate.edulliset, 0)
        self.assertEqual(self.kortti.saldo, 200)

    def test_lataa_kortille(self):
        self.paate.lataa_rahaa_kortille(self.kortti, 100)
        self.assertEqual(self.kortti.saldo, 1100)
        self.assertEqual(self.paate.kassassa_rahaa, 100000+100)

    def test_lataa_kortille_negatiivinen(self):
        self.paate.lataa_rahaa_kortille(self.kortti, -100)
        self.assertEqual(self.kortti.saldo, 1000)
        self.assertEqual(self.paate.kassassa_rahaa, 100000)
