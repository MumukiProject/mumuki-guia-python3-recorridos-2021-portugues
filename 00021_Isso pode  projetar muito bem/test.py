  
  def test_o_dobro_de_ganhos_de_uma_lista_de_balanços_retorna_o_dobro_dos_ganhos(self):
    self.assertEqual(dobro_do_lucro([{ "mes": "janeiro", "lucro": 1000 }, { "mes": "fevereiro", "lucro": -200 }, { "mes": "março", "lucro": 500 }]), [2000, -400, 1000])
  
  def test_o_dobro_de_ganhos_de_uma_lista_de_balanços_negativos_retorna_uma_lista_de_números_negativos_o_dobro_dos_negativos(self):
    self.assertEqual(dobro_do_lucro([{ "mes": "janeiro", "lucro": -1000 }, { "mes": "fevereiro", "lucro": -200 }, { "mes": "março", "lucro": -500 }]), [-2000, -400, -1000])

  def test_o_dobro_de_ganhos_de_uma_lista_de_balanços_com_ganho_zero_retorna_uma_lista_de_zeros(self):
    self.assertEqual(dobro_do_lucro([{ "mes": "janeiro", "lucro": 0 }, { "mes": "fevereiro", "lucro": 0 }]), [0, 0])