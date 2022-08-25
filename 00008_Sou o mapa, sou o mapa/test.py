
  def test_ganancias_de_los_balances_de_un_periodo_de_tres_meses_me_devuelve_solo_los_valores_de_las_ganancias_de_esos_tres_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro":0 }]), [10, 2, 0])

  def test_ganancias_de_los_balances_de_un_periodo_de_cuatro_meses_me_devuelve_solo_los_valores_de_las_ganancias_de_esos_cuatro_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro":0 }, { "mes": "dezembro", "lucro": 8 }]), [10, 2, 0, 8])

  def test_ganancias_de_los_balances_de_un_periodo_de_dos_meses_me_devuelve_solo_los_valores_de_las_ganancias_de_esos_dos_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "lucro": 8 }, { "mes": "agosto", "lucro": 7 }]), [8,7])
