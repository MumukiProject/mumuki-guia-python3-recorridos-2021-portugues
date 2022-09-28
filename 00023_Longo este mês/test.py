
  def test_os_balanços_de_meses_longos_do_primeiro_semestre_retorna_os_balanços_de_janeiro_março_e_maio(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": -200 }, { "mes": "março", "lucro": 500 }, { "mes": "abril", "lucro": 800 }, { "mes": "maio", "lucro": 770 }, { "mes": "junho", "lucro": 870 }]), [{ "mes": "janeiro", "lucro": 1000 }, { "mes": "março", "lucro": 500 }, { "mes": "maio", "lucro": 770 }])

  def test_os_balanços_de_meses_longos_do_último_semestre_retorna_os_balanços_de_julho_agosto_outubro_e_dezembro(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "julho", "lucro": 500 }, { "mes": "agosto", "lucro": 900 }, { "mes": "setembro", "lucro": 1800 }, { "mes": "outubro", "lucro": 900 }, { "mes": "novembro", "lucro": 2300 }, { "mes": "dezembro", "lucro": 2000 }]), [{ "mes": "julho", "lucro": 500 }, { "mes": "agosto", "lucro": 900 }, { "mes": "outubro", "lucro": 900 }, { "mes": "dezembro", "lucro": 2000 }])

  def test_os_balanços_de_meses_longos_do_primeiro_trimestre_retornam_os_balanços_de_janiero_e_março(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": -200 }, { "mes": "março", "lucro": 500 }]), [{ "mes": "janeiro", "lucro": 1000 }, { "mes": "março", "lucro": 500 }])

  def test_os_balanços_de_meses_longos_do_segundo_trimestre_retorna_o_balanço_de_maio(self):
  	self.assertEqual(balancos_de_meses_longos([{ "mes": "abril", "lucro": 800 }, { "mes": "maio", "lucro": 770 }, { "mes": "junho", "lucro": 870 }]), [{ "mes": "maio", "lucro": 770 }])