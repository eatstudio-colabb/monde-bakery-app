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

# --- RECEPTDATABAS ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            "Dough: Wheat Flour": 0.3350, "Dough: Milk": 0.2577, "Dough: Sourdough": 0.1289,
            "Dough: Cold Butter (last)": 0.0805, "Dough: Sugar": 0.0548, "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045, "Filling: Butter": 0.0967, "Filling: Sugar": 0.0290, "Filling: Cinnamon": 0.0064
        },
        "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash & Pearl Sugar",
        "instructions": """
        1. **Autolyse (The Soak):** Mix the cold milk, freshly ground cardamom, sugar, and flour in the mixer. Mix on low speed just until combined (2-3 mins). Let it rest for 30-40 minutes. This hydrates the flour and makes the dough easier to work with.
        
        2. **The Starter:** Add your active sourdough starter to the mix. Knead on medium speed for about 8-10 minutes. The dough should start to look smooth and begin to pull away from the sides of the bowl.
        
        3. **Salt & Cold Butter:** Add the salt. Then, with the mixer running, add the **cold butter** cut into small cubes, one by one. Knead for another 5-7 minutes. It is crucial that the butter is cold to create "lamination" layers and a strong gluten structure. The dough should be glossy, elastic, and pass the 'windowpane test'.
        
        4. **First Rise (Bulk):** Let the dough rest in a container at room temperature for about 3-4 hours. Perform one 'stretch and fold' after 60 minutes.
        
        5. **The Filling:** While the dough rests, cream together the room-temperature butter, sugar, and cinnamon into a smooth paste.
        
        6. **Shaping:** Roll out the dough into a large rectangle. Spread the filling evenly all the way to the edges. Fold the dough (either a book-fold or a simple fold). Cut into strips, twist them, and tie them into beautiful knots.
        
        7. **Cold Proof:** Place the buns on a baking tray, cover them, and put them in the fridge for 12-14 hours. This develops the deep sourdough flavor and perfect texture.
        
        8. **Baking:** Take them out and let them sit at room temp for 30-60 mins. Brush carefully with egg wash (mixed with a splash of milk and salt). Sprinkle with pearl sugar. Bake until golden brown (internal temp 92-94°C).
        """,
        "pro_tips": "Never melt the butter for the dough! Using cold cubes at the end of kneading is the secret to the perfect Swedish bun texture."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Brine & Rosemary",
        "instructions": """
        1. **Autolyse:** Mix flour and water (40-60 min).
        2. **Mix:** Add starter and yeast. Knead 8-10 min.
        3. **Salt & Oil:** Add salt and oil, knead until smooth.
        4. **Folds:** 3-4 sets of folds every 30 min.
        5. **Cold Proof:** 12-14h in fridge in an oiled tray.
        6. **Dimpling:** Pour brine (water/oil/salt) over and press deep holes. Bake at 245°C.
        """,
        "pro_tips": "Don't be afraid of the water! A wet dough (high hydration) makes the best bubbles."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "15s Steam",
        "instructions": "1. Autolyse. 2. Mix starter/salt. 3. Stretch & Fold. 4. Incorporate seeds. 5. Cold proof 12h.",
        "pro_tips": "Bake until 98°C internal for a fully set crumb."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam",
        "instructions": "1. Autolyse 40m. 2. Mix starter/salt. 3. Knead 10m. 4. Fold in walnuts.",
        "pro_tips": "Toast the walnuts first!"
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
    **2. Fridge Storage:** Feed weekly (1kg starter + 2kg water + 2kg flour).
    **3. Before Baking:** Feed 4-6h before use. 
    **4. Troubleshooting:** Acetone smell = Hungry.
    """)

st.sidebar.divider()

# CUSTOM INGREDIENT & ECONOMICS
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Name", value="Topping")
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
        st.subheader("Professional Step-by-Step")
        st.write(recipe["instructions"])
    
    with tab3:
        st.subheader("Baker's Secrets")
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Economics")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Dough Cost: {cost_dough:,.0f} LKR")
    st.write(f"Extra Cost: {cost_custom:,.0f} LKR")
    st.divider()
    st.info(f"Oven: {recipe['bake_temp']} | Time: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
