# E3 — MVP: Núcleo Funcional com Primeiras Telas

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 10 de maio de 2026  
> **Peso:** 25% da nota final  

---

## Identificação do Grupo

| Grupo: Node Conquest | |
|-------|----------|
| [Repositório GitHub](https://github.com/Luis-Hardt/Node-Conquest.git) | |
| Bruna Alves de Jesus | 40420418 |
| Luis Fernando Barcelos Hardt | 38774631 |
| Miguel da Silva Pereira | 41005422 |

---

## 1. Como Executar o MVP

> Instrua como rodar o projeto do zero. Alguém que nunca viu o código deve conseguir executar seguindo estas instruções.

**Pré-requisitos:**

```bash
Python 3.12 ou superior
Bibliotecas: networkx, matplotlib
```

**Instalação:**

```bash
git clone https://github.com/Luis-Hardt/Node-Conquest
cd Node-Conquest-main
pip install -r requirements.txt  (ou npm install, etc.)
```

**Execução:**

```bash
python src/main.py --input data/exemplo.json
```

**Saída esperada:**

```

```

---

## 2. Algoritmo Implementado

| Campo | Resposta |
|-------|----------|
| Nome do algoritmo | A* Estrela |
| Arquivo de implementação | src/algorithms/a_star.py |
| Complexidade de tempo | O( ) |
| Complexidade de espaço | O( ) |

**Trecho do código com comentário de Big-O:**

```python
def a_star(graph, start, goal, heuristic):
    open_set = [(0, start)] # Fila de prioridade
    g_score = {node: float('inf') for node in graph} # O(V)
    g_score[start] = 0

    while open_set: # O(V) no pior caso
        current = heapq.heappop(open_set)[1] # O(log V)
        
        if current == goal:
            return reconstruct_path(came_from, current)

        for neighbor, weight in graph[current].items(): # O(E/V)
            tentative_g = g_score[current] + weight
            if tentative_g < g_score[neighbor]:
                g_score[neighbor] = tentative_g
                f_score = tentative_g + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor)) # O(log V)
```

---

## 3. Estrutura do Repositório

> Confirme que a estrutura implementada está de acordo com o E2.

```
Node-Conquest/
├── src/
│   ├── core/         
│   ├── algorithms/  
│   ├── utils/        
│   └── main.py      
├── tests/           
├── data/            
└── requirements.txt
```

**Desvios em relação ao E2** *(se houver)*:

---

## 4. Telas do MVP

> Insira screenshots ou gravações da interface funcionando.

### Tela de Entrada

![Tela de entrada](./assets/mvp_entrada.png)

*Descrição:*

### Tela de Resultado

![Tela de resultado](./assets/mvp_resultado.png)

*Descrição:*

---

## 5. Testes Unitários

| Algoritmo | Caso de teste | Status | Comando para executar |
|-----------|--------------|--------|----------------------|
| | Caso base | ✅ / ❌ | `pytest tests/test_algoritmo.py::test_caso_base` |
| | Grafo vazio | ✅ / ❌ | | pytest tests/test_a_star.py::test_empty_graph
| | Grafo completo | ✅ / ❌ | | pytest tests/test_a_star.py::test_no_path

**Como rodar todos os testes:**

```bash
pytest tests/
```

**Resultado atual:**
tests/test_a_star.py . . . [100%]
3 passed in 0.08s
```
# Cole aqui a saída do pytest / JUnit
```

---

## 6. Histórico de Commits

> Liste os 5+ commits mais relevantes desta entrega.

| Hash (7 chars) | Mensagem | Autor |
|----------------|----------|-------|
| `abc1234` | feat: implementa classe A* com heurística euclidiana |Luis Hardt |
| `def5678` | feat: estrutura da classe Graph e suporte a JSON |Miguel Pereira |
| `ghi9012` | test: test: adiciona 3 casos de teste para o A* |Bruna Jesus|
| `jkl3456` | feat: finaliza documentação do MVP e README |Luis Hardt |
| `mno7890` | feat: visualização do grafo usando Matplotlib |Luis Hardt |

---

## 7. O que está funcionando / O que ainda falta

| Funcionalidade | Status | Observação |
|---------------|--------|------------|
| Classe do grafo | ✅ Completo | |
| Algoritmo principal | ✅ Completo /  |
| Leitura de arquivo | ✅ Completo / |
| Tela de entrada | ✅ Completo / 🔄 Parcial | |
| Tela de resultado | ✅ Completo / |
| Testes unitários | ✅ Completo / |

---

## Checklist de Entrega

- [ ] Repositório público e acessível
- [ ] .gitignore configurado
- [ ] README com instruções de execução do MVP
- [ ] Algoritmo principal executando sem erros
- [ ] Tela de entrada e tela de resultado demonstráveis
- [ ] 3 testes unitários por algoritmo (mínimo caso base passando)
- [ ] ≥ 5 commits com prefixos semânticos (feat:, fix:, test:, docs:)
- [ ] Ao menos 1 arquivo de grafo de exemplo em `data/`

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
