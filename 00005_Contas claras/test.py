
  def test_cantidad_de_balances_positivos_con_una_lista_con_un_solo_balance_positivo_es_uno(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "novembro", "lucro": 5 }]), 1)

  def test_cantidad_de_balances_positivos_con_una_lista_con_dos_balances_positivos_es_dos(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "março", "lucro": 8 }, { "mes": "agosto", "lucro": 10 }]), 2)

  def test_cantidad_de_balances_positivos_de_la_lista_vacia_es_cero(self):
    self.assertEqual(quantidade_de_balancos_positivos([]), 0)

  def test_cantidad_de_balances_positivos_cuando_todos_los_balances_tuvieron_ganancia_cero_es_cero(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "março", "lucro": 0 }, { "mes": "agosto", "lucro": 0 }]), 0)

  def test_cantidad_de_balances_positivos_con_tres_balances_positivos_y_uno_negativo_da_tres(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "janeiro", "lucro": 10 }, { "mes": "fevereiro", "lucro": -10 }, { "mes": "março", "lucro": 2 }, { "mes": "abril", "lucro": 100 }]), 3)
  
  def test_cantidad_de_balances_positivos_cuando_todos_los_meses_tienen_ganancia_negativa_es_cero(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "janeiro", "lucro": -1 }, { "mes": "fevereiro", "lucro": -2 }, { "mes": "março", "lucro": -3 }]), 0)
