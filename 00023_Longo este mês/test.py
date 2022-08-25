
  def test_los_balances_de_meses_largos_del_primer_semestre_retorna_los_balances_de_enero_marzo_y_mayo(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "janeiro", "ganancia": 1000 }, { "mes": "fevereiro", "ganancia": -200 }, { "mes": "março", "ganancia": 500 }, { "mes": "abril", "ganancia": 800 }, { "mes": "maio", "ganancia": 770 }, { "mes": "junho", "ganancia": 870 }]), [{ "mes": "janeiro", "ganancia": 1000 }, { "mes": "março", "ganancia": 500 }, { "mes": "maio", "ganancia": 770 }])

  def test_los_balances_de_meses_largos_del_ultimo_semestre_retorna_los_balances_de_julio_agosto_octubre_y_diciembre(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "julho", "ganancia": 500 }, { "mes": "agosto", "ganancia": 900 }, { "mes": "setembro", "ganancia": 1800 }, { "mes": "outubro", "ganancia": 900 }, { "mes": "novembro", "ganancia": 2300 }, { "mes": "dezembro", "ganancia": 2000 }]), [{ "mes": "julho", "ganancia": 500 }, { "mes": "agosto", "ganancia": 900 }, { "mes": "outubro", "ganancia": 900 }, { "mes": "dezembro", "ganancia": 2000 }])

  def test_los_balances_de_meses_largos_del_primer_trimestre_retornan_los_balances_de_enero_y_marzo(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "janeiro", "ganancia": 1000 }, { "mes": "fevereiro", "ganancia": -200 }, { "mes": "março", "ganancia": 500 }]), [{ "mes": "janeiro", "ganancia": 1000 }, { "mes": "março", "ganancia": 500 }])

  def test_los_balances_de_meses_largos_del_segundo_trimestre_retorna_el_balance_de_mayo(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "abril", "ganancia": 800 }, { "mes": "maio", "ganancia": 770 }, { "mes": "junho", "ganancia": 870 }]), [{ "mes": "maio", "ganancia": 770 }])