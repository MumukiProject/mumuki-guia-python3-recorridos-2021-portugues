
  def test_meses_de_um_trimestre_retorna_três_meses(self):
    self.assertEqual(meses([{ "mes": "janeiro", "lucro": 10 }, { "mes": "fevereiro", "lucro": 2 }, { "mes": "março", "lucro": 5 }]), ["janeiro", "fevereiro", "março"])
  
  def test_meses_de_um_semestre_retorna_seis_meses(self):
    self.assertEqual(meses([{ "mes": "janeiro", "lucro": 10 }, { "mes": "fevereiro", "lucro": 2 }, { "mes": "março", "lucro": 5 }, { "mes": "abril", "lucro": 8 }, { "mes": "maio", "lucro": 12 }, { "mes": "junho", "lucro": 25 }]), ["janeiro", "fevereiro", "março", "abril", "maio", "junho"])