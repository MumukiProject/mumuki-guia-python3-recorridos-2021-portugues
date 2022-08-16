
  def test_los_balances_de_meses_largos_del_primer_semestre_retorna_los_balances_de_enero_marzo_y_mayo(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": -200 }, { "mes": "marzo", "ganancia": 500 }, { "mes": "abril", "ganancia": 800 }, { "mes": "mayo", "ganancia": 770 }, { "mes": "junio", "ganancia": 870 }]), [{ "mes": "enero", "ganancia": 1000 }, { "mes": "marzo", "ganancia": 500 }, { "mes": "mayo", "ganancia": 770 }])

  def test_los_balances_de_meses_largos_del_ultimo_semestre_retorna_los_balances_de_julio_agosto_octubre_y_diciembre(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "julio", "ganancia": 500 }, { "mes": "agosto", "ganancia": 900 }, { "mes": "septiembre", "ganancia": 1800 }, { "mes": "octubre", "ganancia": 900 }, { "mes": "noviembre", "ganancia": 2300 }, { "mes": "diciembre", "ganancia": 2000 }]), [{ "mes": "julio", "ganancia": 500 }, { "mes": "agosto", "ganancia": 900 }, { "mes": "octubre", "ganancia": 900 }, { "mes": "diciembre", "ganancia": 2000 }])

  def test_los_balances_de_meses_largos_del_primer_trimestre_retornan_los_balances_de_enero_y_marzo(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "enero", "ganancia": 1000 }, { "mes": "febrero", "ganancia": -200 }, { "mes": "marzo", "ganancia": 500 }]), [{ "mes": "enero", "ganancia": 1000 }, { "mes": "marzo", "ganancia": 500 }])

  def test_los_balances_de_meses_largos_del_segundo_trimestre_retorna_el_balance_de_mayo(self):
  	self.assertEqual(balances_de_meses_largos([{ "mes": "abril", "ganancia": 800 }, { "mes": "mayo", "ganancia": 770 }, { "mes": "junio", "ganancia": 870 }]), [{ "mes": "mayo", "ganancia": 770 }])