
  def test_los_balances_de_meses_largos_del_primer_semestre_retorna_los_balances_de_enero_marzo_y_mayo(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": -200 }, { "mes": "março", "lucro": 500 }, { "mes": "abril", "lucro": 800 }, { "mes": "maio", "lucro": 770 }, { "mes": "junho", "lucro": 870 }]), [{ "mes": "janeiro", "lucro": 1000 }, { "mes": "março", "lucro": 500 }, { "mes": "maio", "lucro": 770 }])

  def test_los_balances_de_meses_largos_del_ultimo_semestre_retorna_los_balances_de_julio_agosto_octubre_y_diciembre(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "julho", "lucro": 500 }, { "mes": "agosto", "lucro": 900 }, { "mes": "setembro", "lucro": 1800 }, { "mes": "outubro", "lucro": 900 }, { "mes": "novembro", "lucro": 2300 }, { "mes": "dezembro", "lucro": 2000 }]), [{ "mes": "julho", "lucro": 500 }, { "mes": "agosto", "lucro": 900 }, { "mes": "outubro", "lucro": 900 }, { "mes": "dezembro", "lucro": 2000 }])

  def test_los_balances_de_meses_largos_del_primer_trimestre_retornan_los_balances_de_enero_y_marzo(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": -200 }, { "mes": "março", "lucro": 500 }]), [{ "mes": "janeiro", "lucro": 1000 }, { "mes": "março", "lucro": 500 }])

  def test_los_balances_de_meses_largos_del_segundo_trimestre_retorna_el_balance_de_mayo(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "abril", "lucro": 800 }, { "mes": "maio", "lucro": 770 }, { "mes": "junho", "lucro": 870 }]), [{ "mes": "maio", "lucro": 770 }])