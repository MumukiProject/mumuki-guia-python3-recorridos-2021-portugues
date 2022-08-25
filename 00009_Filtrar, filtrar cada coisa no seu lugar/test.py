
  def test_balances_positivos_devuelve_todos_los_balances_si_todos_tienen_ganancia_mayor_a_cero(self):
	  self.assertEqual(balanco_positivo([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro": 8 }]), [{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro": 8 }])

  def test_balances_positivos_excluye_a_los_balances_con_ganancia_cero(self):
	  self.assertEqual(balanco_positivo([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro": 0 }]), [{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }])

  def test_balances_positivos_excluye_a_los_balances_con_ganancia_negativa(self):
	  self.assertEqual(balanco_positivo([{ "mes": "julho", "lucro": 12 }, { "mes": "agosto", "lucro": -2 }]), [{ "mes": "julho", "lucro": 12 }])
 
  def test_balances_positivos_devuelve_la_lista_vacia_si_todos_los_balances_tienen_ganancia_de_cero_o_menos(self):
	  self.assertEqual(balanco_positivo([{ "mes": "agosto", "lucro": -12 }, { "mes": "setembro", "lucro": 0 }]), [])