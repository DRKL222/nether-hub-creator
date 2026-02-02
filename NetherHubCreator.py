import streamlit as st

st.title('NetherHubCreator')

tab1, tab2 = st.tabs(["Overworld → Nether", "Nether → Overworld"])

with tab1:
    st.markdown('### Coloque as coordenadas do Overworld!')
    
    cordenadas_x = st.number_input('Digite a coordenada X:', value=0, step=1, key='ow_x')
    cordenadas_z = st.number_input('Digite a coordenada Z:', value=0, step=1, key='ow_z')
    
    if st.button('Calcular Nether', key='calc_nether'):
        nether_x = cordenadas_x / 8
        nether_z = cordenadas_z / 8
        
        st.success(' Resultado!')
        st.write(f'**Coordenada X no Nether:** {nether_x:.2f}')
        st.write(f'**Coordenada Z no Nether:** {nether_z:.2f}')

with tab2:
    st.markdown('### Coloque as coordenadas do Nether!')
    
    cordenadas_xnether = st.number_input('Digite a coordenada X:', value=0, step=1, key='nether_x')
    cordenadas_znether = st.number_input('Digite a coordenada Z:', value=0, step=1, key='nether_z')
    
    if st.button('Calcular Overworld', key='calc_overworld'):
        overworld_x = cordenadas_xnether * 8
        overworld_z = cordenadas_znether * 8
        
        st.success(' Resultado!')
        st.write(f'**Coordenada X no Overworld:** {overworld_x}')
        st.write(f'**Coordenada Z no Overworld:** {overworld_z}')
