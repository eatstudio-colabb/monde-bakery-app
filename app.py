import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES WITH HYDRATION & DETAILED RATIOS ---
# Note: Hydration is calculated as (Total Water / Total Flour)
recipes = {
    "Focaccia with Sourdough": {
        "ingredients": {"Wheat Flour": 0.4655, "Water": 0.3335, "Sourdough": 0.1817, "Salt": 0.0111, "Olive Oil": 0.0082},
        "hydration": 72,
        "default_weight": 5002,
        "instructions": "1. Mix flour, water, and starter. Autolyse 30 min. 2. Add salt/oil. 4 sets of folds. 3. Proof in tray with oil. 4. Dimple and bake at 230°C.",
        "tips": "High hydration requires gentle folding (coil folds) to keep the air."
    },
    "Artisan Levain French Sourdough": {
        "ingredients": {"Wheat Flour": 0.4965, "Water": 0.3308, "Sourdough": 0.1613, "Salt": 0.0114},
        "hydration": 67,
        "default_weight": 800,
        "instructions": "1. Autolyse 1h. 2. Add starter/salt. Bulk ferment 5h (26°C). 3. Shape and cold proof 12h+. 4. Bake at 240°C with steam.",
        "tips": "Use a Dutch oven for the first 20 mins to get the perfect crust."
    },
    "Baguette with Poolish": {
        "ingredients": {"Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2417, "Salt": 0.0089, "Dry Yeast": 0.0001},
        "hydration": 65,
        "default_weight": 350,
        "instructions": "1. Poolish 12h before. 2. Mix dough, rest 45 min. 3. Shape long and proof in couche. 4. Score 5 times and bake with heavy steam.",
        "tips": "Don't over-knead; let the poolish do the flavor work."
    },
    "Multi Grain Sourdough": {
        "ingredients": {"Wheat Flour": 0.2946, "Whole Wheat": 0.0810, "Water": 0.4051, "Sourdough": 0.1539, "Seeds Mix": 0.0654},
        "hydration": 78,
        "default_weight": 1000,
        "instructions": "1. Soak seeds 2h. 2. Mix all. Bulk ferment with 3 folds. 3. Shape and coat in seeds. 4. Cold proof.",
        "tips": "Whole grains absorb more water, hence the higher hydration."
    },
    "Sourdough Ciabatta": {
        "ingredients": {"Wheat Flour": 0.5389, "Water": 0.4001, "Sourdough": 0.0500, "Salt": 0.0110},
        "hydration": 82,
        "default_weight": 300,
        "instructions": "1. Mix to full gluten development. 2. Fold every 30 min. 3. Flip onto floured surface, cut, don't de-gas. 4. Bake hot.",
        "tips": "Very sticky dough! Use wet hands during folding and lots of flour for shaping."
    },
    "Swedish Cinnamon Buns": {
        "ingredients": {"Wheat Flour": 0.3350, "Milk": 0.2000, "Butter": 0.0966, "Sugar": 0.0644, "Yeast": 0.0161, "Filling": 0.2879},
        "hydration": 60, # Calculated on milk
        "default_weight": 130,
        "instructions": "1. Creamy dough mix. 2. Rise 1h. 3. Roll out, add filling, knot. 4. Proof 45 min, egg wash, bake at 225°C.",
        "tips": "Cardamom in the dough makes the flavor authentic."
    },
    "Sourdough with Walnuts": {
        "ingredients": {"Wheat Flour": 0.3971, "Rye": 0.0393, "Water": 0.3090, "Sourdough": 0.1765, "Walnuts": 0.0662, "Salt": 0.0119},
        "hydration": 70,
        "default_weight": 900,
        "instructions": "1. Toast walnuts. 2. Mix dough, add nuts during first fold. 3. Standard sourdough bulk/shape. 4. Bake.",
        "tips": "The walnuts will tint the dough slightly purple; this is normal."
    },
     "Whole Wheat Sourdough": {
        "ingredients": {"Whole Wheat": 0.3654, "Wheat Flour": 0.1500, "Water": 0.3500, "Sourdough": 0.1235, "Salt": 0.0111},
        "hydration": 75,
        "default_weight": 850,
        "instructions": "1. Long autolyse (2h). 2. Gentle mix. 3. Bulk ferment at 25°C. 4. Deep scoring.",
        "tips": "Whole wheat ferments faster than white flour. Watch the dough closely!"
    }
}

# --- SIDEBAR ---
st.sidebar.header("Recipe Selector")
selected_name = st.sidebar.selectbox("Bread Type", list(recipes.keys()))
recipe = recipes[selected_name]

st.sidebar.divider()
st.sidebar.header("Batch Size")
units = st.sidebar.number_input("Number of units", min_value=1, value=1)
target_weight = st.sidebar.number_input("Weight per unit (g)", value=recipe["default_weight"])

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000

# --- MAIN DISPLAY ---
col_main, col_stats = st.columns([2, 1])

with col_main:
    st.header(selected_name)
    tab1, tab2 = st.tabs(["Ingredient List", "Baking Instructions"])

    with tab1:
        # Create a table for clarity
        st.write("### Production Sheet")
        header_col = st.columns([3, 2, 2])
        header_col[0].write("**Ingredient**")
        header_col[1].write("**Weight**")
        header_col[2].write("**% of Total**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            
            row = st.columns([3, 2, 2])
            row[0].write(ing)
            row[1].write(f"**{display_val:.2f} {unit}**")
            row[2].write(f"{ratio*100:.1f}%")
        
        st.divider()
        st.write(f"Total Batch Weight: **{total_batch_kg:.2f} kg**")

    with tab2:
        st.write("### Step-by-Step")
        st.write(recipe["instructions"])
        st.success(f"**Pro Tip:** {recipe['tips']}")

with col_stats:
    st.subheader("Bakers Stats")
    st.metric("Hydration", f"{recipe['hydration']}%")
    st.info("Hydration is calculated on total flour content.")
    
    # Simple Costing Box
    st.subheader("Quick Costing")
    price_flour = st.number_input("Flour Price (LKR/kg)", value=224.0)
    total_cost = total_batch_kg * price_flour * 0.55 # Baseline factor
    st.write(f"Estimated Cost: **{total_cost:.0f} LKR**")
