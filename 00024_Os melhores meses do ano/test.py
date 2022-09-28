
  def test_meses_sortudos_retorna_os_meses_dos_balanços_sortudos(self):
    self.assertEqual(meses_sortudos([{ "mes": "janeiro", "lucro": 1001 }, { "mes": "fevereiro", "lucro": -10 }, { "mes": "março", "lucro": 2300 }, { "mes": "abril", "lucro": 800 }]), ["janeiro", "março"])
    
  def test_meses_sortudos_retorna_uma_lista_vazia_se_não_houve_balanços_afortunados(self):
    self.assertEqual(meses_sortudos([{ "mes": "janeiro", "lucro": 999 }, { "mes": "fevereiro", "lucro": -10 }, { "mes": "março", "lucro": 20 }, { "mes": "abril", "lucro": 800 }]), [])