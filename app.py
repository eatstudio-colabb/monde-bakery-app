import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# --- CUSTOM CSS FOR STYLING ---
st.markdown("""
    <style>
    /* Smalare rubrik */
    h1 {
        font-weight: 300 !important;
        letter-spacing: -0.5px;
    }
    
    /* Röd knapp för Sourdough Guide i sidomenyn */
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 2px solid #FF4B4B;
        border-radius: 10px;
        background-color: #FF4B4B;
    }
    
    /* Vit text på knappen */
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: white !important;
        font-weight: 600 !important;
        text-transform: uppercase;
    }
    
    /* Vitt innehåll i guiden */
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
            "Dough: Cold Butter": 0.0805, "Dough: Sugar": 0.0548, "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045, "Filling: Butter": 0.0967, "Filling: Sugar": 0.0290, "Filling: Cinnamon": 0.0064
        },
        "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash",
        "instructions": "1. Autolyse: Mix milk, cardamom, sugar and flour. Rest 30 min. 2. Mix: Add sourdough starter, knead 10 min. 3. Salt: Add salt, knead 3 min. 4. Filling: Mix butter, sugar, cinnamon. 5. Shape: Roll, spread filling, fold in three, cut strips and twist. 6. Proof: Cold proof 12h. 7. Bake: Brush with egg wash and pearl sugar.",
        "pro_tips": "Use cold milk to control friction heat. Do not over-tighten knots. Internal temp: 92-94°C."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam",
        "instructions": "1. Autolyse 40m. 2. Mix starter/salt (10m). 3. 3-4 sets of folds every 30m. 4. Cold proof 12-14h. 5. Dimple with brine before baking.",
        "pro_tips": "The Brine Secret: Whisk water, oil and salt into an emulsion for the dimples."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "15s Steam",
        "instructions": "1. Autolyse 40m. 2. Mix starter/salt. 3. Stretch & Fold. 4. Incorporate seeds. 5. Cold proof 12-14h.",
        "pro_tips": "Bake until 98°C internal. Use steam for the first 15 mins for maximum volume."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam",
        "instructions": "1. Autolyse with yeast 40m. 2. Add starter/salt. 3. Knead 10m. 4. Fold in walnuts during first set of folds.",
        "pro_tips": "Toast walnuts lightly before adding for better flavor."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "default_weight": 300, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam",
        "instructions": "1. Autolyse 40m. 2. Mix everything. 3. 4 sets of folds. 4. Cold proof 12h. 5. Handle gently to keep bubbles.",
        "pro_tips": "High hydration dough. Use plenty of flour on the bench."
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Dry Yeast": 0.0001
        },
        "default_weight": 350, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam",
        "instructions": "1. Prepare poolish 12h before. 2. Mix and knead 9m. 3. Bulk ferment. 4. Shape and cold proof.",
        "pro_tips": "Score at a shallow angle for the best 'ear'."
    }
}

# --- SIDOMENY ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight (g)", value=recipe["default_weight"])

st.sidebar.divider()

# --- SOURDOUGH GUIDE ---
with st.sidebar.expander("📖 SOURDOUGH CARE GUIDE"):
    st.markdown("""
    **1. Daily Care**
    Feed 1-2 times/day at room temp (Ratio 1:1:1). Ready in 4-8h.
    **2. Fridge Storage**
    Feed once a week. Discard all but 1kg, feed with 2kg water + 2kg flour.
    **3. Before Baking**
    Feed 4-6h before use. Ready at peak.
    **4. Troubleshooting**
    Acetone smell = Hungry. Hooch (liquid) = Stir in and feed.
    """)

st.sidebar.divider()

# CUSTOM INGREDIENT & ECONOMICS
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Name", value="Walnuts")
custom_ing_amount = st.sidebar.number_input("Grams per unit", min_value=0, value=0)
custom_ing_price = st.sidebar.number_input("Price (LKR/kg)", value=1500.0)

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
        st.subheader("Instructions")
        st.write(recipe["instructions"])
    
    with tab3:
        st.subheader("Professional Tips")
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Profit & Specs")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Dough Cost: {cost_dough:,.0f} LKR")
    st.write(f"Custom Cost: {cost_custom:,.0f} LKR")
    st.info(f"Oven: {recipe['bake_temp']} | Time: {recipe['bake_time']}")

st.caption("Monde Bakery Digital Handbook | 2026")
