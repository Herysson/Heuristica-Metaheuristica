## Problema
Trata-se de um problema de sequenciamento de 10 tarefas em 2 máquinas, onde o objetivo é minimizar o tempo total de conclusão (o *makespan*). Existem custos de tempo de preparação (setup) que dependem da ordem das tarefas, o que torna o problema mais complexo.

### Adptanto o problema ao problema já conhecido de *bin packing*

* **Itens (Bin Packing)** -> **Tarefas (Scheduling)**
* **Tamanho do Item** -> **Tempo de Processamento da Tarefa**
* **Bins (Bin Packing)** -> **Máquinas (Scheduling)**

### Adaptando o Algoritmo First Fit Decreasing (FFD)

A adaptação do FFD para o nosso problema de scheduling será a seguinte:

1.  **Decreasing (Ordenação):** Primeiro, ordenamos as tarefas em ordem decrescente de seus tempos de processamento. A intuição é que as tarefas mais longas são mais difíceis de encaixar e devem ser alocadas primeiro para equilibrar a carga entre as máquinas.
2.  **First Fit (Alocação):** Em seguida, pegamos as tarefas, uma a uma, na ordem decrescente, e as alocamos na máquina que terminará o trabalho mais cedo. Esta é a nossa regra "First Fit": escolher a primeira máquina (a que termina mais cedo) que pode receber a tarefa.

***

### Cenário A: Sem Tempos de Liberação

Todas as tarefas estão disponíveis no tempo `t=0`.

#### Passo 1: Ordenar as Tarefas por Tempo de Processamento (Decrescente)

| Tarefa | Tempo de Processamento ($p_j$) |
| :--- | :--- |
| T5 | 40 |
| T3 | 35 |
| T8 | 30 |
| T1 | 28 |
| T7 | 25 |
| T4 | 22 |
| T10 | 20 |
| T6 | 18 |
| T2 | 15 |
| T9 | 12 |

#### Passo 2: Alocar as Tarefas na Máquina que Termina Primeiro

Inicializamos as máquinas:
* **Máquina 1 (M1):** Tempo Total = 0, Sequência = [], Última Tarefa = 0 (inicial)
* **Máquina 2 (M2):** Tempo Total = 0, Sequência = [], Última Tarefa = 0 (inicial)

Vamos alocar tarefa por tarefa:

1.  **Tarefa T5 (p=40):**
    * Custo em M1: $s_{0,5} + p_5 = 25 + 40 = 65$
    * Custo em M2: $s_{0,5} + p_5 = 25 + 40 = 65$
    * Empate. Alocamos em M1.
    * **M1:** Tempo=65, Seq=[T5], Última=5

2.  **Tarefa T3 (p=35):**
    * Custo em M1: (Impossível, já tem T5)
    * Custo em M2: $s_{0,3} + p_3 = 50 + 35 = 85$
    * Alocamos em M2.
    * **M2:** Tempo=85, Seq=[T3], Última=3

3.  **Tarefa T8 (p=30):**
    * Tempo M1 se adicionar T8: $65 + s_{5,8} + p_8 = 65 + 38 + 30 = 133$
    * Tempo M2 se adicionar T8: $85 + s_{3,8} + p_8 = 85 + 58 + 30 = 173$
    * M1 termina antes (133 < 173). Alocamos em M1.
    * **M1:** Tempo=133, Seq=[T5, T8], Última=8

4.  **Tarefa T1 (p=28):**
    * Tempo M1 se adicionar T1: $133 + s_{8,1} + p_1 = 133 + 51 + 28 = 212$
    * Tempo M2 se adicionar T1: $85 + s_{3,1} + p_1 = 85 + 92 + 28 = 205$
    * M2 termina antes (205 < 212). Alocamos em M2.
    * **M2:** Tempo=205, Seq=[T3, T1], Última=1

5.  **Tarefa T7 (p=25):**
    * Tempo M1 se adicionar T7: $133 + s_{8,7} + p_7 = 133 + 36 + 25 = 194$
    * Tempo M2 se adicionar T7: $205 + s_{1,7} + p_7 = 205 + 58 + 25 = 288$
    * M1 termina antes (194 < 288). Alocamos em M1.
    * **M1:** Tempo=194, Seq=[T5, T8, T7], Última=7

6.  **Tarefa T4 (p=22):**
    * Tempo M1 se adicionar T4: $194 + s_{7,4} + p_4 = 194 + 72 + 22 = 288$
    * Tempo M2 se adicionar T4: $205 + s_{1,4} + p_4 = 205 + 71 + 22 = 298$
    * M1 termina antes (288 < 298). Alocamos em M1.
    * **M1:** Tempo=288, Seq=[T5, T8, T7, T4], Última=4

