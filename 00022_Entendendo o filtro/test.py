
  def test_afortunados_devuelve_los_balances_cuya_ganancia_es_mayor_a_1000(self):
    self.assertEqual(sortudo([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": 2000 }, { "mes": "março", "lucro": 2500 }, { "mes": "abril", "lucro": 1001 }, { "mes": "maio", "lucro": 0 }, { "mes": "junho", "lucro": -25 }]), [{ "mes": "fevereiro", "lucro": 2000 }, { "mes": "março", "lucro": 2500 }, { "mes": "abril", "lucro": 1001 }])
  
  def test_afortunados_devuelve_una_lista_vacia_si_ningun_balance_tiene_ganancia_mayor_a_1000(self):
    self.assertEqual(sortudo([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": 0 }, { "mes": "março", "lucro": 200 }, { "mes": "abril", "lucro": -30 }]), [])