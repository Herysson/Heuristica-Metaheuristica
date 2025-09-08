### **Configuração do Problema (Dados Estruturados)**

* **Máquinas (m):** 2 (M1, M2)
* **Tarefas (n):** 10 (T1, T2, ..., T10)

* **Coordenadas das Tarefas no Plano (x, y):**
    A Tarefa 0 (T0) representa a origem ou o estado inicial das máquinas.

| Tarefa | Coordenada (x, y) |
| :--- | :---: |
| T0 | (50, 50) |
| T1 | (10, 20) |
| T2 | (15, 85) |
| T3 | (90, 80) |
| T4 | (80, 10) |
| T5 | (25, 45) |
| T6 | (70, 95) |
| T7 | (40, 70) |
| T8 | (60, 30) |
| T9 | (95, 45) |
| T10| (55, 60) |

* **Tempos de Processamento ($p_j$) em minutos:**
    * p1=28, p2=15, p3=35, p4=22, p5=40
    * p6=18, p7=25, p8=30, p9=12, p10=20

### **Matriz de Tempos de Preparação ($s_{ij}$) (Simétrica)**
Calculada como a distância Euclidiana (arredondada para o inteiro mais próximo) entre os pontos das tarefas. A diagonal principal é **0**, pois a distância de uma tarefa para ela mesma é nula.

| De (i) \ Para (j) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| :--- | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: | :-: |
| **0 (Inicial)** | 50 | 47 | 50 | 42 | 25 | 49 | 22 | 22 | 45 | 11 |
| **1** | 0 | 65 | 92 | 71 | 29 | 92 | 58 | 51 | 89 | 57 |
| **2** | 65 | 0 | 75 | 96 | 41 | 56 | 32 | 68 | 89 | 47 |
| **3** | 92 | 75 | 0 | 71 | 74 | 25 | 51 | 58 | 40 | 40 |
| **4** | 71 | 96 | 71 | 0 | 59 | 86 | 72 | 28 | 38 | 56 |
| **5** | 29 | 41 | 74 | 59 | 0 | 67 | 29 | 38 | 70 | 34 |
| **6** | 92 | 56 | 25 | 86 | 67 | 0 | 39 | 66 | 34 | 38 |
| **7** | 58 | 32 | 51 | 72 | 29 | 39 | 0 | 36 | 60 | 18 |
| **8** | 51 | 68 | 58 | 28 | 38 | 66 | 36 | 0 | 41 | 30 |
| **9** | 89 | 89 | 40 | 38 | 70 | 34 | 60 | 41 | 0 | 43 |
| **10** | 57 | 47 | 40 | 56 | 34 | 38 | 18 | 30 | 43 | 0 |

---
#### **Verificação da Desigualdade Triangular (Exemplo)**
Vamos testar se $s_{1,3} \le s_{1,2} + s_{2,3}$:
* Caminho direto de 1 para 3: $s_{1,3} = 92$.
* Caminho indireto via 2: $s_{1,2} + s_{2,3} = 65 + 75 = 140$.
* **Resultado:** $92 \le 140$. A desigualdade é respeitada. Por ser uma matriz de distância Euclidiana, essa propriedade será válida para qualquer combinação de três tarefas.

---

### **Cenário A: Sem Tempos de Liberação (Release Dates)**

* **Condição:** Todas as 10 tarefas estão disponíveis em $t=0$.
* **Objetivo:** Alocar e sequenciar as 10 tarefas nas 2 máquinas para minimizar o makespan.

### **Cenário B: Com Tempos de Liberação (Release Dates)**

* **Condição:** As tarefas só podem ser iniciadas a partir dos seus tempos de liberação.
* **Dados Adicionais - Tempos de Liberação ($r_j$) em minutos:**
    * r1=0, r2=20, r3=10, r4=0, r5=35
    * r6=50, r7=15, r8=60, r9=5, r10=45