7.  **Tarefa T10 (p=20):**
    * Tempo M1 se adicionar T10: $288 + s_{4,10} + p_{10} = 288 + 56 + 20 = 364$
    * Tempo M2 se adicionar T10: $205 + s_{1,10} + p_{10} = 205 + 57 + 20 = 282$
    * M2 termina antes (282 < 364). Alocamos em M2.
    * **M2:** Tempo=282, Seq=[T3, T1, T10], Última=10

8.  **Tarefa T6 (p=18):**
    * Tempo M1 se adicionar T6: $288 + s_{4,6} + p_6 = 288 + 86 + 18 = 392$
    * Tempo M2 se adicionar T6: $282 + s_{10,6} + p_6 = 282 + 38 + 18 = 338$
    * M2 termina antes (338 < 392). Alocamos em M2.
    * **M2:** Tempo=338, Seq=[T3, T1, T10, T6], Última=6

9.  **Tarefa T2 (p=15):**
    * Tempo M1 se adicionar T2: $288 + s_{4,2} + p_2 = 288 + 96 + 15 = 399$
    * Tempo M2 se adicionar T2: $338 + s_{6,2} + p_2 = 338 + 56 + 15 = 409$
    * M1 termina antes (399 < 409). Alocamos em M1.
    * **M1:** Tempo=399, Seq=[T5, T8, T7, T4, T2], Última=2

10. **Tarefa T9 (p=12):**
    * Tempo M1 se adicionar T9: $399 + s_{2,9} + p_9 = 399 + 89 + 12 = 500$
    * Tempo M2 se adicionar T9: $338 + s_{6,9} + p_9 = 338 + 34 + 12 = 384$
    * M2 termina antes (384 < 500). Alocamos em M2.
    * **M2:** Tempo=384, Seq=[T3, T1, T10, T6, T9], Última=9

#### Solução Inicial (Cenário A)

* **Máquina 1:**
    * Sequência: **T5 -> T8 -> T7 -> T4 -> T2**
    * Tempo Total: **399**
* **Máquina 2:**
    * Sequência: **T3 -> T1 -> T10 -> T6 -> T9**
    * Tempo Total: **384**

O **makespan** (tempo da máquina que termina por último) é **399**.


***

### Cenário B: Com Tempos de Liberação

Agora, a máquina pode ficar ociosa esperando a tarefa ser liberada. O tempo de início de uma tarefa `j` será `max(tempo_atual_maquina, r_j)`.

Usaremos a mesma ordem de tarefas (decrescente por tempo de processamento).

#### Configuração Inicial

**1. Ordem das Tarefas:** As tarefas são consideradas em ordem decrescente de seu tempo de processamento. Para cada tarefa, também listamos seu tempo de liberação ($r_j$).

| Ordem | Tarefa | Tempo de Processamento ($p_j$) | Tempo de Liberação ($r_j$) |
|:---|:---|:---:|:---:|
| 1º | T5 | 40 | 35 |
| 2º | T3 | 35 | 10 |
| 3º | T8 | 30 | 60 |
| 4º | T1 | 28 | 0 |
| 5º | T7 | 25 | 15 |
| 6º | T4 | 22 | 0 |
| 7º | T10| 20 | 45 |
| 8º | T6 | 18 | 50 |
| 9º | T2 | 15 | 20 |
| 10º| T9 | 12 | 5 |

**2. Estado Inicial das Máquinas:**
* **Máquina 1 (M1):** Tempo de Conclusão = 0, Última Tarefa = '0' (inicial)
* **Máquina 2 (M2):** Tempo de Conclusão = 0, Última Tarefa = '0' (inicial)

---

#### Passo a Passo da Alocação

A fórmula para o tempo de conclusão de uma tarefa `j` em uma máquina `M` é:
`Tempo de Conclusão = max(Tempo Livre da Máquina, Tempo de Liberação de j) + s(última_tarefa, j) + p(j)`

1.  **Tarefa T5 (p=40, r=35):**
    * Tempo M1 se adicionar T5: Início=max(0, 35)=35. Conclusão = $35 + s_{0,5} + p_5 = 35 + 25 + 40 = 100$
    * Tempo M2 se adicionar T5: Início=max(0, 35)=35. Conclusão = $35 + s_{0,5} + p_5 = 35 + 25 + 40 = 100$
    * Empate. Alocamos em M1.
    * **M1:** Tempo=100, Seq=[T5], Última=5

2.  **Tarefa T3 (p=35, r=10):**
    * Tempo M1 se adicionar T3: Início=max(100, 10)=100. Conclusão = $100 + s_{5,3} + p_3 = 100 + 74 + 35 = 209$
    * Tempo M2 se adicionar T3: Início=max(0, 10)=10. Conclusão = $10 + s_{0,3} + p_3 = 10 + 50 + 35 = 95$
    * M2 termina antes (95 < 209). Alocamos em M2.
    * **M2:** Tempo=95, Seq=[T3], Última=3

