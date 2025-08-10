import streamlit as st

precos_ingredientes = {
    "Bife Cru Premium": 200,
    "Lagosta Crua": 370,
    "Camarão Cru": 300,
    "Carne Crua de Coelho": 186,
    "Peixe Cru": 50,
    "Atum": 86,
    "Ostra": 360,
    "Bacon": 10,
    "Ovos": 10,
    "Manteiga": 40,
    "Folhas Verdes": 15,
    "Alface": 20,
    "Tomates": 10,
    "Limão": 10,
    "Água": 5,
    "Vinho Branco": 700,
    "Cogumelo": 20,
    "Trufa Branca": 250,
    "Sal": 10,
    "Pimenta": 15,
    "Arroz": 10,
    "Alho": 10,
    "Batata": 10,
    "Azeite": 15,
    "Cebola": 10,
    "Creme de Leite": 20,
    "Pasta": 10,
    "Queijo": 15,
    "Carne de Carangueijo": 400,
    "Polvo Cru": 500,
    "Galinha": 300,
    "Carne de Cordeiro Crua": 650
}

receitas = {
    "Frango Teriyaki": {
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
    "Paella de Camarão": {
        "Camarão Cru": 8,
        "Arroz": 2,
        "Folhas Verdes": 1,
        "Tomates": 1,
        "Azeite": 1,
        "Pimenta": 1,
        "Água": 3,
        "Sal": 1,
        "Trufa Branca": 3
    }
}

def calcular_ingredientes(food, quantidade):
    total_ingredientes = {ing: 0 for ing in precos_ingredientes.keys()}
    total_custo = 0

    for ing, qtd in receitas[food].items():
        total_ingredientes[ing] += qtd * quantidade
        total_custo += precos_ingredientes[ing] * qtd * quantidade

    return total_ingredientes, total_custo

st.title("🍽️ Craft de Food")

comida = st.selectbox("Selecione a comida:", list(receitas.keys()))
quantidade = st.number_input("Quantidade:", min_value=1, value=1)

if st.button("Calcular"):
    total_ingredientes, total_custo = calcular_ingredientes(comida, quantidade)

    ingredientes_usados = [(ing, total_ingredientes[ing]) for ing in precos_ingredientes.keys() if total_ingredientes[ing] > 0]
    
    max_len = max(len(ing) for ing, _ in ingredientes_usados)

    linhas = []
    for ing, qtd in ingredientes_usados:
        linhas.append(f"{ing.ljust(max_len)} : {qtd}x")

    st.subheader(f"Ingredientes para {quantidade}x {comida}:")
    
    st.code("\n".join(linhas), language='text')

    st.subheader("💰 Custo total:")
    st.write(f"{total_custo/1000:.2f}K Berries")
