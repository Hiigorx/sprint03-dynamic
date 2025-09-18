
# Sprint 03 - Dynamic Programming: Controle de Consumo de Insumos

## 👥 Integrantes
- Fabricio Bettarello - RM 554638  
- Eric Yuji - RM 554869  
- Kaue Pires - RM 554403  
- Higor Batista - RM 558907  
- Ricardo Di Tilia - RM 555155  
- Enzo Miletta - RM 98677  

---

## 📌 Descrição
Projeto da **Sprint 03** com foco em aplicar **estruturas de dados** e **algoritmos clássicos** para organizar o consumo diário de insumos em unidades de diagnóstico. O objetivo é melhorar o **controle de estoque** e a **previsão de reposição**.  

---

## ⚙️ Funcionalidades
- **Fila (FIFO):** registra o consumo em ordem cronológica.  
- **Pilha (LIFO):** consulta os últimos consumos primeiro.  
- **Busca Sequencial:** percorre todos os registros até encontrar o insumo.  
- **Busca Binária:** busca otimizada em lista ordenada.  
- **Merge Sort:** ordena por quantidade.  
- **Quick Sort:** ordena por validade.  

---

## 📊 Fluxo
1. Simulação de consumo de insumos (nome, quantidade, validade, dia).  
2. Registros armazenados em fila e pilha.  
3. Consultas e buscas de insumos específicos.  
4. Ordenação com Merge Sort e Quick Sort.  
5. Exibição dos resultados no console.  

---

## 🖥️ Execução
```bash
git clone https://github.com/Hiigorx/sprint03-dynamic
python main.py
```

---

## 📊 Relatório

### 💻 Código no GitHub
Todo o código do projeto está neste repositório, organizado para representar as estruturas de dados e algoritmos solicitados:
- **Fila** → controle cronológico de consumo.
- **Pilha** → consulta dos últimos registros primeiro.
- **Busca** → localizar insumos específicos.
- **Ordenação** → organizar dados para análise.

---

### 🛠️ Explicação das Estruturas e Algoritmos

#### 🟦 Fila (Queue)
A fila foi usada para registrar o **consumo diário de insumos em ordem cronológica**, simulando a entrada de cada consumo conforme o dia passa.  
Isso permite analisar padrões de demanda ao longo do tempo.

#### 🟥 Pilha (Stack)
A pilha foi utilizada para **consultar os consumos mais recentes primeiro**.  
No contexto real, gestores muitas vezes precisam verificar os últimos dias de consumo para prever necessidades imediatas, e a pilha facilita esse acesso invertendo a ordem dos registros.

#### 🔍 Estruturas de Busca
- **Busca Sequencial**: percorre todos os insumos até encontrar o procurado.  
  Útil em listas pequenas ou não ordenadas.  
- **Busca Binária**: aplicada após ordenação, permite encontrar rapidamente um insumo específico.  
  Representa a necessidade de localizar um item no estoque de forma **mais eficiente**.

#### 🔄 Algoritmos de Ordenação
- **Merge Sort**: organiza os insumos por **quantidade consumida**.  
  Algoritmo eficiente e estável, garantindo que itens com o mesmo valor mantenham a ordem.  
- **Quick Sort**: ordena os insumos por **validade**, simulando a gestão de estoque onde itens com vencimento próximo precisam de prioridade.

---

### 🎯 Conclusão
O projeto simula a realidade de uma unidade de diagnóstico onde o controle de insumos é essencial.  
Cada estrutura e algoritmo foi escolhido para resolver problemas práticos:
- **Fila**: registro histórico.  
- **Pilha**: acesso rápido aos últimos consumos.  
- **Busca**: localizar insumos de forma simples ou eficiente.  
- **Ordenação**: análise e priorização de estoque.

Dessa forma, fica claro como **estruturas de dados e algoritmos clássicos auxiliam diretamente na gestão de estoque e previsão de reposição**.
