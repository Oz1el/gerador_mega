import hashlib
import random
import streamlit as st
from datetime import datetime

def generate_numbers(name, birthdate):
    seed = name + birthdate
    hash_object = hashlib.sha256(seed.encode())
    hex_dig = hash_object.hexdigest()
    random.seed(int(hex_dig, 16))
    numbers = sorted(random.sample(range(1, 61), 6))
    return numbers

st.set_page_config(initial_sidebar_state="collapsed")

st.title("Bem-vindo ao Gerador de Números para a Mega")
st.write("Por favor, insira seu nome e data de nascimento no formato dd/mm/yyyy para gerar uma sequência de 6 números.")

name = st.text_input("Nome")
birthdate = (st.date_input(
    "Data de Nascimento",
    value=datetime.now(),
    min_value=datetime(1900, 1, 1),
    max_value=datetime.now(),
    format="DD/MM/YYYY"
)).strftime('%d/%m/%Y')

if st.button("Gerar Números"):
    if name and birthdate:
        try:
            # Validação do formato dd/mm/yyyy
            date_obj = datetime.strptime(birthdate, "%d/%m/%Y")
            # Converte para o formato yyyy-mm-dd
            formatted_birthdate = date_obj.strftime("%Y-%m-%d")
            numbers = generate_numbers(name, formatted_birthdate)
            formatted_numbers = ", ".join(map(str, numbers))  # Formata a saída
            st.write(f"Os números gerados são: {formatted_numbers}")
        except ValueError:
            st.write("Por favor, insira a data de nascimento no formato dd/mm/yyyy.")
    else:
        st.write("Por favor, preencha todos os campos.")