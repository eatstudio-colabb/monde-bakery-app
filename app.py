import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Gör huvudrubriken tunnare */
    h1 {
        font-weight: 300 !important;
        letter-spacing: -0.5px;
    }
    
    /* Styling för Sourdough Guide-knappen (Expander) */
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 2px solid #FF4B4B;
        border-radius: 10px;
        background-color: #FF4B4B; /* Bakgrundsfärg på själva "knappen" */
    }
    
    /* Textfärg inuti expander-knappen när den är stängd */
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: white !important;
        font-weight: 600 !important;
    }
    
    /* Styling för innehållet när expandern öppnas */
    div[data-testid="stSidebar"] [data-testid="stExpanderDetails"] {
        background-color: white;
        color: black;
        border-radius: 0 0 8px 8px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Monde Bakery - Professional Recipe Master")

# --- RECEPTDATABAS ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            "Dough: Wheat Flour": 0.3350, "Dough: Milk": 0.2577, "Dough: Sourdough": 0.1289,
            "Dough: Cold Butter": 0.0805, "Dough: Sugar": 0.0548, "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045, "Filling: Butter": 0.0967, "Filling: Sugar": 0.0290, "Filling: Cinnamon": 0.0064
        },
        "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash"
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam"
    }
}

# --- SIDOMENY: KALKYLATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()

# FÄRGLAGD SURDEGSGUIDE
with st.sidebar.expander("📖 SOURDOUGH CARE GUIDE"):
    st.write("**Daily Care:** Feed 1:1:1 (Starter:Water:Flour).")
    st.write("**Storage:** In fridge, feed once a week.")
    st.write("**Pro-tip:** Add a bit of Rye flour for more activity.")

st.sidebar.divider()

# CUSTOM INGREDIENT
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Ingredient Name", value="Extra Ingredient")
custom_ing_amount = st.sidebar.number_input("Amount (g per unit)", min_value=0, value=0)
custom_ing_price = st.sidebar.number_input("Ingredient Price (LKR/kg)", value=500.0)

st.sidebar.divider()

# ECONOMICS
st.sidebar.header("Economics (LKR)")
flour_price_kg = st.sidebar.number_input("Base Flour Price (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- BERÄKNINGAR ---
total_dough_kg = (units * target_weight) / 1000
total_custom_kg = (units * custom_ing_amount) / 1000

# Kostnadskalkyl
cost_dough = total_dough_kg * flour_price_kg
cost_custom = total_custom_kg * custom_ing_price
# Adderar 25% overhead (el, smör i vissa recept, etc)
total_production_cost = (cost_dough + cost_custom) * 1.25

total_revenue = units * selling_price
total_profit = total_revenue - total_production_cost

# --- LAYOUT ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Production Sheet", "Financials"])
    
    with tab1:
        st.subheader("Ingredients Weight")
        st.write(f"Batch: {units} units x {target_weight}g")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_dough_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            st.write(f"{ing}: **{val:.2f} {unit}**")
            
        if custom_ing_amount > 0:
            c_val = total_custom_kg if total_custom_kg >= 1 else total_custom_kg * 1000
            st.write(f"{custom_ing_name}: **{c_val:.2f} {'kg' if total_custom_kg >= 1 else 'g'}**")

    with tab2:
        st.subheader("Cost Breakdown")
        st.write(f"Base Dough Cost: {cost_dough:,.2f} LKR")
        st.write(f"{custom_ing_name} Cost: {cost_custom:,.2f} LKR")
        st.markdown("---")
        st.write(f"**Total Production Cost:** {total_production_cost:,.2f} LKR")

with col_right:
    st.subheader("Results")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.info(f"Oven: {recipe['bake_temp']} | {recipe['bake_time']}")
