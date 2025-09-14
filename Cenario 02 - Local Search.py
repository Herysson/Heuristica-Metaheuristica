import copy

# --- Dados do Problema (Cenário 02 - 2M 10P) ---
# (Mesmos dados da etapa anterior)
processing_times = {
    1: 28, 2: 15, 3: 35, 4: 22, 5: 40,
    6: 18, 7: 25, 8: 30, 9: 12, 10: 20
}
setup_matrix = {
    '0': {1: 50, 2: 47, 3: 50, 4: 42, 5: 25, 6: 49, 7: 22, 8: 22, 9: 45, 10: 11},
    1: {1: 0, 2: 65, 3: 92, 4: 71, 5: 29, 6: 92, 7: 58, 8: 51, 9: 89, 10: 57},
    2: {2: 0, 1: 65, 3: 75, 4: 96, 5: 41, 6: 56, 7: 32, 8: 68, 9: 89, 10: 47},
    3: {3: 0, 1: 92, 2: 75, 4: 71, 5: 74, 6: 25, 7: 51, 8: 58, 9: 40, 10: 40},
    4: {4: 0, 1: 71, 2: 96, 3: 71, 5: 59, 6: 86, 7: 72, 8: 28, 9: 38, 10: 56},
    5: {5: 0, 1: 29, 2: 41, 3: 74, 4: 59, 6: 67, 7: 29, 8: 38, 9: 70, 10: 34},
    6: {6: 0, 1: 92, 2: 56, 3: 25, 4: 86, 5: 67, 7: 39, 8: 66, 9: 34, 10: 38},
    7: {7: 0, 1: 58, 2: 32, 3: 51, 4: 72, 5: 29, 6: 39, 8: 36, 9: 60, 10: 18},
    8: {8: 0, 1: 51, 2: 68, 3: 58, 4: 28, 5: 38, 6: 66, 7: 36, 9: 41, 10: 30},
    9: {9: 0, 1: 89, 2: 89, 3: 40, 4: 38, 5: 70, 6: 34, 7: 60, 8: 41, 10: 43},
    10: {10: 0, 1: 57, 2: 47, 3: 40, 4: 56, 5: 34, 6: 38, 7: 18, 8: 30, 9: 43}
}
release_dates = {
    1: 0, 2: 20, 3: 10, 4: 0, 5: 35,
    6: 50, 7: 15, 8: 60, 9: 5, 10: 45
}

# --- Funções Auxiliares ---
def calculate_sequence_time(sequence, processing_times, setup_matrix, release_dates=None):
    """Calcula o tempo total de conclusão para uma dada sequência de tarefas em uma máquina."""
    completion_time = 0
    last_task = '0'
    if not sequence:
        return 0
    
    for task_id in sequence:
        start_time = completion_time
        if release_dates:
            start_time = max(completion_time, release_dates[task_id])
        
        setup_time = setup_matrix[last_task][task_id]
        proc_time = processing_times[task_id]
        completion_time = start_time + setup_time + proc_time
        last_task = task_id
        
    return completion_time

# --- Algoritmo Construtivo FFD (da etapa anterior) ---
def solve_with_ffd(processing_times, setup_matrix, release_dates=None):
    sorted_tasks = sorted(processing_times.keys(), key=lambda task: processing_times[task], reverse=True)
    machines = {
        1: {'sequence': [], 'completion_time': 0, 'last_task': '0'},
        2: {'sequence': [], 'completion_time': 0, 'last_task': '0'}
    }
    for task_id in sorted_tasks:
        potential_times = {}
        for machine_id in machines:
            # Simula a adição da tarefa à sequência atual
            temp_sequence = machines[machine_id]['sequence'] + [task_id]
            potential_times[machine_id] = calculate_sequence_time(temp_sequence, processing_times, setup_matrix, release_dates)
        
        best_machine = min(potential_times, key=potential_times.get)
        machines[best_machine]['sequence'].append(task_id)
        # Atualiza o tempo e a última tarefa (embora o tempo não seja mais usado aqui)
        machines[best_machine]['completion_time'] = potential_times[best_machine]
        machines[best_machine]['last_task'] = task_id
        
    # Retorna apenas as sequências, pois os tempos serão recalculados
    final_sequences = {m_id: data['sequence'] for m_id, data in machines.items()}
    return final_sequences

