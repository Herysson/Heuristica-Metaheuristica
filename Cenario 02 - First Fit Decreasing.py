# --- Dados do Problema (Cenário 02 - 2M 10P) ---

# Dicionário com os tempos de processamento {tarefa: tempo}
processing_times = {
    1: 28, 2: 15, 3: 35, 4: 22, 5: 40,
    6: 18, 7: 25, 8: 30, 9: 12, 10: 20
}

# Matriz de tempos de preparação (setup)
# Usamos um dicionário de dicionários para facilitar o acesso: setup_matrix[de][para]
# A chave '0' representa o estado inicial da máquina.
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

# Dicionário com os tempos de liberação (release dates) para o Cenário B
release_dates = {
    1: 0, 2: 20, 3: 10, 4: 0, 5: 35,
    6: 50, 7: 15, 8: 60, 9: 5, 10: 45
}

def solve_with_ffd(processing_times, setup_matrix, release_dates=None):
    """
    Resolve o problema de scheduling usando a heurística FFD adaptada.
    Se 'release_dates' for fornecido, considera o Cenário B.
    """
    # 1. ORDENAÇÃO (Decreasing): Ordena as tarefas em ordem decrescente de tempo de processamento.
    sorted_tasks = sorted(processing_times.keys(), key=lambda task: processing_times[task], reverse=True)
    
    # Inicializa o estado das máquinas
    machines = {
        1: {'sequence': [], 'completion_time': 0, 'last_task': '0'},
        2: {'sequence': [], 'completion_time': 0, 'last_task': '0'}
    }
    
    print("Ordem de alocação das tarefas:", sorted_tasks)
    print("-" * 30)

    # 2. ALOCAÇÃO (First Fit): Itera sobre as tarefas ordenadas
    for task_id in sorted_tasks:
        
        # Dicionário para guardar o custo (tempo de término) de alocar a tarefa em cada máquina
        potential_completion_times = {}

        # Calcula o tempo de término para cada máquina se a tarefa atual for alocada nela
        for machine_id, machine_data in machines.items():
            
            last_task = machine_data['last_task']
            machine_ready_time = machine_data['completion_time']
            
            # Determina o tempo de início da tarefa
            start_time = machine_ready_time
            if release_dates:
                task_release_time = release_dates[task_id]
                start_time = max(machine_ready_time, task_release_time) # A máquina pode ter que esperar
            
            # Calcula o novo tempo de conclusão
            setup_time = setup_matrix[last_task][task_id]
            proc_time = processing_times[task_id]
            completion_time = start_time + setup_time + proc_time
            
            potential_completion_times[machine_id] = completion_time

        # Escolhe a máquina que termina a tarefa mais cedo ("First Fit")
        best_machine = min(potential_completion_times, key=potential_completion_times.get)
        
        # Atualiza a máquina escolhida com a nova tarefa
        machines[best_machine]['sequence'].append(task_id)
        machines[best_machine]['completion_time'] = potential_completion_times[best_machine]
        machines[best_machine]['last_task'] = task_id
        
        print(f"Alocando Tarefa {task_id}: Escolhida Máquina {best_machine} (termina em {potential_completion_times[best_machine]:.0f})")

    # Calcula o makespan final
    makespan = max(m['completion_time'] for m in machines.values())
    
    return machines, makespan

# --- Execução e Resultados ---

print("="*40)
print("Resolvendo Cenário A: Sem Tempos de Liberação")
print("="*40)
machines_a, makespan_a = solve_with_ffd(processing_times, setup_matrix)
print("\n--- Resultado Final (Cenário A) ---")
print(f"Máquina 1: Sequência = {machines_a[1]['sequence']}, Tempo Total = {machines_a[1]['completion_time']:.0f}")
print(f"Máquina 2: Sequência = {machines_a[2]['sequence']}, Tempo Total = {machines_a[2]['completion_time']:.0f}")
print(f"\n==> Makespan Final (Cenário A): {makespan_a:.0f}\n\n")


print("="*40)
print("Resolvendo Cenário B: Com Tempos de Liberação")
print("="*40)
machines_b, makespan_b = solve_with_ffd(processing_times, setup_matrix, release_dates)
print("\n--- Resultado Final (Cenário B) ---")
print(f"Máquina 1: Sequência = {machines_b[1]['sequence']}, Tempo Total = {machines_b[1]['completion_time']:.0f}")
print(f"Máquina 2: Sequência = {machines_b[2]['sequence']}, Tempo Total = {machines_b[2]['completion_time']:.0f}")
print(f"\n==> Makespan Final (Cenário B): {makespan_b:.0f}")