import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="wide")
st.image("logo.png", width=400)

st.markdown(
    """
    <style>
    .title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
    }
    </style>
    <div class="title">GESTÃO DE CONSUMO E FATURAMENTO DE ENERGIA</div>
    """, 
    unsafe_allow_html=True
)


# Menu expansível para Gerenciamento de Clientes
with st.expander("Gerenciamento de Clientes"):
    
    # Opções dentro do menu expansível
    menu_cliente = st.radio(
        "Escolha uma operação:",
        ("Adicionar Cliente", "Visualizar Clientes", "Obter informações de um Cliente", "Atualizar Cliente", "Deletar Cliente")
    )
    
    def show_response_message(response):
        if response.status_code == 200:
            st.success("Operação realizada com sucesso!")
        else:
            try:
                data = response.json()
                if "detail" in data:
                    if isinstance(data["detail"], list):
                        errors = "\n".join([error["msg"] for error in data["detail"]])
                        st.error(f"Erro: {errors}")
                    else:
                        st.error(f"Erro: {data['detail']}")
            except ValueError:
                st.error("Erro desconhecido. Não foi possível decodificar a resposta.")
    
    if menu_cliente == "Adicionar Cliente":
        with st.form("new_cliente"):
            name = st.text_input("Nome do Cliente")
            endereco = st.text_area("Endereço do Cliente")
            telefone = st.text_input("Telefone")
            email_cliente = st.text_input("Email do cliente")
            submit_button = st.form_submit_button("Adicionar Cliente")

            if submit_button:
                response = requests.post(
                    "http://backend:8000/cliente/",
                    json={
                        "nome": name,
                        "endereco": endereco,
                        "telefone": telefone,
                        "email_cliente": email_cliente,
                    },
                )
                show_response_message(response)

    elif menu_cliente == "Visualizar Clientes":
        if st.button("Exibir Todos os Clientes"):
            response = requests.get("http://backend:8000/cliente/")
            if response.status_code == 200:
                cliente = response.json()
                df = pd.DataFrame(cliente)
                df = df[[
                    "id_cliente",
                    "nome",
                    "endereco",
                    "telefone",
                    "email_cliente",
                    "data_cadastro"
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_cliente == "Obter informações de um Cliente":
        get_id = st.number_input("ID do Cliente", min_value=1, format="%d")
        if st.button("Buscar Cliente"):
            response = requests.get(f"http://backend:8000/cliente/{get_id}")
            if response.status_code == 200:
                cliente = response.json()
                df = pd.DataFrame([cliente])
                df = df[[
                    "id_cliente",
                    "nome",
                    "endereco",
                    "telefone",
                    "email_cliente",
                    "data_cadastro"
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_cliente == "Atualizar Cliente":
        cliente_id = st.number_input("ID do Cliente para Atualizar", min_value=1)
        new_endereco = st.text_area("Novo Endereço do Cliente")
        new_telefone = st.text_input("Novo Telefone")
        new_email_cliente = st.text_input("Novo Email do Cliente")

        update_button = st.button("Atualizar Cliente")
        if update_button:
            response = requests.put(
                f"http://backend:8000/cliente/{cliente_id}",
                json={
                    "endereco": new_endereco,
                    "telefone": new_telefone,
                    "email_cliente": new_email_cliente,
                },
            )
            show_response_message(response)

    elif menu_cliente == "Deletar Cliente":
        delete_id = st.number_input("ID do Cliente para Deletar", min_value=1)
        delete_button = st.button("Deletar Cliente")
        if delete_button:
            response = requests.delete(f"http://backend:8000/cliente/{delete_id}")
            show_response_message(response)


with st.expander("Gerenciamento de Medidores"):
    
    # Opções dentro do menu expansível
    menu_medidor = st.radio(
        "Escolha uma operação:",
        ("Adicionar Medidor", "Visualizar Medidores", "Obter informações de um Medidor", "Atualizar Medidor", "Deletar Medidor")
    )
    
    if menu_medidor == "Adicionar Medidor":
        with st.form("new_medidor"):
            cliente_id = st.number_input("ID do Cliente", min_value=1 ,format="%d")
            numero_medidor = st.number_input("Numero do Medidor", min_value=1, format="%d")
            tipo = st.selectbox("Novo Tipo",[
            
        "Medidor Eletromecânico",
        "Medidor Eletrônico",
        "Medidor Digital",
        "Medidor Monofásico",
        "Medidor Bifásico",
        "Medidor Trifásico",
        "Medidor Inteligente (Smart Meter)",
        "Medidor de Tarifa Branca",
        "Medidor de Média Tensão",
        "Medidor de Baixa Tensão",
        "Medidor de Alta Tensão"
],)
            submit_button = st.form_submit_button("Adicionar Medidor")

            if submit_button:
                response = requests.post(
                    "http://backend:8000/medidor/",
                    json={
                        "cliente_id": cliente_id,
                        "numero_medidor": numero_medidor,
                        "tipo": tipo,
                        
                    },
                )
                show_response_message(response)

    elif menu_medidor == "Visualizar Medidores":
        if st.button("Exibir Todos os Medidores"):
            response = requests.get("http://backend:8000/medidor/")
            if response.status_code == 200:
                medidor = response.json()
                df = pd.DataFrame(medidor)
                df = df[[
                    "id_medidor",
                    "cliente_id",
                    "numero_medidor",
                    "tipo",
                    "data_instalacao"
                    
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_medidor == "Obter informações de um Medidor":
        get_id = st.number_input("ID do Medidor", min_value=1, format="%d")
        if st.button("Buscar Medidor"):
            response = requests.get(f"http://backend:8000/medidor/{get_id}")
            if response.status_code == 200:
                medidor = response.json()
                df = pd.DataFrame([medidor])
                df = df[[
                    "id_medidor",
                    "cliente_id",
                    "numero_medidor",
                    "tipo",
                    "data_instalacao"
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_medidor == "Atualizar Medidor":
        id_medidor = st.number_input("ID do Medidor", min_value=1)
        cliente_id = st.number_input("ID do Cliente para Atualizar", min_value=1, format="%d")
        new_numero_medidor = st.number_input("Novo numero do Medidor", min_value=1, format="%d")
        new_tipo = st.selectbox("Novo Tipo",[
            
        "Medidor Eletromecânico",
        "Medidor Eletrônico",
        "Medidor Digital",
        "Medidor Monofásico",
        "Medidor Bifásico",
        "Medidor Trifásico",
        "Medidor Inteligente (Smart Meter)",
        "Medidor de Tarifa Branca",
        "Medidor de Média Tensão",
        "Medidor de Baixa Tensão",
        "Medidor de Alta Tensão"
],)

        
       

        update_button = st.button("Atualizar Medidor")
        if update_button:
            response = requests.put(
                f"http://backend:8000/medidor/{id_medidor}",
                json={
                    "cliente_id": cliente_id,
                    "numero_medidor": new_numero_medidor,
                    "tipo": new_tipo,
                },
            )
            show_response_message(response)

    elif menu_medidor == "Deletar Medidor":
        id_medidor = st.number_input("ID do Medidor para Deletar", min_value=1)
        delete_button = st.button("Deletar Medidor")
        if delete_button:
            response = requests.delete(f"http://backend:8000/medidor/{id_medidor}")
            show_response_message(response)


# Menu expansível para Gerenciamento de Leitura
with st.expander("Gerenciamento de Leitura"):
    
    # Opções dentro do menu expansível
    menu_leitura = st.radio(
        "Escolha uma operação:",
        ("Adicionar Leitura", "Visualizar Leituras", "Obter informações de uma Leitura", "Atualizar Leitura", "Deletar Leitura")
    )
    
    def show_response_message(response):
        if response.status_code == 200:
            st.success("Operação realizada com sucesso!")
        else:
            try:
                data = response.json()
                if "detail" in data:
                    if isinstance(data["detail"], list):
                        errors = "\n".join([error["msg"] for error in data["detail"]])
                        st.error(f"Erro: {errors}")
                    else:
                        st.error(f"Erro: {data['detail']}")
            except ValueError:
                st.error("Erro desconhecido. Não foi possível decodificar a resposta.")
    
    if menu_leitura == "Adicionar Leitura":
        with st.form("new_leitura"):
            cliente_id = st.number_input("Adicione o numero do medidor",  min_value=1)
            valor = st.number_input("Adicione a leitura em KWH")
            submit_button = st.form_submit_button("Adicionar Leitura")

            if submit_button:
                response = requests.post(
                    "http://backend:8000/leitura/",
                    json={
                        "medidor_id": medidor_id,
                        "leitura_kwh": leitura_kwh,
                       
                    },
                )
                show_response_message(response)

    elif menu_leitura == "Visualizar Leituras":
        if st.button("Exibir Todos os Leituras"):
            response = requests.get("http://backend:8000/leitura/")
            if response.status_code == 200:
                cliente = response.json()
                df = pd.DataFrame(cliente)
                df = df[[
                    "id_leitura",
                    "medidor_id",
                    "data_leitura",
                    "leitura_kwh"
                    
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_leitura == "Obter informações de uma Leitura":
        get_id = st.number_input("ID da Leitura", min_value=1, format="%d")
        if st.button("Buscar Leitura"):
            response = requests.get(f"http://backend:8000/leitura/{get_id}")
            if response.status_code == 200:
                cliente = response.json()
                df = pd.DataFrame([cliente])
                df = df[[
                    "id_leitura",
                    "medidor_id",
                    "leitura_kwh",
                    "data_leitura"
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_leitura == "Atualizar Leitura":
        cliente_id = st.number_input("ID da Leitura para Atualizar", min_value=1)
        new_medidor_id = st.number_input("Novo ID do Medidor",  min_value=1)
        new_leitura_kwh = st.number_input("Novo Leitura kwh",  min_value=1)
        

        update_button = st.button("Atualizar Leitura")
        if update_button:
            response = requests.put(
                f"http://backend:8000/leitura/{leitura_id}",
                json={
                    "medidor_id": new_medidor_id,
                    "leitura_kwh": new_leitura_kwh,
                },
            )
            show_response_message(response)

    elif menu_leitura == "Deletar Leitura":
        id_leitura = st.number_input("ID da Leitura para Deletar", min_value=1)
        delete_button = st.button("Deletar Leitura")
        if delete_button:
            response = requests.delete(f"http://backend:8000/leitura/{id_leitura}")
            show_response_message(response)



with st.expander("Gerenciamento de Fatura"):
    # Opções dentro do menu expansível
    menu_fatura = st.radio(
        "Escolha uma operação:",
        ("Adicionar Fatura", "Visualizar Faturas", "Obter informações de uma Fatura", "Atualizar Fatura", "Deletar Fatura")
    )
    
    def show_response_message(response):
        if response.status_code == 200:
            st.success("Operação realizada com sucesso!")
        else:
            try:
                data = response.json()
                if "detail" in data:
                    if isinstance(data["detail"], list):
                        errors = "\n".join([error["msg"] for error in data["detail"]])
                        st.error(f"Erro: {errors}")
                    else:
                        st.error(f"Erro: {data['detail']}")
            except ValueError:
                st.error("Erro desconhecido. Não foi possível decodificar a resposta.")
    
    if menu_fatura == "Adicionar Fatura":
        with st.form("new_fatura"):
            cliente_id = st.number_input("Adicione o ID do Cliente", min_value=1)
            valor = st.number_input("Adicione o Valor da Fatura")
            status_pagamento = st.selectbox("Novo Status de Pagamento", [
                "Pago",
                "A vencer",
                "Atrasado"
            ])

            submit_button = st.form_submit_button("Adicionar Fatura")

            if submit_button:
                response = requests.post(
                    "http://backend:8000/fatura/",
                    json={
                        "cliente_id": cliente_id,
                        "valor": valor,
                        "status_pagamento": status_pagamento
                    },
                )
                show_response_message(response)

    elif menu_fatura == "Visualizar Faturas":
        if st.button("Exibir Todas as Faturas"):
            response = requests.get("http://backend:8000/fatura/")
            if response.status_code == 200:
                faturas = response.json()
                df = pd.DataFrame(faturas)
                df = df[[
                    "id_fatura",
                    "cliente_id",
                    "mes_referencia",
                    "valor",
                    "status_pagamento",
                    "data_emissao",
                    "data_vencimento"
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_fatura == "Obter informações de uma Fatura":
        get_id = st.number_input("ID da Fatura", min_value=1, format="%d")
        if st.button("Buscar Fatura"):
            response = requests.get(f"http://backend:8000/fatura/{get_id}")
            if response.status_code == 200:
                fatura = response.json()
                df = pd.DataFrame([fatura])
                df = df[[
                    "id_fatura",
                    "cliente_id",
                    "mes_referencia",
                    "valor",
                    "status_pagamento",
                    "data_emissao",
                    "data_vencimento"
                ]]
                st.write(df.to_html(index=False), unsafe_allow_html=True)
            else:
                show_response_message(response)

    elif menu_fatura == "Atualizar Fatura":
        fatura_id = st.number_input("ID da Fatura para Atualizar", min_value=1)
        new_cliente_id = st.number_input("Novo ID do Cliente", min_value=1)
        new_valor = st.number_input("Novo Valor da Fatura", min_value=1)
        status_pagamento = st.selectbox("Novo Status de Pagamento", [
            "Pago",
            "A vencer",
            "Atrasado"
        ])

        update_button = st.button("Atualizar Fatura")
        if update_button:
            response = requests.put(
                f"http://backend:8000/fatura/{fatura_id}",
                json={
                    "cliente_id": new_cliente_id,
                    "valor": new_valor,
                    "status_pagamento": status_pagamento
                },
            )
            show_response_message(response)

    elif menu_fatura == "Deletar Fatura":
        id_fatura = st.number_input("ID da Fatura para Deletar", min_value=1)
        delete_button = st.button("Deletar Fatura")
        if delete_button:
            response = requests.delete(f"http://backend:8000/fatura/{id_fatura}")
            show_response_message(response)
