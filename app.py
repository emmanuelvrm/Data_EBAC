
import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. Título e texto
st.title('Demonstração de Funcionalidades do Streamlit')
st.write('Esta aplicação demonstra diversas funcionalidades do Streamlit.')

# 2. Exibição de DataFrame
df = pd.DataFrame({
    'Coluna 1': [1, 2, 3, 4],
    'Coluna 2': [10, 20, 30, 40]
})
st.write('Exemplo de DataFrame:')
st.dataframe(df)

# 3. Gráfico de linha
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)
st.line_chart(chart_data)

# 4. Slider
x = st.slider('Selecione um valor para X', 0, 100, 50)
st.write(f'Você selecionou: {x}')

# 5. Entrada de texto
nome = st.text_input('Digite seu nome', 'Visitante')
st.write(f'Olá, {nome}!')

# 6. Checkbox
if st.checkbox('Mostrar gráfico de área'):
    st.area_chart(chart_data)

# 7. Barra lateral
st.sidebar.write('Esta é a barra lateral.')
opcao = st.sidebar.selectbox(
    'Selecione uma opção:',
    ['Opção 1', 'Opção 2', 'Opção 3']
)
st.sidebar.write(f'Você selecionou: {opcao}')

# 8. Barra de progresso
st.write('Barra de progresso:')
progresso = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progresso.progress(i + 1)

# 9. Mensagem de sucesso
st.success('Operação realizada com sucesso!')

# 10. Mensagem de aviso
st.warning('Este é um aviso.')

# 11. Mensagem de erro
st.error('Ocorreu um erro.')

# 12. Código
st.code("""x = 10
print(x)""", language='python')

# 13. Texto em Markdown
st.markdown('**Texto em negrito** e *itálico*.')

# 14. Exibição de imagem
st.image('https://docs.streamlit.io/en/stable/_static/logo.png', caption='Logo do Streamlit')

# 15. Exibição de vídeo
st.video('https://www.youtube.com/watch?v=LMD6MqwErzc')

# 16. Exibição de áudio
st.audio('https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3')

# 17. Mapa
mapa_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon']
)
st.map(mapa_data)

# 18. Seleção múltipla
opcoes = st.multiselect(
    'Quais são suas cores favoritas?',
    ['Verde', 'Amarelo', 'Vermelho', 'Azul'],
    ['Verde', 'Amarelo']
)
st.write('Você selecionou:', opcoes)

# 19. Botão
if st.button('Clique aqui'):
    st.write('Botão clicado!')

# 20. Data e hora
data = st.date_input('Selecione uma data', pd.to_datetime('2023-01-01'))
hora = st.time_input('Selecione um horário', pd.to_datetime('12:00').time())
st.write(f'Data selecionada: {data}')
st.write(f'Horário selecionado: {hora}')

