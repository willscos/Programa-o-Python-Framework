import streamlit as st

class Linguagem:
    def executar(self):
        return 'Executando Código...'

class Python(Linguagem):
    def executar(self):
        return "Executar Linguagem back e front"

class Go(Linguagem):
    def executar(self):
        return 'Linguagem de servidor e segurança'

class JS(Linguagem):
    def executar(self):
        return 'Linguagem para web'


st.title('POO - POLIMORFISMO')
st.write('Escolha uma...')

opcao = st.selectbox(
    'Escolha a Linguagem',
    ['Python', 'Go', 'JS']
)

if opcao == 'Python':
    linguagem = Python()
elif opcao == 'Go':
    linguagem = Go()
else:  # opcao == 'JS'
    linguagem = JS()

st.subheader('RESULTADO')
st.success(linguagem.executar())
st.balloons()

