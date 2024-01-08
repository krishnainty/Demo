import streamlit as st
st.set_page_config(page_title='Dogs')
st.header("Types of Dogs")

col1, col2 = st.columns(2)
with col1:
  st.subheader("Husky")
  st.image("./Husky.jpeg", caption="Husky",height=300, width=300,use_column_width=True)
  st.write("Husky dogs are cute")
with col2:
  st.subheader("Golden Retriver")
  st.image("./Golden Retriver.jpeg", caption="Ragdoll Cat",height=300, width=300,use_column_width=True)
  st.write("Golden Retriver are friendly")
