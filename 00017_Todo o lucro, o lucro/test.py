  
  def test_ganancia_total_de_balances_del_primer_trimestre_es_menos_8(self):
    self.assertEqual(ganancia_total([{ "mes": "janeiro", "lucro": 2 }, { "mes": "fevereiro", "lucro": 10 }, { "mes": "março", "lucro": -20 }]), -8)
  
  def test_ganancia_total_de_balances_del_ultimo_semestre_es_1538(self):
    self.assertEqual(ganancia_total([{ "mes": "julho", "lucro": 50 }, { "mes": "agosto", "lucro": -12 }, { "mes": "setembro", "lucro": 1000 }, { "mes": "outubro", "lucro": 300 }, { "mes":  "novembro", "lucro": 200 }, { "mes": "dezembro", "lucro": 0 }]), 1538)