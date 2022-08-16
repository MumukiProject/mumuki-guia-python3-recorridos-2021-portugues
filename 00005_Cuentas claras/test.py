
  def test_cantidad_de_balances_positivos_con_una_lista_con_un_solo_balance_positivo_es_uno(self):
    self.assertEqual(cantidad_de_balances_positivos([{ "mes": "noviembre", "ganancia": 5 }]), 1)

  def test_cantidad_de_balances_positivos_con_una_lista_con_dos_balances_positivos_es_dos(self):
    self.assertEqual(cantidad_de_balances_positivos([{ "mes": "marzo", "ganancia": 8 }, { "mes": "agosto", "ganancia": 10 }]), 2)

  def test_cantidad_de_balances_positivos_de_la_lista_vacia_es_cero(self):
    self.assertEqual(cantidad_de_balances_positivos([]), 0)

  def test_cantidad_de_balances_positivos_cuando_todos_los_balances_tuvieron_ganancia_cero_es_cero(self):
    self.assertEqual(cantidad_de_balances_positivos([{ "mes": "marzo", "ganancia": 0 }, { "mes": "agosto", "ganancia": 0 }]), 0)

  def test_cantidad_de_balances_positivos_con_tres_balances_positivos_y_uno_negativo_da_tres(self):
    self.assertEqual(cantidad_de_balances_positivos([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": -10 }, { "mes": "marzo", "ganancia": 2 }, { "mes": "abril", "ganancia": 100 }]), 3)
  
  def test_cantidad_de_balances_positivos_cuando_todos_los_meses_tienen_ganancia_negativa_es_cero(self):
    self.assertEqual(cantidad_de_balances_positivos([{ "mes": "enero", "ganancia": -1 }, { "mes": "febrero", "ganancia": -2 }, { "mes": "marzo", "ganancia": -3 }]), 0)
