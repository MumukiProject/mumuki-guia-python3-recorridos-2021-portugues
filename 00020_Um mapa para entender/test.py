
  def test_meses_de_un_trimestre_devuelve_tres_meses(self):
    self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }]), ["enero", "febrero", "marzo"])
  
  def test_meses_de_un_semestre_devuelve_seis_meses(self):
    self.assertEqual(meses([{ "mes": "enero", "ganancia": 10 }, { "mes": "febrero", "ganancia": 2 }, { "mes": "marzo", "ganancia": 5 }, { "mes": "abril", "ganancia": 8 }, { "mes": "mayo", "ganancia": 12 }, { "mes": "junio", "ganancia": 25 }]), ["enero", "febrero", "marzo", "abril", "mayo", "junio"])