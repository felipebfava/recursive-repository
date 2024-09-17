import os
import threading

# Caminho completo para o arquivo de log
log_file = r"C:\Users\User\OneDrive\Área de Trabalho\threads\access.log"

# Função que processa um intervalo de linhas do log
def process_log_lines(lines):
    hourly_access_count = {}
    status_200_count = 0

    for line in lines:
        parts = line.split()
        if len(parts) > 8:
            timestamp = parts[3][1:]  # Extrai o timestamp (removendo o colchete inicial)
            status_code = parts[8]  # Extrai o código de status (ex: 200, 404)
            
            # Extrai a hora do timestamp
            date_parts = timestamp.split(':')
            if len(date_parts) > 1:
                hour = date_parts[1]  # Obtém a hora do timestamp

                # Conta os acessos por hora
                if hour not in hourly_access_count:
                    hourly_access_count[hour] = 0
                hourly_access_count[hour] += 1

                # Conta as respostas com código de status 200
                if status_code == '200':
                    status_200_count += 1

    return hourly_access_count, status_200_count

# Função que lê e processa o arquivo de log
def process_log_file(log_file):
    with open(log_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    # Divide as linhas do log em partes para multithreading
    num_threads = 4
    chunk_size = len(lines) // num_threads
    threads = []
    results = []

    for i in range(num_threads):
        start_index = i * chunk_size
        if i == num_threads - 1:
            end_index = len(lines)  # Última parte pega todas as linhas restantes
        else:
            end_index = (i + 1) * chunk_size
        
        thread_lines = lines[start_index:end_index]
        thread = threading.Thread(target=lambda q, arg1: q.append(process_log_lines(arg1)), args=(results, thread_lines))
        threads.append(thread)
        thread.start()

    # Aguarda todas as threads terminarem
    for thread in threads:
        thread.join()

    # Combina os resultados de todas as threads
    combined_hourly_access_count = {}
    total_status_200_count = 0

    for hourly_access_count, status_200_count in results:
        total_status_200_count += status_200_count
        for hour, count in hourly_access_count.items():
            if hour not in combined_hourly_access_count:
                combined_hourly_access_count[hour] = 0
            combined_hourly_access_count[hour] += count

    return combined_hourly_access_count, total_status_200_count

# Executa o processamento do arquivo de log
hourly_access_count, total_status_200_count = process_log_file(log_file)

# Exibe os resultados
print("Acessos por hora:", hourly_access_count)
print("Total de respostas com código 200:", total_status_200_count)
