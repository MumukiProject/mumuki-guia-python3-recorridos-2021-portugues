
  def test_meses_de_un_trimestre_devuelve_tres_meses(self):
    self.assertEqual(meses([{ "mes": "janeiro", "ganancia": 10 }, { "mes": "fevereiro", "ganancia": 2 }, { "mes": "março", "ganancia": 5 }]), ["janeiro", "fevereiro", "março"])
  
  def test_meses_de_un_semestre_devuelve_seis_meses(self):
    self.assertEqual(meses([{ "mes": "janeiro", "ganancia": 10 }, { "mes": "fevereiro", "ganancia": 2 }, { "mes": "março", "ganancia": 5 }, { "mes": "abril", "ganancia": 8 }, { "mes": "maio", "ganancia": 12 }, { "mes": "junho", "ganancia": 25 }]), ["janeiro", "fevereiro", "março", "abril", "maio", "junho"])