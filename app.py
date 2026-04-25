import streamlit as st
import pandas as pd
import numpy as np

# st.title('ISSO É UM TESTE')

import streamlit as st
import pandas as pd

st.title("ISSO É UM TESTE")

dados = {
    'dia': [1, 2, 3, 4, 5],
    'vendas': [500, 450, 200, 150, 1000]
}

df_exemplo = pd.DataFrame(dados)

if st.button('Gerar gráfico (exemplo)', key="btn_exemplo"):
    st.line_chart(df_exemplo.set_index('dia'))

# --------------------------------------------------------

st.title('Ler o CSV')

arquivo = st.file_uploader('Enviar CSV', type=["csv"])

if arquivo is not None:
    # tente primeiro com vírgula; se seu CSV for ; troque sep=","
    df = pd.read_csv(arquivo)

    st.write('Dados do CSV:')
    st.dataframe(df)

    if st.button('Gerar gráfico (CSV)', key="btn_csv"):
        # plota apenas colunas numéricas
        df_num = df.select_dtypes(include="number")
        if df_num.empty:
            st.warning("Não encontrei colunas numéricas para plotar.")
        else:
            st.line_chart(df_num)
