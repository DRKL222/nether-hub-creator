import streamlit as st

st.title('NetherHubCreator')
st.markdown('Coloque as cordenadas do overworld! ')

cordenadas_x = st.number_input('digite a cordenadas x ', value=0, step=1)
cordenadas_z = st.number_input('digite a cordenadas z ', value=0, step=1)

if st.button('Calcular '):
    nether_x = cordenadas_x / 8
    nether_z = cordenadas_z / 8

    st.success('Resultado! ')
    st.write(nether_x)
    st.write(nether_z)