
  def test_balances_positivos_devuelve_todos_los_balances_si_todos_tienen_ganancia_mayor_a_cero(self):
	  self.assertEqual(balanco_positivo([{ "mes": "março", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "setembro", "ganancia": 8 }]), [{ "mes": "março", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "setembro", "ganancia": 8 }])

  def test_balances_positivos_excluye_a_los_balances_con_ganancia_cero(self):
	  self.assertEqual(balanco_positivo([{ "mes": "março", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "setembro", "ganancia": 0 }]), [{ "mes": "março", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }])

  def test_balances_positivos_excluye_a_los_balances_con_ganancia_negativa(self):
	  self.assertEqual(balanco_positivo([{ "mes": "julho", "ganancia": 12 }, { "mes": "agosto", "ganancia": -2 }]), [{ "mes": "julho", "ganancia": 12 }])
 
  def test_balances_positivos_devuelve_la_lista_vacia_si_todos_los_balances_tienen_ganancia_de_cero_o_menos(self):
	  self.assertEqual(balanco_positivo([{ "mes": "agosto", "ganancia": -12 }, { "mes": "setembro", "ganancia": 0 }]), [])