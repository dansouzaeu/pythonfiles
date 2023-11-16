def substituir_virgulas_por_ponto_virgula(nome_arquivo):
    # Abrir o arquivo para leitura
    with open(nome_arquivo, 'r') as arquivo:
        conteudo = arquivo.read()

    # Substituir as vírgulas por ponto e vírgula
    conteudo_modificado = conteudo.replace(',', ';')

    # Abrir o arquivo para escrita e salvar o conteúdo modificado
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write(conteudo_modificado)

    print(f"As vírgulas no arquivo {nome_arquivo} foram substituídas por ponto e vírgula.")


# Exemplo de uso
nome_arquivo = "TB_PMTFIL_VIVO2_part5.txt"  # Substitua pelo nome do seu arquivo
substituir_virgulas_por_ponto_virgula(nome_arquivo)