import streamlit as st


# herança e poliformismo ...


class Linguagem:
    def executar(self):
        return 'Executando codigo ...'


class Python(Linguagem):
    def executar(self):
        return 'Executar linguagem back e front'    


class Go(Linguagem):
    def executar(self):
        return 'Linguagem de servidor e segurança ...'


class JS(Linguagem):
    def executar(self):
        return 'Linguagem para web ...'      



st.title('poo -  POLIFORMISMO')
st.write('Escolha uma ...')


opcao = st.selectbox(


        'escolha a linguagem',
        ['Python', 'Go', 'JS']


)
if opcao == 'Python':
    linguagem = Python()
elif opcao == 'Go':
    linguagem = Go()
elif opcao == 'JS':
    linguagem = JS()



st.subheader('RESULTADO')
st.success(linguagem.executar())
st.balloons()


# st.camera_input()   


enable = st.checkbox("Enable camera")
picture = st.camera_input('teste',  label_visibility="visible" ,args=[])


if picture:
    st.image(picture)