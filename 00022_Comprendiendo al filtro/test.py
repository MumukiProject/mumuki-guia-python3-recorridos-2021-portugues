
  def test_afortunados_devuelve_los_balances_cuya_ganancia_es_mayor_a_1000(self):
    self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }, { "mes": "mayo", "ganancia": 0 }, { "mes": "junio", "ganancia": -25 }]), [{ "mes": "febrero", "ganancia": 2000 }, { "mes": "marzo", "ganancia": 2500 }, { "mes": "abril", "ganancia": 1001 }])
  
  def test_afortunados_devuelve_una_lista_vacia_si_ningun_balance_tiene_ganancia_mayor_a_1000(self):
    self.assertEqual(afortunados([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": 0 }, { "mes": "marzo", "ganancia": 200 }, { "mes": "abril", "ganancia": -30 }]), [])