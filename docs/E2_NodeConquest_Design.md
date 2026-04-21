# E2 — Design Técnico, Arquitetura e Backlog

> **Disciplina:** Teoria dos Grafos  
> **Prazo:** 13 de abril de 2026  
> **Peso:** 20% da nota final  

---

## Identificação do Grupo

| Grupo: Node Conquest | |
| [Repositório GitHub](https://github.com/Luis-Hardt/Node-Conquest.git) | |
| Bruna Alves de Jesus | 40420418 |
| Luis Fernando Barcelos Hardt | 38774631 |
| Miguel da Silva Pereira | 41005422 |

---

## 1. Algoritmos Escolhidos

### 1.1 Algoritmo Principal

| Campo | Resposta |
|-------|----------|
| Algoritmo A* (A-Estrela) | |
| Categoria | Busca |
| Complexidade de tempo | O(b^d) |
| Complexidade de espaço | O(V) |
| Problema que resolve | Busca de menor caminho em grafos ponderados |

**Por que este algoritmo foi escolhido?**

O  algoritmo A* permite que os agentes em jogos de estratégia encontrem rotas de forma mais natural e eficiente. Ele é ideal pois utiliza uma função heurística para guiar a busca, reduzindo o tempo de processamento comparado a outros algoritmos de busca, o que evita quedas de FPS em simulações com múltiplos agentes.

**Alternativa descartada e motivo:**

| Algoritmo alternativo | Motivo da exclusão |
|----------------------|-------------------|
| Busca em largura (BFS) | Ignora os pesos das arestas/vértices |
| Dijkstra | Não é ideal para grafos ponderados |

**Limitações no contexto do problema:**

O desempenho do A* é altamente dependente da escolha de função heurística. Em coordenadas hexagonais, o uso de heurísticas euclidianas comuns pode gerar má otimização. Além disso, o custo de memória é elevado pois ele mantém todos os nós visitados na lista aberta/fechada.

**Referência bibliográfica:**

> CORMEN, T. H. et al. Algoritmos: teoria e prática. 3. ed. Rio de Janeiro: Elsevier, 2012.

---

## 2. Arquitetura em Camadas

![Diagrama de arquitetura](./docs/E2_NodeConquest_DiagramaArquitetura)

### Descrição das camadas

| Camada | Responsabilidade | Artefatos principais |
|--------|-----------------|----------------------|
| Apresentação (UI/CLI) | Interface gráfica com Pygame, renderização da grade e visualização do caminho | renderer.py |
| Aplicação (Service) | Organização das ações do usuário, como iniciar a busca e mover os agentes | main.py |
| Domínio (Core) | Estruturas de dados fundamentais e lógica matemática do algoritmo A* | a_star.py, graph.py, node.py |
| Infraestrutura (I/O) | Carregamento e salvamento dos mapas (datasets) em arquivos de disco |  data_manager.py |

---

## 3. Estrutura de Diretórios

```
node-conquest-terrarium/
├── docs/
│   ├── E1_NodeConquest_Visao.md
│   └── E2_NodeConquest_Design.md
├── src/
│   ├── core/
│   │   ├── graph.py          # Representação por matriz 2D
│   │   └── node.py           # Vértices
│   ├── algorithms/
│   │   └── a_star.py         # Implementação do algoritmo A* 
│   ├── ui/
│   │   └── renderer.py       # Renderização Pygame 
│   ├── io/
│   │   └── data_manager.py   # Leitura/Escrita de JSON
│   └── main.py
├── data/
│   └── maps/                 # Arquivos de mapas
└── requirements.txt          # Dependência: Pygame
```

---

## 4. Definição do Dataset

JSON. O arquivo descreve a dimensão da grade e uma lista de objetos representando cada célula com seus dados, como o peso associado.

```json
{
  "grid_width": 20,
  "grid_height": 20,
  "cells": [
    { "q": 0, "r": 0, "type": "plain", "weight": 1 },
    { "q": 0, "r": 1, "type": "forest", "weight": 2 }
  ]
}
```

**Estratégia de geração aleatória:**

| Parâmetro | Descrição |
|-----------|-----------|
| Número de vértices | Definido pela grade escolhida pelo usuário |
| Densidade | Change de uma célula ser gerada como obstáculo impassável |
| Faixa de pesos | Atribuição aleatória de pesos entre 1 (planície) e 3 (colicas com floresta/lago) |

---

## 5. Backlog do Projeto

### 5.1 In-Scope — O que será implementado

| # | Funcionalidade | Prioridade | Critério de aceite |
|---|---------------|------------|-------------------|
| 1 | Renderização hexagonal | Alta | Dado um tamanho de grade, quando o sistema inicia, então deve exibir hexágonos conectados bidimensionalmente |
| 2 | Cálculo com algoritmo A* | Alta | Dado um ponto de origem e destino, quando o algoritmo é executado, então deve retornar a rota de menor custo |
| 3 | Sistema de Pesos | Alta | Dado um caminho que atravessa floresta/colina (peso 2), quando calculado o total, então o custo deve ser superior a uma rota equivalente em planície |
| 4 | Editor de terrenos | Média | Dado um input em uma célula, quando o usuário altera o tipo, então o peso do vértice deve ser atualizado no grafo |
| 5 | Visualização de custo | Baixo | Dado um caminho finalizado, quando renderizado, então o sistema deve exibir o valor numérico do custo total na UI |

### 5.2 Out-of-Scope — O que NÃO será feito

| Funcionalidade excluída | Motivo |
|------------------------|--------|
| Multiplayer | Aumentaria a complexidade de rede além do escopo da disciplina de grafos |
| Animações e gráficos | O foco é a demonstração de algoritmos de busca, não mecânicas visuais avançadas |
| Complexidade das IAs | O projeto foca no movimento individual imediato entre dois pontos |

---

*Teoria dos Grafos — Profa. Dra. Andréa Ono Sakai*
