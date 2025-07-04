import streamlit as st
import pandas as pd

# 1. Título da aplicação
st.title('Otimização do Kit de Primeiros‑Socorros')

# 2. Tabela de itens disponíveis
items = {
    'ID':     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'Nome':   ['Ataduras', 'Seringas/Agulhas', 'Desfibrilador Portátil',
               'Analgésicos Fortes', 'Solução Salina', 'Antisséptico',
               'Gesso Leve', 'Kit de Sutura', 'Monitor de Sinais Vitais',
               'Cobertor Térmico'],
    'Peso':   [1, 1, 3, 1, 2, 1, 2, 1, 4, 1],   # kg (inteiros p/ DP)
    'Valor':  [30, 25, 90, 40, 50, 20, 60, 35, 100, 45]  # importância
}
df = pd.DataFrame(items)

st.subheader('Itens Médicos Disponíveis')
st.table(df)

# 3. Entrada do usuário: capacidade da mochila
st.sidebar.header('Parâmetros da Missão')
capacidade = st.sidebar.number_input('Capacidade da Mochila (kg)',
                                     min_value=1, max_value=20, value=10)

# 4. Função de Programação Dinâmica para Knapsack 0‑1
def knapsack(pesos, valores, W):
    n = len(pesos)
    dp = [[0]*(W+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for w in range(W+1):
            if pesos[i-1] <= w:
                dp[i][w] = max(dp[i-1][w],
                               dp[i-1][w-pesos[i-1]] + valores[i-1])
            else:
                dp[i][w] = dp[i-1][w]

    # Recuperar solução
    valor_max = dp[n][W]
    w = W
    selecionados = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selecionados.append(i-1)
            w -= pesos[i-1]
    selecionados.reverse()
    return valor_max, selecionados

# 5. Botão para otimizar
if st.sidebar.button('Otimizar Kit'):
    valor_max, sel = knapsack(df['Peso'].tolist(),
                              df['Valor'].tolist(),
                              capacidade)

    st.subheader('Resultado da Otimização')
    st.write(f'**Cobertura total obtida:** {valor_max}')
    st.write(f'**Peso total utilizado:** {sum(df.loc[sel, "Peso"])} kg')

    st.write('**Itens Selecionados:**')
    st.table(df.loc[sel].reset_index(drop=True))

    st.success('Otimização concluída com sucesso!')