# --- Algoritmo de Busca Local ---
def local_search(initial_sequences, processing_times, setup_matrix, release_dates=None):
    """
    Aplica a busca local para tentar melhorar uma solução inicial.
    """
    current_solution = initial_sequences
    
    # Calcula o makespan inicial
    time1 = calculate_sequence_time(current_solution[1], processing_times, setup_matrix, release_dates)
    time2 = calculate_sequence_time(current_solution[2], processing_times, setup_matrix, release_dates)
    current_makespan = max(time1, time2)
    
    iteration = 0
    while True:
        iteration += 1
        print(f"\n--- Iteração {iteration} da Busca Local ---")
        best_neighbor_solution = None
        best_neighbor_makespan = current_makespan

        # Vizinhança 1: Transferência (mover tarefa de uma máquina para outra)
        for m_from in [1, 2]:
            m_to = 2 if m_from == 1 else 1
            for i in range(len(current_solution[m_from])):
                neighbor = copy.deepcopy(current_solution)
                task_to_move = neighbor[m_from].pop(i)
                neighbor[m_to].append(task_to_move)
                
                t1 = calculate_sequence_time(neighbor[1], processing_times, setup_matrix, release_dates)
                t2 = calculate_sequence_time(neighbor[2], processing_times, setup_matrix, release_dates)
                neighbor_makespan = max(t1, t2)
                
                if neighbor_makespan < best_neighbor_makespan:
                    best_neighbor_makespan = neighbor_makespan
                    best_neighbor_solution = neighbor

        # Vizinhança 2: Troca Inter-Máquinas (trocar tarefa entre máquinas)
        for i in range(len(current_solution[1])):
            for j in range(len(current_solution[2])):
                neighbor = copy.deepcopy(current_solution)
                task1 = neighbor[1][i]
                task2 = neighbor[2][j]
                neighbor[1][i], neighbor[2][j] = task2, task1 # Troca
                
                t1 = calculate_sequence_time(neighbor[1], processing_times, setup_matrix, release_dates)
                t2 = calculate_sequence_time(neighbor[2], processing_times, setup_matrix, release_dates)
                neighbor_makespan = max(t1, t2)
                
                if neighbor_makespan < best_neighbor_makespan:
                    best_neighbor_makespan = neighbor_makespan
                    best_neighbor_solution = neighbor

        # Vizinhança 3: Troca Intra-Máquina (trocar tarefas na mesma máquina)
        for m_id in [1, 2]:
            seq_len = len(current_solution[m_id])
            if seq_len < 2: continue
            for i in range(seq_len):
                for j in range(i + 1, seq_len):
                    neighbor = copy.deepcopy(current_solution)
                    neighbor[m_id][i], neighbor[m_id][j] = neighbor[m_id][j], neighbor[m_id][i] # Troca
                    
                    t1 = calculate_sequence_time(neighbor[1], processing_times, setup_matrix, release_dates)
                    t2 = calculate_sequence_time(neighbor[2], processing_times, setup_matrix, release_dates)
                    neighbor_makespan = max(t1, t2)

                    if neighbor_makespan < best_neighbor_makespan:
                        best_neighbor_makespan = neighbor_makespan
                        best_neighbor_solution = neighbor
        
        # Verifica se houve melhoria
        if best_neighbor_solution is None:
            print("=> Ótimo local encontrado. Nenhuma melhoria possível nas vizinhanças testadas.")
            break
        else:
            # Move para a melhor solução vizinha encontrada nesta iteração
            current_solution = best_neighbor_solution
            current_makespan = best_neighbor_makespan

            # Recalcula os tempos individuais das máquinas para exibição
            time1 = calculate_sequence_time(current_solution[1], processing_times, setup_matrix, release_dates)
            time2 = calculate_sequence_time(current_solution[2], processing_times, setup_matrix, release_dates)

            # Exibe os detalhes da nova solução atual
            print(f"=> Melhoria encontrada! Novo Makespan: {current_makespan:.0f}")
            print(f"   Nova Solução M1: Seq={current_solution[1]}, Tempo={time1:.0f}")
            print(f"   Nova Solução M2: Seq={current_solution[2]}, Tempo={time2:.0f}")

    return current_solution, current_makespan

# --- Execução Principal ---
def run_scenario(scenario_name, release_dates_data=None):
    print("="*50)
    print(f"EXECUTANDO {scenario_name}")
    print("="*50)
    
    # 1. Gerar Solução Inicial
    print("\n[FASE 1: GERANDO SOLUÇÃO INICIAL COM FFD]")
    initial_solution = solve_with_ffd(processing_times, setup_matrix, release_dates_data)
    time1_initial = calculate_sequence_time(initial_solution[1], processing_times, setup_matrix, release_dates_data)
    time2_initial = calculate_sequence_time(initial_solution[2], processing_times, setup_matrix, release_dates_data)
    makespan_initial = max(time1_initial, time2_initial)
    
    print("\n--- Solução Inicial Encontrada ---")
    print(f"Máquina 1: Seq={initial_solution[1]}, Tempo={time1_initial:.0f}")
    print(f"Máquina 2: Seq={initial_solution[2]}, Tempo={time2_initial:.0f}")
    print(f"Makespan Inicial: {makespan_initial:.0f}")

    # 2. Aplicar Busca Local
    print("\n[FASE 2: APLICANDO BUSCA LOCAL PARA MELHORIA]")
    final_solution, final_makespan = local_search(initial_solution, processing_times, setup_matrix, release_dates_data)
    
    # 3. Exibir Resultado Final
    time1_final = calculate_sequence_time(final_solution[1], processing_times, setup_matrix, release_dates_data)
    time2_final = calculate_sequence_time(final_solution[2], processing_times, setup_matrix, release_dates_data)
    
    print("\n" + "="*50)
    print(f"RESULTADO FINAL PARA {scenario_name}")
    print("="*50)
    print("--- Solução Após Busca Local ---")
    print(f"Máquina 1: Seq={final_solution[1]}, Tempo={time1_final:.0f}")
    print(f"Máquina 2: Seq={final_solution[2]}, Tempo={time2_final:.0f}")
    print(f"Makespan Final: {final_makespan:.0f}")
    print(f"\nMelhoria de Makespan: {makespan_initial - final_makespan:.0f}\n\n")

# Executar para os dois cenários
run_scenario("CENÁRIO A (Sem Tempos de Liberação)")
run_scenario("CENÁRIO B (Com Tempos de Liberação)", release_dates)