
  def test_meses_afortunados_devuelve_los_meses_de_los_balances_afortunados(self):
    self.assertEqual(meses_sortudos([{ "mes": "janeiro", "lucro": 1001 }, { "mes": "fevereiro", "lucro": -10 }, { "mes": "março", "lucro": 2300 }, { "mes": "abril", "lucro": 800 }]), ["janeiro", "março"])
    
  def test_meses_afortunados_devuelve_una_lista_vacia_si_no_hubo_balances_afortunados(self):
    self.assertEqual(meses_sortudos([{ "mes": "enero", "lucro": 999 }, { "mes": "fevereiro", "lucro": -10 }, { "mes": "março", "lucro": 20 }, { "mes": "abril", "lucro": 800 }]), [])