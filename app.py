import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    h1 { font-weight: 300 !important; letter-spacing: -0.5px; }
    
    /* Röd Sourdough Guide-knapp i sidomenyn */
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
        1. **Autolyse (The Soak):** Mix the cold milk, freshly ground cardamom, sugar, and flour in the mixer. Mix on low speed just until combined (2–3 minutes). Let the dough rest for 30–40 minutes.
        2. **The Mix:** Add your active sourdough starter. Knead on medium speed for about 8–10 minutes until the dough begins to pull away from the bowl.
        3. **Salt & Cold Butter:** Add the salt. Gradually add the **cold butter** (cut into small cubes). Knead for another 5–7 minutes until glossy and elastic (passes the windowpane test).
        4. **Bulk Fermentation:** Let the dough rest for 3–4 hours at room temperature. Perform one 'stretch and fold' after 60 minutes.
        5. **Shaping & Cold Proof:** Spread filling, twist into knots, and refrigerate for 12–14 hours.
        6. **Baking:** Brush with egg wash and sprinkle pearl sugar. Bake until internal temp 92–94°C.
        """,
        "pro_tips": "Cold butter added at the end is the secret to a fluffy, high-end bakery texture."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Brine & Rosemary",
        "instructions": """
        1. **Autolyse:** Mix the bread flour and water until no dry spots remain. Let it rest for 40–60 minutes to allow natural gluten development.
        
        2. **The Mix:** Add the active sourdough starter and the tiny amount of dry yeast. Knead for 8–10 minutes until the dough becomes cohesive.
        
        3. **Salt & Oil:** Add the salt and a splash of olive oil. Knead until the dough is smooth and starts to release from the sides of the bowl. Note: The dough will be very sticky and high-hydration.
        
        4. **Bulk Fermentation (Folds):** Let the dough rest in a bowl. Perform 3–4 sets of 'Stretch and Folds' every 30 minutes. This builds the strength needed to hold the large air bubbles.
        
        5. **Pan Preparation:** Pour 2–3 tablespoons of olive oil into your baking tray. Place the dough in the tray, flip it to coat in oil, and gently stretch it toward the corners.
        
        6. **Cold Proof:** Cover and refrigerate for 12–14 hours. This slow cold ferment is essential for the characteristic sourdough tang and airy structure.
        
        7. **Dimpling & Brine:** Take the dough out 1–2 hours before baking. Whisk together a 'brine' (2 parts water, 1 part oil, a pinch of salt) until emulsified. Pour the brine over the dough. Use your fingers to press deep dimples all the way to the bottom of the tray.
        
        8. **Baking:** Top with fresh rosemary and sea salt. Bake at 245°C until golden and crispy on the outside.
        """,
        "pro_tips": "The brine creates steam pockets in the dimples, keeping them soft while the rest of the surface gets crunchy."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Wheat Bread Flour": 0.4500, "Water": 0.3150, "Sourdough Starter": 0.1350, 
            "Salt": 0.0090, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 850, "bake_temp": "250°C", "bake_time": "35-40 min", "finish": "Steam",
        "instructions": "1. Autolyse 60m. 2. Mix starter/salt. 3. Stretch & Fold 3 sets. 4. Shape and cold proof 12h.",
        "pro_tips": "Deep scoring at a 45-degree angle for a perfect 'ear'."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "hydration": 82, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25 min", "finish": "Flour Dust",
        "instructions": "1. High hydration mix. 2. Intensive folding. 3. Cut into slippers, handle with care.",
        "pro_tips": "Use plenty of flour on the bench to handle the high hydration."
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

# CUSTOM INGREDIENT & ECONOMICS
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Name", value="Extra Ingredient")
custom_ing_amount = st.sidebar.number_input("Grams per unit", min_value=0, value=0)
custom_ing_price = st.sidebar.number_input("Price (LKR/kg)", value=1500.0)

st.sidebar.divider()
st.sidebar.header("Economics (LKR)")
flour_price_kg = st.sidebar.number_input("Base Flour Price (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- BERÄKNINGAR ---
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
        st.subheader("Professional Guide (English)")
        st.write(recipe["instructions"])
    with tab3:
        st.subheader("Baker's Secrets")
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Economics")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Dough Cost: {cost_dough:,.0f} LKR")
    if custom_ing_amount > 0:
        st.write(f"Extra Cost: {cost_custom:,.0f} LKR")
    st.divider()
    st.info(f"Oven: {recipe['bake_temp']} | Time: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
