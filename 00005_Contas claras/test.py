
  def test_quantidade_de_balanços_positivos_com_uma_lista_com_apenas_um_balanço_positivo_é_um(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "novembro", "lucro": 5 }]), 1)

  def test_quantidade_de_balanços_positivos_com_uma_lista_com_dois_balanços_positivos_é_dois(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "março", "lucro": 8 }, { "mes": "agosto", "lucro": 10 }]), 2)

  def test_quantidade_de_balanços_positivos_da_lista_vazia_é_zero(self):
    self.assertEqual(quantidade_de_balancos_positivos([]), 0)

  def test_quantidade_de_balanços_positivos_quando_todos_os_balanços_tiveram_ganho_zero_é_zero(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "março", "lucro": 0 }, { "mes": "agosto", "lucro": 0 }]), 0)

  def test_quantidade_de_balanços_positivos_com_três_balanços_positivos_e_um_negativo_da_três(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "janeiro", "lucro": 10 }, { "mes": "fevereiro", "lucro": -10 }, { "mes": "março", "lucro": 2 }, { "mes": "abril", "lucro": 100 }]), 3)
  
  def test_quantidade_de_balanços_positivos_quando_todos_os_meses_têm_ganho_negativo_é_zero(self):
    self.assertEqual(quantidade_de_balancos_positivos([{ "mes": "janeiro", "lucro": -1 }, { "mes": "fevereiro", "lucro": -2 }, { "mes": "março", "lucro": -3 }]), 0)
