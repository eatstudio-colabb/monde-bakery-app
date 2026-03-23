import streamlit as st

# Page settings
st.set_page_config(page_title="Monde Bakery Calculator", layout="wide")

st.title("Monde Bakery - Focaccia Calculator")
st.markdown("---")

# --- SIDEBAR: SETTINGS ---
st.sidebar.header("1. Baking Settings")
antal = st.sidebar.number_input("Number of loaves", min_value=1, value=1, step=1)
vikt_per_st = st.sidebar.number_input("Weight per loaf (grams)", min_value=100, value=5002, step=50)
forsaljningspris = st.sidebar.number_input("Selling price per unit (LKR)", value=9000)

st.sidebar.header("2. Raw Material Prices (LKR/kg)")
pris_mjol = st.sidebar.number_input("Wheat Flour (price/kg)", value=224.0)
pris_salt = st.sidebar.number_input("Salt (price/kg)", value=100.0)
pris_olja = st.sidebar.number_input("Olive Oil (price/kg)", value=1500.0)

# --- LOGIC & DATA ---
total_vikt_kg = (antal * vikt_per_st) / 1000

# Percentage distribution based on your Excel file
recept_data = {
    "Wheat Flour": {"ratio": 0.4655, "price": pris_mjol},
    "Water": {"ratio": 0.3335, "price": 0.0},
    "Sourdough": {"ratio": 0.1817, "price": 0.0},
    "Salt": {"ratio": 0.0111, "price": pris_salt},
    "Olive Oil": {"ratio": 0.0082, "price": pris_olja}
}

# --- LAYOUT: RESULTS ---
col1, col2 = st.columns(2)

with col1:
    st.subheader("Recipe")
    total_kostnad = 0
    for name, info in recept_data.items():
        weight_kg = total_vikt_kg * info["ratio"]
        cost = weight_kg * info["price"]
        total_kostnad += cost
        
        # Unit formatting (kg or grams)
        if weight_kg >= 1:
            st.write(f"**{name}:** {weight_kg:.2f} kg")
        else:
            st.write(f"**{name}:** {weight_kg*1000:.0f} g")

with col2:
    st.subheader("Economics (LKR)")
    total_revenue = forsaljningspris * antal
    profit = total_revenue - total_kostnad
    margin = (profit / total_revenue) * 100 if total_revenue > 0 else 0
    
    st.metric("Total Ingredient Cost", f"{total_kostnad:.0f} LKR")
    st.metric("Estimated Profit", f"{profit:.0f} LKR", delta=f"{margin:.1f}% margin")
    
    st.info(f"Cost per loaf: {total_kostnad/antal:.2f} LKR")

st.divider()
st.caption("Calculations based on Monde Bakery original sourdough focaccia recipe.")

