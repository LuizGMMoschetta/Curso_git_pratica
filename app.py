import streamlit as st
from src.extraction import loud_data

st.set_page_config(layout='wide')

def main():
    df_row = loud_data()

    st.dataframe(df_row)

if __name__ == '__main__':
    main()