3.  **Tarefa T8 (p=30, r=60):**
    * Tempo M1 se adicionar T8: Início=max(100, 60)=100. Conclusão = $100 + s_{5,8} + p_8 = 100 + 38 + 30 = 168$
    * Tempo M2 se adicionar T8: Início=max(95, 60)=95. Conclusão = $95 + s_{3,8} + p_8 = 95 + 58 + 30 = 183$
    * M1 termina antes (168 < 183). Alocamos em M1.
    * **M1:** Tempo=168, Seq=[T5, T8], Última=8

4.  **Tarefa T1 (p=28, r=0):**
    * Tempo M1 se adicionar T1: Início=max(168, 0)=168. Conclusão = $168 + s_{8,1} + p_1 = 168 + 51 + 28 = 247$
    * Tempo M2 se adicionar T1: Início=max(95, 0)=95. Conclusão = $95 + s_{3,1} + p_1 = 95 + 92 + 28 = 215$
    * M2 termina antes (215 < 247). Alocamos em M2.
    * **M2:** Tempo=215, Seq=[T3, T1], Última=1

5.  **Tarefa T7 (p=25, r=15):**
    * Tempo M1 se adicionar T7: Início=max(168, 15)=168. Conclusão = $168 + s_{8,7} + p_7 = 168 + 36 + 25 = 229$
    * Tempo M2 se adicionar T7: Início=max(215, 15)=215. Conclusão = $215 + s_{1,7} + p_7 = 215 + 58 + 25 = 298$
    * M1 termina antes (229 < 298). Alocamos em M1.
    * **M1:** Tempo=229, Seq=[T5, T8, T7], Última=7

6.  **Tarefa T4 (p=22, r=0):**
    * Tempo M1 se adicionar T4: Início=max(229, 0)=229. Conclusão = $229 + s_{7,4} + p_4 = 229 + 72 + 22 = 323$
    * Tempo M2 se adicionar T4: Início=max(215, 0)=215. Conclusão = $215 + s_{1,4} + p_4 = 215 + 71 + 22 = 308$
    * M2 termina antes (308 < 323). Alocamos em M2.
    * **M2:** Tempo=308, Seq=[T3, T1, T4], Última=4

7.  **Tarefa T10 (p=20, r=45):**
    * Tempo M1 se adicionar T10: Início=max(229, 45)=229. Conclusão = $229 + s_{7,10} + p_{10} = 229 + 18 + 20 = 267$
    * Tempo M2 se adicionar T10: Início=max(308, 45)=308. Conclusão = $308 + s_{4,10} + p_{10} = 308 + 56 + 20 = 384$
    * M1 termina antes (267 < 384). Alocamos em M1.
    * **M1:** Tempo=267, Seq=[T5, T8, T7, T10], Última=10

8.  **Tarefa T6 (p=18, r=50):**
    * Tempo M1 se adicionar T6: Início=max(267, 50)=267. Conclusão = $267 + s_{10,6} + p_6 = 267 + 38 + 18 = 323$
    * Tempo M2 se adicionar T6: Início=max(308, 50)=308. Conclusão = $308 + s_{4,6} + p_6 = 308 + 86 + 18 = 412$
    * M1 termina antes (323 < 412). Alocamos em M1.
    * **M1:** Tempo=323, Seq=[T5, T8, T7, T10, T6], Última=6

9.  **Tarefa T2 (p=15, r=20):**
    * Tempo M1 se adicionar T2: Início=max(323, 20)=323. Conclusão = $323 + s_{6,2} + p_2 = 323 + 56 + 15 = 394$
    * Tempo M2 se adicionar T2: Início=max(308, 20)=308. Conclusão = $308 + s_{4,2} + p_2 = 308 + 96 + 15 = 419$
    * M1 termina antes (394 < 419). Alocamos em M1.
    * **M1:** Tempo=394, Seq=[T5, T8, T7, T10, T6, T2], Última=2

10. **Tarefa T9 (p=12, r=5):**
    * Tempo M1 se adicionar T9: Início=max(394, 5)=394. Conclusão = $394 + s_{2,9} + p_9 = 394 + 89 + 12 = 495$
    * Tempo M2 se adicionar T9: Início=max(308, 5)=308. Conclusão = $308 + s_{4,9} + p_9 = 308 + 38 + 12 = 358$
    * M2 termina antes (358 < 495). Alocamos em M2.
    * **M2:** Tempo=358, Seq=[T3, T1, T4, T9], Última=9

#### Solução Inicial (Cenário B)

* **Máquina 1:**
    * Sequência: **T5 -> T8 -> T7 -> T10 -> T6 -> T2**
    * Tempo Total: **394**
* **Máquina 2:**
    * Sequência: **T3 -> T1 -> T4 -> T9**
    * Tempo Total: **358**

O **makespan** (tempo da máquina que termina por último) é **394**.
