
  def test_ganancias_de_los_balances_de_un_periodo_de_tres_meses_me_devuelve_solo_los_valores_de_las_ganancias_de_esos_tres_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "setembro", "ganancia":0 }]), [10, 2, 0])

  def test_ganancias_de_los_balances_de_un_periodo_de_cuatro_meses_me_devuelve_solo_los_valores_de_las_ganancias_de_esos_cuatro_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "ganancia": 10 }, { "mes": "agosto", "ganancia": 2 }, { "mes": "setembro", "ganancia":0 }, { "mes": "dezembro", "ganancia": 8 }]), [10, 2, 0, 8])

  def test_ganancias_de_los_balances_de_un_periodo_de_dos_meses_me_devuelve_solo_los_valores_de_las_ganancias_de_esos_dos_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "ganancia": 8 }, { "mes": "agosto", "ganancia": 7 }]), [8,7])
