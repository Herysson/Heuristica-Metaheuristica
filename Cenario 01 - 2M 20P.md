
### **Configuração do Problema (Dados Completos)**

* **Máquinas (m):** 2 (M1, M2)
* **Tarefas (n):** 20 (T1, T2, ..., T20)

* **Tempos de Processamento ($p_j$) em minutos:**
    * p1=25, p2=30, p3=18, p4=40, p5=22
    * p6=35, p7=42, p8=15, p9=28, p10=50
    * p11=19, p12=24, p13=33, p14=45, p15=20
    * p16=38, p17=21, p18=48, p19=16, p20=29

### **Matriz Completa de Tempos de Preparação ($s_{ij}$) (Assimétrica)**
As linhas representam a tarefa 'De' (a tarefa que acabou de terminar) e as colunas representam a tarefa 'Para' (a próxima a ser executada). O valor `999` na diagonal representa um movimento impossível (não se faz setup para a mesma tarefa). A linha 0 representa o estado inicial das máquinas.

| De (i) \ Para (j) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **0** | 10 | 12 | 8 | 15 | 11 | 9 | 14 | 7 | 13 | 18 | 6 | 9 | 11 | 16 | 8 | 10 | 7 | 19 | 5 | 9 |
| **1** | 999 | 25 | 18 | 30 | 22 | 33 | 30 | 15 | 28 | 40 | 17 | 23 | 29 | 38 | 20 | 26 | 21 | 42 | 14 | 27 |
| **2** | 28 | 999 | 20 | 35 | 24 | 38 | 41 | 18 | 31 | 45 | 19 | 22 | 32 | 41 | 22 | 30 | 23 | 48 | 17 | 30 |
| **3** | 16 | 21 | 999 | 28 | 19 | 30 | 34 | 12 | 25 | 38 | 14 | 20 | 26 | 35 | 18 | 24 | 18 | 39 | 12 | 24 |
| **4** | 38 | 42 | 31 | 999 | 35 | 48 | 50 | 28 | 45 | 55 | 32 | 25 | 45 | 52 | 33 | 41 | 36 | 60 | 29 | 43 |
| **5** | 20 | 26 | 15 | 32 | 999 | 28 | 36 | 14 | 27 | 41 | 16 | 21 | 28 | 37 | 19 | 25 | 20 | 41 | 13 | 26 |
| **6** | 32 | 39 | 28 | 45 | 31 | 999 | 48 | 25 | 40 | 52 | 29 | 36 | 42 | 50 | 30 | 39 | 34 | 58 | 27 | 41 |
| **7** | 40 | 45 | 35 | 52 | 38 | 50 | 999 | 29 | 48 | 58 | 36 | 43 | 49 | 55 | 37 | 46 | 40 | 28 | 30 | 49 |
| **8** | 14 | 17 | 10 | 22 | 13 | 24 | 27 | 999 | 20 | 30 | 11 | 15 | 19 | 28 | 12 | 16 | 14 | 32 | 9 | 18 |
| **9** | 26 | 32 | 21 | 40 | 28 | 42 | 44 | 21 | 999 | 48 | 25 | 31 | 37 | 46 | 27 | 34 | 29 | 51 | 23 | 36 |
| **10** | 48 | 53 | 41 | 60 | 46 | 58 | 62 | 38 | 55 | 999 | 42 | 50 | 56 | 65 | 45 | 52 | 47 | 70 | 40 | 54 |
| **11** | 17 | 20 | 13 | 26 | 16 | 28 | 31 | 10 | 23 | 35 | 999 | 18 | 22 | 31 | 15 | 20 | 16 | 36 | 11 | 21 |
| **12** | 22 | 20 | 18 | 30 | 20 | 32 | 35 | 16 | 28 | 42 | 19 | 999 | 29 | 38 | 21 | 27 | 22 | 43 | 15 | 28 |
| **13** | 30 | 36 | 25 | 44 | 31 | 45 | 48 | 24 | 39 | 51 | 28 | 34 | 999 | 49 | 29 | 37 | 32 | 55 | 26 | 40 |
| **14** | 42 | 48 | 38 | 55 | 41 | 54 | 59 | 33 | 50 | 63 | 39 | 47 | 53 | 999 | 40 | 50 | 44 | 68 | 36 | 52 |
| **15** | 18 | 23 | 14 | 29 | 18 | 30 | 33 | 13 | 25 | 39 | 16 | 20 | 26 | 36 | 999 | 23 | 19 | 40 | 12 | 25 |
| **16** | 35 | 41 | 31 | 49 | 36 | 48 | 53 | 28 | 44 | 57 | 34 | 40 | 47 | 56 | 35 | 999 | 38 | 62 | 31 | 46 |
| **17** | 19 | 24 | 16 | 30 | 20 | 32 | 35 | 14 | 27 | 40 | 17 | 22 | 28 | 37 | 20 | 26 | 999 | 42 | 14 | 27 |
| **18** | 45 | 51 | 40 | 62 | 46 | 59 | 64 | 36 | 54 | 68 | 43 | 51 | 58 | 69 | 46 | 56 | 49 | 999 | 40 | 57 |
| **19** | 15 | 18 | 11 | 24 | 14 | 25 | 28 | 10 | 21 | 33 | 12 | 16 | 20 | 29 | 13 | 18 | 15 | 34 | 999 | 20 |
| **20** | 27 | 33 | 23 | 41 | 29 | 42 | 46 | 23 | 38 | 50 | 27 | 33 | 39 | 49 | 28 | 36 | 31 | 55 | 25 | 999 |

---



### **Cenário A: Sem Tempos de Liberação (Release Dates)**

* **Condição:** Todas as tarefas estão disponíveis em $t=0$. ($r_j=0$ para j=1,...,20).
* **Objetivo:** Encontrar uma partição das 20 tarefas em dois conjuntos (um para M1, outro para M2) e uma sequência para cada conjunto, de modo que o tempo de conclusão da última tarefa a terminar (em qualquer uma das máquinas) seja o menor possível.
* **Exemplo de Cálculo (para uma sequência hipotética M1: T1 -> T7 -> ...):**
    * `Tempo Total M1 = (s_0,1 + p_1) + (s_1,7 + p_7) + ...`
    * `Tempo Total M1 = (10 + 25) + (30 + 42) + ... = 35 + 72 + ...`

### **Cenário B: Com Tempos de Liberação (Release Dates)**

* **Condição:** As tarefas só podem ser iniciadas a partir dos seus tempos de liberação.
* **Dados Adicionais - Tempos de Liberação ($r_j$) em minutos:**
    * r1=0, r2=15, r3=5, r4=0, r5=25
    * r6=40, r7=40, r8=60, r9=10, r10=55
    * r11=70, r12=80, r13=30, r14=20, r15=90
    * r16=0, r17=100, r18=45, r19=110, r20=65
* **Objetivo:** O mesmo do Cenário A, mas agora o cálculo do tempo de término de cada tarefa deve considerar o tempo de liberação.
