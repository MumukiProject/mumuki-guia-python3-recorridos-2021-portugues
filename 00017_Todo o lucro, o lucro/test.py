  
  def test_ganho_total_de_balanços_do_primeiro_trimestre_é_menos_8(self):
    self.assertEqual(lucro_total([{ "mes": "janeiro", "lucro": 2 }, { "mes": "fevereiro", "lucro": 10 }, { "mes": "março", "lucro": -20 }]), -8)
  
  def test_ganho_total_de_balanços_do_último_semestre_é_1538(self):
    self.assertEqual(lucro_total([{ "mes": "julho", "lucro": 50 }, { "mes": "agosto", "lucro": -12 }, { "mes": "setembro", "lucro": 1000 }, { "mes": "outubro", "lucro": 300 }, { "mes":  "novembro", "lucro": 200 }, { "mes": "dezembro", "lucro": 0 }]), 1538)