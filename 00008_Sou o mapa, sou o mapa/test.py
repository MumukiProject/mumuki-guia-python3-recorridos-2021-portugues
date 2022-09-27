
  def test_ganhos_dos_balanços_de_um_período_de_três_meses_retorna_apenas_os_valores_dos_ganhos_desses_três_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro":0 }]), [10, 2, 0])

  def test_ganhos_dos_balanços_de_um_período_de_quatro_meses_retorna_apenas_os_valores_dos_ganhos_desses_quatro_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro":0 }, { "mes": "dezembro", "lucro": 8 }]), [10, 2, 0, 8])

  def test_ganhos_dos_balanços_de_um_período_de_dois_meses_retorna_apenas_os_valores_dos_ganhos_desses_dois_meses(self):
	  self.assertEqual(lucros([{ "mes": "março", "lucro": 8 }, { "mes": "agosto", "lucro": 7 }]), [8,7])
