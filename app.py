import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    h1 { font-weight: 300 !important; letter-spacing: -0.5px; }
    
    /* Röd Sourdough Guide-knapp */
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 2px solid #FF4B4B;
        border-radius: 10px;
        background-color: #FF4B4B;
    }
    
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: white !important;
        font-weight: 600 !important;
        text-transform: uppercase;
    }
    
    div[data-testid="stSidebar"] [data-testid="stExpanderDetails"] {
        background-color: white;
        color: black;
        border-radius: 0 0 8px 8px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Monde Bakery - Professional Recipe Master")

# --- RECEPTDATABAS MED HYDRERING OCH PROCENT ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            "Dough: Wheat Flour": 0.3350, "Dough: Milk": 0.2577, "Dough: Sourdough": 0.1289,
            "Dough: Cold Butter (last)": 0.0805, "Dough: Sugar": 0.0548, "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045, "Filling: Butter": 0.0967, "Filling: Sugar": 0.0290, "Filling: Cinnamon": 0.0064
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash",
        "instructions": """
        1. **Autolyse:** Blanda mjölk, kardemumma, socker och mjöl. Vila 30-40 min.
        2. **Mix:** Tillsätt surdeg, knåda 8-10 min i maskin.
        3. **Salt & Smör:** Tillsätt salt och sedan det **kalla smöret** i tärningar. Knåda ytterligare 5-7 min tills degen är glansig och klarar 'fönstertestet'.
        4. **Vila:** Låt degen vila 3-4 timmar i rumstemp.
        5. **Forma:** Kavla ut, bred på fyllning, vik och gör knutar.
        6. **Kalljäst:** Jäs i kylskåp 12-14 timmar.
        7. **Bakning:** Pensla med ägg, på med pärlsocker och baka till innertemp 92-94°C.
        """,
        "pro_tips": "Kallt smör i slutet av knådningen är hemligheten bakom en luftig bulle med perfekt struktur."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Brine & Rosemary",
        "instructions": """
        1. **Autolyse:** Blanda mjöl och vatten (40-60 min).
        2. **Mix:** Tillsätt surdeg och jäst. Knåda 8-10 min.
        3. **Salt & Olja:** Tillsätt salt och olja, knåda till smidig deg.
        4. **Folds:** Gör 3-4 set 'Stretch & Fold' var 30:e minut.
        5. **Kalljäst:** 12-14h i kylen i oljad plåt.
        6. **Dimpling:** Häll över saltlake (vatten/olja/salt) och tryck djupa hål med fingrarna. Baka direkt på 245°C.
        """,
        "pro_tips": "Saltlaken (brine) skapar ånga i hålen vilket håller brödet saftigt inuti och krispigt utanpå."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "hydration": 72, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "Steam",
        "instructions": "Autolyse 40m. Mix starter/salt. Stretch & Fold. Kalljäst 12h.",
        "pro_tips": "Innertemp 98°C för perfekt resultat."
    }
}

# --- SIDOMENY ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight (g)", value=recipe["default_weight"])

st.sidebar.divider()

# SOURDOUGH GUIDE
with st.sidebar.expander("📖 SOURDOUGH CARE GUIDE"):
    st.markdown("""
    **Daily Care:** Feed 1:1:1. Ready in 4-8h.
    **Storage:** Fridge, feed weekly (1kg starter + 2kg water + 2kg flour).
    **Troubleshoot:** Acetone smell = Hungry.
    """)

st.sidebar.divider()

# CUSTOM INGREDIENT & ECONOMICS
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Name", value="Walnuts/Extra")
custom_ing_amount = st.sidebar.number_input("Grams per unit", min_value=0, value=0)
custom_ing_price = st.sidebar.number_input("Price (LKR/kg)", value=1200.0)

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
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Core Process", "Pro Tips"])
    
    with tab1:
        st.subheader("Ingredients Weight & Ratios")
        st.write(f"Batch: {units} units x {target_weight}g | **Hydration: {recipe['hydration']}%**")
        st.markdown("---")
        
        # Skapa tabell-liknande layout för procenten
        c1, c2, c3 = st.columns([3, 2, 1])
        c1.write("**Ingredient**")
        c2.write("**Weight**")
        c3.write("**% of Total**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_dough_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(ing)
            r2.write(f"**{val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        if custom_ing_amount > 0:
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(custom_ing_name)
            c_val = total_custom_kg if total_custom_kg >= 1 else total_custom_kg * 1000
            r2.write(f"**{c_val:.2f} {'kg' if total_custom_kg >= 1 else 'g'}**")
            r3.write("Extra")
        
        st.markdown("---")
        st.metric("Total Batch Weight", f"{(total_dough_kg + total_custom_kg):.2f} kg")

    with tab2:
        st.write(recipe["instructions"])
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Financial Summary")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Base Cost: {cost_dough:,.0f} LKR")
    if custom_ing_amount > 0:
        st.write(f"Extra Cost: {cost_custom:,.0f} LKR")
    st.divider()
    st.info(f"Oven: {recipe['bake_temp']} | Time: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
