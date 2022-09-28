
  def test_balanços_positivos_retorna_todos_os_balanços_se_todos_tem_ganho_maior_que_zero(self):
	  self.assertEqual(balanco_positivo([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro": 8 }]), [{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro": 8 }])

  def test_balanços_positivos_exclui_os_balanços_com_ganho_zero(self):
	  self.assertEqual(balanco_positivo([{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }, { "mes": "setembro", "lucro": 0 }]), [{ "mes": "março", "lucro": 10 }, { "mes": "agosto", "lucro": 2 }])

  def test_balanços_positivos_exclui_os_balanços_com_ganho_negativo(self):
	  self.assertEqual(balanco_positivo([{ "mes": "julho", "lucro": 12 }, { "mes": "agosto", "lucro": -2 }]), [{ "mes": "julho", "lucro": 12 }])
 
  def test_balanços_positivos_retorna_a_lista_vazia_se_todos_os_balanços_têm_ganho_zero_ou_menos(self):
	  self.assertEqual(balanco_positivo([{ "mes": "agosto", "lucro": -12 }, { "mes": "setembro", "lucro": 0 }]), [])