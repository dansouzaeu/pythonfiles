import os

def split_file(file_path):
    # Defina o número de linhas em cada parte
    lines_per_file = 1000000

    # Defina o nome base para cada parte
    base_name = os.path.splitext(file_path)[0]

    with open(file_path, 'r') as input_file:
        # Ignora a primeira linha, caso seja um cabeçalho
        header = input_file.readline()

        # Cria a primeira parte
        part_num = 1
        output_file = open(f'{base_name}_part{part_num}.txt', 'w')
        output_file.write(header)

        # Conta o número de linhas na parte atual
        current_lines = 0

        for line in input_file:
            # Escreve a linha atual na parte atual
            output_file.write(line)

            # Incrementa o número de linhas na parte atual
            current_lines += 1

            # Se atingir o número máximo de linhas por parte, cria uma nova parte
            if current_lines == lines_per_file:
                # Fecha a parte atual
                output_file.close()

                # Cria a próxima parte
                part_num += 1
                output_file = open(f'{base_name}_part{part_num}.txt', 'w')
                output_file.write(header)

                # Reinicia o contador de linhas na parte atual
                current_lines = 0

        # Fecha a última parte
        output_file.close()

if __name__ == '__main__':
    file_path = 'TB_PMTFIL_VIVO2.csv'
    split_file(file_path)
