import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    /* Tjockare rubrik med röd färg */
    h1 { 
        font-weight: 800 !important; 
        color: #FF4B4B !important;
        letter-spacing: -0.5px; 
    }
    
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

# --- KOMPLETT RECEPTDATABAS ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            "Dough: Wheat Flour": 0.3350, "Dough: Milk": 0.2577, "Dough: Sourdough": 0.1289,
            "Dough: Cold Butter (last)": 0.0805, "Dough: Sugar": 0.0548, "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045, "Filling: Butter": 0.0967, "Filling: Sugar": 0.0290, "Filling: Cinnamon": 0.0064
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash & Pearl Sugar",
        "instructions": """
        1. **Autolyse:** Mix cold milk, cardamom, sugar, and flour. Rest 30–40 min.
        2. **Mix:** Add sourdough starter. Knead 8–10 min on medium speed.
        3. **Salt & Butter:** Add salt. Gradually add **cold butter cubes**. Knead 5–7 min until glossy and elastic.
        4. **Bulk:** Rest 3–4h. One stretch & fold after 60 min.
        5. **Shape & Proof:** Spread filling, twist into knots. Cold proof 12–14h in fridge.
        6. **Bake:** Brush with egg wash, add pearl sugar. Bake to internal temp 92–94°C.
        """,
        "pro_tips": "Cold butter added at the end is the secret to a fluffy bakery texture."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Brine & Rosemary",
        "instructions": """
        1. **Autolyse:** Mix flour and water. Rest 40–60 min.
        2. **Mix:** Add starter and yeast. Knead 8–10 min.
        3. **Salt & Oil:** Add salt and olive oil. Knead until smooth.
        4. **Bulk:** 3–4 sets of 'Stretch and Folds' every 30 min.
        5. **Prep:** Place in oiled tray. Cold proof 12–14h in fridge.
        6. **Brine & Dimple:** Pour brine (water/oil/salt) over dough. Press deep dimples with fingers.
        7. **Bake:** Add rosemary and sea salt. Bake at 245°C.
        """,
        "pro_tips": "The brine keeps the dimples soft while the crust gets crunchy."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "30-35 min", "finish": "15s Steam",
        "instructions": "1. Toast walnuts. 2. Autolyse. 3. Mix starter. 4. Fold in walnuts. 5. Cold proof 12h.",
        "pro_tips": "Toasting walnuts enhances flavor and prevents purple dough."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "hydration": 72, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "15s Steam",
        "instructions": "1. Soak seeds. 2. Autolyse. 3. Mix starter/salt. 4. Fold in seeds. 5. Cold proof 12h.",
        "pro_tips": "Bake until internal temp reaches 98°C for a perfect crumb."
    },
    "Artisan Whole Wheat": {
        "ingredients": {
            "Whole Wheat Flour": 0.3500, "Wheat Bread Flour": 0.1000, "Water": 0.3500, 
            "Sourdough Starter": 0.1800, "Salt": 0.0120, "Honey/Malt": 0.0080
        },
        "hydration": 80, "default_weight": 850, "bake_temp": "240°C", "bake_time": "40 min", "finish": "Flour Dust",
        "instructions": "1. Long autolyse (2h). 2. Mix starter/salt. 3. 4 sets of folds. 4. Cold proof 12-15h.",
        "pro_tips": "A long autolyse is essential for whole wheat to soften the bran."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Wheat Bread Flour": 0.4500, "Water": 0.3150, "Sourdough Starter": 0.1350, 
            "Salt": 0.0090, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 850, "bake_temp": "250°C", "bake_time": "35-40 min", "finish": "Steam",
        "instructions": "1. Autolyse 60m. 2. Mix starter/salt. 3. Stretch & Fold 3 sets. 4. Cold proof 12h.",
        "pro_tips": "Deep scoring at a 45-degree angle for a perfect 'ear'."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "hydration": 82, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25 min", "finish": "Flour Dust",
        "instructions": "1. High hydration mix. 2. Intensive folding. 3. Handle with care during shaping.",
        "pro_tips": "Use plenty of flour on the bench to prevent sticking."
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Dry Yeast": 0.0001
        },
        "hydration": 68, "default_weight": 350, "bake_temp": "245°C", "bake_time": "22 min", "finish": "Heavy Steam",
        "instructions": "1. Poolish 12h before. 2. Mix/Knead 9m. 3. Shape and proof in linen.",
        "pro_tips": "Steam is essential for the thin, crispy crust."
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
    **1. Daily Care:** Feed 1:1:1. Ready in 4-8h.
    **2. Storage:** Fridge storage, feed weekly (1kg starter + 2kg water + 2kg flour).
    **3. Before Baking:** Feed 4-6h before use. 
    **4. Troubleshooting:** Acetone smell = Hungry.
    """)

st.sidebar.divider()

# ECONOMICS
st.sidebar.header("Economics (LKR)")
flour_price_kg = st.sidebar.number_input("Base Flour Price (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- CALCULATIONS ---
total_dough_kg = (units * target_weight) / 1000
cost_dough = total_dough_kg * flour_price_kg
total_prod_cost = cost_dough * 1.25
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
        
        st.markdown("---")
        st.metric("Total Batch Weight", f"{total_dough_kg:.2f} kg")

    with tab2:
        st.subheader("Professional Guide")
        st.write(recipe["instructions"])
    with tab3:
        st.subheader("Baker's Secrets")
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Economics")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Production Cost (Inc. 25% overhead): {total_prod_cost:,.0f} LKR")
    st.divider()
    st.info(f"Oven: {recipe['bake_temp']} | Time: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
