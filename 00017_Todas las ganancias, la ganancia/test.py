  
  def test_ganancia_total_de_balances_del_primer_trimestre_es_menos_8(self):
    self.assertEqual(ganancia_total([{ "mes": "enero", "ganancia": 2 }, { "mes": "febrero", "ganancia": 10 }, { "mes": "marzo", "ganancia": -20 }]), -8)
  
  def test_ganancia_total_de_balances_del_ultimo_semestre_es_1538(self):
    self.assertEqual(ganancia_total([{ "mes": "julio", "ganancia": 50 }, { "mes": "agosto", "ganancia": -12 }, { "mes": "septiembre", "ganancia": 1000 }, { "mes": "octubre", "ganancia": 300 }, { "mes":  "noviembre", "ganancia": 200 }, { "mes": "diciembre", "ganancia": 0 }]), 1538)