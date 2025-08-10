import streamlit as st

precos_ingredientes = {
    "Bife Cru Premium": {"preco": 200, "imagem": "images/bife.png"},
    "Lagosta Crua": {"preco": 370, "imagem": "images/lagosta.png"},
    "Camarão Cru": {"preco": 300, "imagem": "images/camarao.png"},
    "Carne Crua de Coelho": {"preco": 186, "imagem": "images/carne.png"},
    "Peixe Cru": {"preco": 50, "imagem": "images/peixe.png"},
    "Atum": {"preco": 86, "imagem": "images/atum.png"},
    "Ostra": {"preco": 360, "imagem": "images/ostra.png"},
    "Bacon": {"preco": 10, "imagem": "images/bacon.png"},
    "Ovos": {"preco": 10, "imagem": "images/ovo.png"},
    "Manteiga": {"preco": 40, "imagem": "images/manteiga.png"},
    "Folhas Verdes": {"preco": 15, "imagem": "images/folhas.png"},
    "Alface": {"preco": 20, "imagem": "images/alface.png"},
    "Tomates": {"preco": 10, "imagem": "images/tomates.png"},
    "Limão": {"preco": 10, "imagem": "images/limao.png"},
    "Água": {"preco": 5, "imagem": "images/agua.png"},
    "Vinho Branco": {"preco": 700, "imagem": "images/vinho.png"},
    "Cogumelo": {"preco": 20, "imagem": "images/cogumelo.png"},
    "Trufa Branca": {"preco": 250, "imagem": "images/trufa.png"},
    "Sal": {"preco": 10, "imagem": "images/sal.png"},
    "Pimenta": {"preco": 15, "imagem": "images/pimenta.png"},
    "Arroz": {"preco": 10, "imagem": "images/arroz.png"},
    "Alho": {"preco": 10, "imagem": "images/alho.png"},
    "Batata": {"preco": 10, "imagem": "images/batata.png"},
    "Azeite": {"preco": 15, "imagem": "images/azeite.png"},
    "Cebola": {"preco": 10, "imagem": "images/cebola.png"},
    "Creme de Leite": {"preco": 20, "imagem": "images/creme.png"},
    "Pasta": {"preco": 10, "imagem": "images/pasta.png"},
    "Queijo": {"preco": 15, "imagem": "images/queijo.png"},
    "Carne de Carangueijo": {"preco": 400, "imagem": "images/carangueijo.png"},
    "Polvo Cru": {"preco": 500, "imagem": "images/polvo.png"},
    "Galinha": {"preco": 300, "imagem": "images/galinha.png"},
    "Carne de Cordeiro Crua": {"preco": 650, "imagem": "images/cordeiro.png"},
}

receitas = {
    "Frango Teriyaki": {
        "ingredientes": {
            "Galinha": 5,
            "Pimenta": 1,
            "Tomates": 3,
            "Sal": 2,
            "Azeite": 6,
            "Folhas Verdes": 3,
            "Alho": 3,
            "Trufa Branca": 3,
            "Creme de Leite": 3,
        },
        "imagem": "images/frango_teriyaki.png"
    },
    "Paella de Camarão": {
        "ingredientes": {
            "Camarão Cru": 8,
            "Arroz": 2,
            "Folhas Verdes": 1,
            "Tomates": 1,
            "Azeite": 1,
            "Pimenta": 1,
            "Água": 3,
            "Sal": 1,
            "Trufa Branca": 3
        },
        "imagem": "images/paella_de_camarao.png"
    }
}

def calcular_ingredientes(food, quantidade):
    total_ingredientes = {}
    total_custo = 0
    
    for ing, qtd in receitas[food]["ingredientes"].items():
        if ing not in total_ingredientes:
            total_ingredientes[ing] = 0
        total_ingredientes[ing] += qtd * quantidade
        total_custo += precos_ingredientes[ing]["preco"] * qtd * quantidade
        
    return total_ingredientes, total_custo

st.title("🍽️ Craft de Food")

comida = st.selectbox("Selecione a comida:", list(receitas.keys()))
st.image(receitas[comida]["imagem"], width=50)

quantidade = st.number_input("Quantidade:", min_value=1, value=1)

if st.button("Calcular"):
    total_ingredientes, total_custo = calcular_ingredientes(comida, quantidade)

    st.subheader(f"Ingredientes para {quantidade}x {comida}:")
    st.write(f"Custo total: **{total_custo/1000:.2f}K Berries**")
    
    for ing, qtd in total_ingredientes.items():
        col1, col2, col3 = st.columns([0.1, 0.4, 1])
        
        with col1:
            st.image(precos_ingredientes[ing]["imagem"], width=30)
        
        with col2:
            st.markdown(f"**{ing}**")
        
        with col3:
            st.markdown(f"**{qtd}x**")