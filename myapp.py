import streamlit as st
st.set_page_config(page_title='Cats')
st.header("Types of Dogs")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Husky")
  st.image("./Husky.jpeg", caption="Husky", width=300,use_column_width=True)
  st.write("Persian cats are cute")
with col2:
  st.subheader("Golden Retriver")
  st.image("./Golden Retriver.jpeg", caption="Ragdoll Cat", width=300,use_column_width=True)
  st.write("Ragdoll cats are proud")
