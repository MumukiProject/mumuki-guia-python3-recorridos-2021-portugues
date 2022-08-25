  
  def test_el_doble_de_ganancias_de_una_lista_de_balances_retorna_el_doble_de_sus_ganancias(self):
    self.assertEqual(dobro_do_lucro([{ "mes": "janeiro", "ganancia": 1000 }, { "mes": "fevereiro", "ganancia": -200 }, { "mes": "março", "ganancia": 500 }]), [2000, -400, 1000])
  
  def test_el_doble_de_ganancias_de_una_lista_de_balances_negativos_retorna_una_lista_de_numeros_negativos_el_doble_de_los_negativos(self):
    self.assertEqual(dobro_do_lucro([{ "mes": "janeiro", "ganancia": -1000 }, { "mes": "fevereiro", "ganancia": -200 }, { "mes": "março", "ganancia": -500 }]), [-2000, -400, -1000])

  def test_el_doble_de_ganancias_de_una_lista_de_balances_con_ganancia_cero_retorna_una_lista_de_ceros(self):
    self.assertEqual(dobro_do_lucro([{ "mes": "janeiro", "ganancia": 0 }, { "mes": "fevereiro", "ganancia": 0 }]), [0, 0])