
  def test_meses_afortunados_devuelve_los_meses_de_los_balances_afortunados(self):
    self.assertEqual(meses_afortunados([{ "mes": "enero", "ganancia": 1001 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 2300 }, { "mes": "abril", "ganancia": 800 }]), ["enero", "marzo"])
    
  def test_meses_afortunados_devuelve_una_lista_vacia_si_no_hubo_balances_afortunados(self):
    self.assertEqual(meses_afortunados([{ "mes": "enero", "ganancia": 999 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 20 }, { "mes": "abril", "ganancia": 800 }]), [])