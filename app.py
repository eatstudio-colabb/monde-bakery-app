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
        background-color: #FF4B4B; /* Bakgrundsfärg på knappen */
    }
    
    /* Textfärg på knappen */
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: white !important;
        font-weight: 600 !important;
        text-transform: uppercase;
    }
    
    /* Innehållet inuti guiden när den öppnas */
    div[data-testid="stSidebar"] [data-testid="stExpanderDetails"] {
        background-color: white;
        color: black;
        border-radius: 0 0 8px 8px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Monde Bakery - Professional Recipe Master")

# --- DATA: RECIPES ---
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

# --- SIDEBAR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight (g)", value=recipe["default_weight"])

st.sidebar.divider()

# --- FULLSTÄNDIG SURDEGSGUIDE ---
with st.sidebar.expander("📖 SOURDOUGH CARE GUIDE"):
    st.markdown("### Professional Bakery Guide")
    st.markdown("""
    **1. What it is**
    A living culture of wild yeast (for rise) and lactic acid bacteria (for flavor).
    
    **2. Daily Care (If baking often)**
    Feed 1-2 times/day at room temp. 
    *Example: 50g starter + 50g water + 50g flour.*
    Ready when doubled, bubbly, and smells fresh (4-8h).
    
    **3. Refrigerator Storage**
    Feed once a week. 
    *Weekly feeding:* Take out, discard all but 1kg. Feed with 2kg water + 2kg flour. Let sit 1-2h before returning to fridge.
    
    **4. Before Baking**
    Take out of fridge and feed (e.g., 1kg water + 1kg flour). Wait 4-6h until peak. Many bakers feed twice for extra strength.
    
    **5. Flour Choice**
    Wheat, whole wheat, or rye. Rye/Whole wheat adds more nutrients and activity.
    
    **6. Signs of Health**
    Fruity/yogurty smell, active bubbles, doubles in volume.
    
    **7. Troubleshooting**
    * *Acetone smell:* Hungry starter. Feed more often.
    * *Hooch (Liquid on top):* Normal hunger sign. Pour off/stir in and feed.
    * *Weak fermentation:* Feed several times at room temp.
    
    **8. Temperature**
    * 20-22°C: Slower
    * 24-26°C: Ideal for wheat
    * 28°C+: Very fast and acidic
    """)

st.sidebar.divider()

# CUSTOM INGREDIENT & ECONOMICS
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Name", value="Extra Ingredient")
custom_ing_amount = st.sidebar.number_input("Grams per unit", min_value=0, value=0)
custom_ing_price = st.sidebar.number_input("Price (LKR/kg)", value=500.0)

st.sidebar.divider()
st.sidebar.header("Economics (LKR)")
flour_price_kg = st.sidebar.number_input("Base Flour Price (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- CALCULATIONS ---
total_dough_kg = (units * target_weight) / 1000
total_custom_kg = (units * custom_ing_amount) / 1000

cost_dough = total_dough_kg * flour_price_kg
cost_custom = total_custom_kg * custom_ing_price
total_prod_cost = (cost_dough + cost_custom) * 1.25

total_revenue = units * selling_price
total_profit = total_revenue - total_prod_cost

# --- MAIN DISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Production Sheet", "Financials"])
    
    with tab1:
        st.subheader("Ingredients Weight")
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_dough_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            st.write(f"{ing}: **{val:.2f} {unit}**")
            
        if custom_ing_amount > 0:
            c_val = total_custom_kg if total_custom_kg >= 1 else total_custom_kg * 1000
            st.write(f"{custom_ing_name}: **{c_val:.2f} {'kg' if total_custom_kg >= 1 else 'g'}**")
        
        st.markdown("---")
        st.metric("Total Batch Weight", f"{(total_dough_kg + total_custom_kg):.2f} kg")

    with tab2:
        st.subheader("Cost Breakdown")
        st.write(f"Base Dough Cost: {cost_dough:,.2f} LKR")
        st.write(f"{custom_ing_name} Cost: {cost_custom:,.2f} LKR")
        st.write(f"Overhead (25%): {(total_prod_cost - cost_dough - cost_custom):,.2f} LKR")

with col_right:
    st.subheader("Profit & Specs")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.info(f"Oven: {recipe['bake_temp']} | Time: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
