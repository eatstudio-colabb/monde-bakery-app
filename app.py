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
        "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash",
        "instructions": """
        1. **Autolyse:** Mix milk, cardamom, sugar and flour. Rest 30 min.
        2. **Mix:** Add sourdough starter, knead 10 min.
        3. **Salt & Butter:** Add salt and **cold butter cubes**. Knead final 3-5 min until shiny.
        4. **Shape & Proof:** Fill, twist, and cold proof 12h.
        """,
        "pro_tips": "Adding cold butter at the very end ensures a light, airy crumb without breaking the gluten."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Brine & Rosemary",
        "instructions": """
        1. **Autolyse:** Mix flour and water. Let rest for 40-60 minutes to develop natural gluten.
        2. **Mix:** Add the active sourdough starter and the tiny amount of dry yeast. Knead for 8-10 minutes.
        3. **Salt & Oil:** Add salt and a splash of olive oil. Knead until the dough is smooth and releases from the sides (it will be sticky!).
        4. **Bulk Fermentation:** Let the dough rest in a bowl. Perform 3-4 sets of 'Stretch and Folds' every 30 minutes to build strength.
        5. **Pan Prep:** Pour 2-3 tbsp of olive oil into a baking tray. Place the dough in the tray, coat it in oil, and let it rest/stretch to the corners.
        6. **Cold Proof:** Cover and place in the fridge for 12-14 hours.
        7. **The Dimpling:** Take it out, let it reach room temp (1-2h). Whisk a 'brine' (2 parts water, 1 part oil, pinch of salt) until milky. Pour over dough. Use your fingers to press deep dimples all the way to the bottom.
        8. **Bake:** Top with rosemary and sea salt. Bake at 245°C until golden and crispy.
        """,
        "pro_tips": "The brine is the secret! It creates pockets of steam that keep the dimples soft while the top gets crunchy."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "15s Steam",
        "instructions": "1. Autolyse. 2. Mix starter/salt. 3. Stretch & Fold. 4. Incorporate seeds. 5. Cold proof 12h.",
        "pro_tips": "Internal temp 98°C. Steam is crucial for the first 15 mins."
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
    **4. Troubleshooting:** Acetone smell = Hungry. Hooch = Stir in and feed.
    """)

st.sidebar.divider()

# CUSTOM INGREDIENT & ECONOMICS
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Name", value="Topping/Extra")
custom_ing_amount = st.sidebar.number_input("Grams per unit", min_value=0, value=0)
custom_ing_price = st.sidebar.number_input("Price (LKR/kg)", value=1000.0)

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
        st.subheader("Step-by-Step Instructions")
        st.write(recipe["instructions"])
    
    with tab3:
        st.subheader("Professional Secrets")
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
