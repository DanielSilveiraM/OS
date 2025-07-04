# Otimização do Kit de Primeiros‑Socorros

Este projeto é uma aplicação interativa desenvolvida com **Python** e **Streamlit**, que utiliza **Programação Dinâmica** para resolver o problema da **Mochila 0-1 (Knapsack)** no contexto de uma **missão de resgate em região remota**.

## Cenário

Uma equipe de resgate tem uma **capacidade limitada** de carga em suas mochilas e precisa decidir **quais itens médicos levar**. Cada item tem um **peso** e uma **pontuação de importância** (refletindo sua utilidade em emergências).

### Objetivo:
Selecionar o **conjunto de itens médicos** que **maximiza a cobertura de emergência** sem ultrapassar o peso máximo da mochila.

---

## Tecnologias Utilizadas

- Python 3.x  
- Streamlit  
- Pandas  

---

## Como Executar o Projeto

1. **Clone o repositório** ou copie o código `app.py`:
    ```bash
    git clone https://github.com/seu-usuario/otimizacao-kit-primeiros-socorros.git
    cd otimizacao-kit-primeiros-socorros
    ```

2. **Instale as dependências**:
    ```bash
    pip install streamlit pandas
    ```

3. **Execute o aplicativo**:
    ```bash
    streamlit run app.py
    ```

4. **Abra no navegador**:
    O Streamlit abrirá automaticamente uma aba. Caso não abra, acesse:  
    ```
    http://localhost:8501
    ```

---

## Capturas de Tela

| Página Principal | Resultado da Otimização |
|------------------|--------------------------|
| ![](img/home.png) | ![](img/resultado.png)  |

> *(Imagens meramente ilustrativas – adicione prints do seu app real no diretório `img/`)*

---

## Exemplo de Itens

| Nome                 | Peso (kg) | Valor (Importância) |
|----------------------|-----------|----------------------|
| Ataduras             | 1         | 30                   |
| Desfibrilador Portátil | 3         | 90                   |
| Cobertor Térmico     | 1         | 45                   |
| ...                  | ...       | ...                  |

---

## Algoritmo Usado

O algoritmo implementado é a **Programação Dinâmica para o problema da Mochila 0-1**, com complexidade O(n × W), onde:
- `n`: número de itens
- `W`: capacidade da mochila (em kg)

Este método garante uma **solução ótima**.

---

## Possíveis Extensões

- Adição de restrições de volume.
- Suporte para itens fracionáveis (knapsack contínuo).
- Comparação com algoritmos heurísticos (guloso, branch and bound).
- Exportação dos resultados em PDF ou Excel.

---

## Licença

Este projeto é de uso educacional e livre para modificações e melhorias.

---

## Contribuição

Sinta-se à vontade para sugerir melhorias, abrir *issues* ou enviar *pull requests*!

---
