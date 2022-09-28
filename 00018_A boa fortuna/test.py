
  def test_afortunados_retorna_os_balanços_cujo_ganho_é_maior_que_1000(self):
    self.assertEqual(sortudo([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": 2000 }, { "mes": "março", "lucro": 2500 }, { "mes": "abril", "lucro": 1001 }, { "mes": "maio", "lucro": 0 }, { "mes": "junho", "lucro": -25 }]), [{ "mes": "fevereiro", "lucro": 2000 }, { "mes": "março", "lucro": 2500 }, { "mes": "abril", "lucro": 1001 }])
  
  def test_afortunados_retorna_uma_lista_vazia_se_nenhum_balanço_tem_ganho_maior_que_1000(self):
    self.assertEqual(sortudo([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": 0 }, { "mes": "março", "lucro": 200 }, { "mes": "abril", "lucro": -30 }]), [])