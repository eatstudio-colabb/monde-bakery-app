import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# CSS för surdegsguiden i sidomenyn
st.markdown("""
    <style>
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 2px solid #FF4B4B;
        border-radius: 8px;
        background-color: #FFF5F5;
    }
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: #FF4B4B !important;
        font-weight: bold !important;
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
        "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash",
        "instructions": "1. Autolyse (30m). 2. Mix starter (10m). 3. Add salt. 4. Shape with filling. 5. Cold proof 12h.",
        "pro_tips": "Use cold milk. Do not over-tighten knots. Bake until 92-94°C internal."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam",
        "instructions": "1. Autolyse. 2. Mix starter/salt. 3. Stretch & Fold. 4. Cold proof.",
        "pro_tips": "Use a heavy brine before baking. Preserve the bubbles!"
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "15s Steam",
        "instructions": "Autolyse 40m. Mix starter/salt. Stretch & Fold. Cold proof 12-14h.",
        "pro_tips": "Internal temp 98°C. Steam is crucial for volume."
    }
}

# --- SIDOMENY: KALKYLATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()

# SOURDOUGH GUIDE (EXPANDER)
with st.sidebar.expander("📖 Sourdough Care Guide"):
    st.info("Professional maintenance for your starter.")
    st.write("**Daily:** Feed 1:1:1. **Weekly:** Keep 1kg, feed 2kg water/2kg flour. **Troubleshoot:** Acetone smell = hungry.")

st.sidebar.divider()

# CUSTOM INGREDIENT SECTION
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Ingredient Name", value="Extra Ingredient")
custom_ing_amount = st.sidebar.number_input("Amount (g per unit)", min_value=0, value=0)
custom_ing_price = st.sidebar.number_input("Extra Ingredient Price (LKR/kg)", value=500.0)

st.sidebar.divider()

# ECONOMICS SECTION
st.sidebar.header("Economics (LKR)")
flour_price_kg = st.sidebar.number_input("Flour Price (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- BERÄKNINGAR ---
total_dough_kg = (units * target_weight) / 1000
total_custom_kg = (units * custom_ing_amount) / 1000

# Ekonomisk kalkyl
cost_dough = total_dough_kg * flour_price_kg
cost_custom = total_custom_kg * custom_ing_price
total_production_cost = (cost_dough + cost_custom) * 1.25 # 25% overhead (el, smör, etc)

total_revenue = units * selling_price
total_profit = total_revenue - total_production_cost

# --- HUVUDLAYOUT ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Process", "Pro Tips"])
    
    with tab1:
        st.subheader("Ingredients Weight")
        st.write(f"Production: {units} units at {target_weight}g")
        st.markdown("---")
        
        c1, c2, c3 = st.columns([3, 2, 1])
        c1.write("**Ingredient Name**")
        c2.write("**Required Weight**")
        c3.write("**Ratio**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_dough_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(ing)
            r2.write(f"**{display_val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        if custom_ing_amount > 0:
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(custom_ing_name)
            c_unit = "kg" if total_custom_kg >= 1 else "g"
            c_val = total_custom_kg if c_unit == "kg" else total_custom_kg * 1000
            r2.write(f"**{c_val:.2f} {c_unit}**")
            r3.write("Extra")

        st.markdown("---")
        st.metric("Total Batch Weight", f"{(total_dough_kg + total_custom_kg):.2f} kg")

    with tab2:
        st.write(recipe["instructions"])
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"Oven: {recipe['bake_temp']} | Time: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")
    
    st.divider()
    st.subheader("Financial Summary")
    
    # Detaljerad kostnadsvisning
    st.write(f"Base Dough Cost: {cost_dough:,.0f} LKR")
    if custom_ing_amount > 0:
        st.write(f"{custom_ing_name} Cost: {cost_custom:,.0f} LKR")
    
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Total Revenue: {total_revenue:,.0f} LKR")
    st.write(f"Total Prod. Cost (incl. overhead): {total_production_cost:,.0f} LKR")

st.caption("Monde Bakery Digital Handbook | 2026")
