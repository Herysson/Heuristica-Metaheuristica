# **Configuração do Problema (Dados Estruturados)**

* **Máquinas (m):** 2 (M1, M2)
* **Tarefas (n):** 10 (T1, T2, ..., T10)

* **Tempos de Processamento ($p_j$) em minutos:**
    * p1=28, p2=15, p3=35, p4=22, p5=40
    * p6=18, p7=25, p8=30, p9=12, p10=20

## **Matriz de Tempos de Preparação ($s_{ij}$) (Simétrica)**
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

#### **Verificação da Desigualdade Triangular (Exemplo)**
Vamos testar se $s_{1,3} \le s_{1,2} + s_{2,3}$:
* Caminho direto de 1 para 3: $s_{1,3} = 92$.
* Caminho indireto via 2: $s_{1,2} + s_{2,3} = 65 + 75 = 140$.
* **Resultado:** $92 \le 140$. A desigualdade é respeitada. Por ser uma matriz de distância Euclidiana, essa propriedade será válida para qualquer combinação de três tarefas.

### O que é uma Matriz de Tempos de Preparação?

Uma **Matriz de Tempos de Preparação** (em inglês, *Setup Time Matrix*) é uma tabela que quantifica o tempo necessário para preparar uma máquina ou um processo para iniciar uma nova tarefa, com base na tarefa que acabou de ser concluída. É a representação do custo (em tempo) da **transição** entre duas atividades.

A ideia central é que este tempo de preparação **depende da sequência** das tarefas.

A estrutura da matriz é a seguinte:
* As **linhas** representam a tarefa **"De"**: a tarefa que acabou de terminar.
* As **colunas** representam a tarefa **"Para"**: a próxima tarefa que será executada.
* O valor no cruzamento da linha *i* com a coluna *j* é o tempo de preparação $s_{ij}$: o tempo para configurar a máquina para a tarefa *j* sabendo que ela acabou de fazer a tarefa *i*.

**Exemplo Prático e Simples:**

Imagine uma máquina que pinta peças.
* **Mudar de Tinta Branca para Preta:** Requer pouca ou nenhuma limpeza. O tempo de preparação é baixo. Digamos, $s_{\text{branca} \to \text{preta}} = 5$ minutos.
* **Mudar de Tinta Preta para Branca:** Requer uma limpeza profunda e rigorosa para evitar contaminação da cor. O tempo de preparação é alto. Digamos, $s_{\text{preta} \to \text{branca}} = 60$ minutos.

Este exemplo ilustra duas características-chave que vimos nos artigos:

1.  **Dependência da Sequência:** A ordem em que as cores são pintadas muda drasticamente o tempo total gasto em preparação.
2.  **Assimetria:** O tempo de preparação não é o mesmo nos dois sentidos ($s_{ij} \neq s_{ji}$). [cite_start]Os artigos que analisamos consideram explicitamente essa possibilidade, pois ela reflete a realidade de muitos processos[cite: 2631].

### Para que serve a Matriz?

A Matriz de Tempos de Preparação é um componente crítico para a modelagem e otimização de sistemas de produção realistas. Sua principal finalidade é:

1.  **Tornar o Modelo de Sequenciamento Realista:** Em muitos ambientes de produção (indústria química, têxtil, gráfica, metalúrgica), os tempos de preparação são significativos e não podem ser ignorados. Ignorá-los levaria a planejamentos de produção completamente irrealistas.

2.  **Otimizar a Sequência de Produção:** A matriz fornece os dados necessários para responder à pergunta: "**Qual é a melhor ordem para executar as tarefas para minimizar o tempo perdido em preparações?**". Ao analisar os valores da matriz, um algoritmo pode encontrar uma sequência que agrupe tarefas similares ou que siga uma ordem lógica para reduzir os tempos de troca.

3.  **Reduzir o Tempo Total de Produção (Makespan):** O objetivo final é minimizar o tempo total para concluir todos os trabalhos ($C_{max}$). Como o tempo total em uma máquina é a soma dos tempos de preparação e dos tempos de processamento, minimizar os tempos de preparação contribui diretamente para a redução do makespan.

---

## **Cenário A: Sem Tempos de Liberação (Release Dates)**

* **Condição:** Todas as 10 tarefas estão disponíveis em $t=0$.
* **Objetivo:** Alocar e sequenciar as 10 tarefas nas 2 máquinas para minimizar o makespan.

## **Cenário B: Com Tempos de Liberação (Release Dates)**

* **Condição:** As tarefas só podem ser iniciadas a partir dos seus tempos de liberação.
* **Dados Adicionais - Tempos de Liberação ($r_j$) em minutos:**
    * r1=0, r2=20, r3=10, r4=0, r5=35
    * r6=50, r7=15, r8=60, r9=5, r10=45

### O que são Tempos de Liberação (Release Dates)?

O **Tempo de Liberação** (em inglês, *Release Date* ou *Ready Time*) de uma tarefa é o instante de tempo mais cedo a partir do qual a tarefa se torna **disponível** para ser processada.

Em outras palavras, mesmo que uma máquina esteja livre e pronta, ela não pode começar a trabalhar em uma tarefa (nem mesmo iniciar sua preparação/setup) antes que o tempo de liberação dessa tarefa seja alcançado.

**Analogia Simples: A Encomenda de um Bolo**

Imagine que você é um confeiteiro e sua cozinha é a "máquina". Você tem duas encomendas (tarefas) para hoje:

1.  **Bolo de Chocolate (T1):** Todos os ingredientes estão na sua despensa.
2.  **Bolo de Morango (T2):** O cliente ficou de entregar os morangos frescos às 14h.

O **Tempo de Liberação** do Bolo de Morango (T2) é **14h**. Mesmo que você termine o Bolo de Chocolate (T1) ao meio-dia e sua cozinha esteja livre, você **não pode** começar a fazer o Bolo de Morango. Você é forçado a esperar até as 14h. Esse período de espera é um **tempo ocioso** (idle time) para a sua "máquina".

### Para que servem no Problema de Sequenciamento?

Nos problemas que estamos analisando, os Tempos de Liberação servem para modelar a realidade de que as tarefas não estão todas disponíveis magicamente no início do planejamento. Eles introduzem uma restrição crucial que simula cenários reais, como:

1.  **Chegada de Matéria-Prima:** Uma tarefa não pode começar antes que os materiais necessários cheguem à fábrica.
2.  **Processos Anteriores:** Uma tarefa na "Etapa 2" da produção não pode ser liberada até que a "Etapa 1" seja concluída.
3.  **Ordens de Clientes:** Um cliente pode fazer um pedido com a instrução de que a produção só deve começar a partir de uma data específica.

