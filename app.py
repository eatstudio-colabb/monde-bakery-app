import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

st.title("🥖 Monde Bakery - Professional Recipe Master")

# --- DATA: RECIPES DATABASE ---
recipes = {
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix (Chia/Flax/Sesam/Quinoa)": 0.1052
        },
        "hydration": 70, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flours and water. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds** every 30 min. Add all seeds during folds.
        4. **Bulk**: 3–4 hours at 24–26°C until "jiggly" (30-50% growth).
        5. **Proof**: 12–14 hours in fridge (Cold Proof).
        6. **Bake**: 245°C for 45 min (or 98°C core). 15s steam at start.
        """,
        "pro_tips": "Bake until internal temp reaches **98°C**. Incorporate seeds early to trap them in the gluten net."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour, water, and dry yeast. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds**. Add walnuts during the 2nd fold.
        4. **Bulk**: 3–4 hours at 24–26°C until "jiggly".
        5. **Proof**: 12–14 hours in fridge.
        6. **Bake**: 245°C for 25-30 min. 15s steam at start.
        """,
        "pro_tips": "Toast walnuts lightly before adding. Cold proof makes 'scars' (scoring) much easier to execute."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour, dry yeast, and water. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds**.
        4. **Bulk**: 3–4 hours at 24–26°C until "jiggly".
        5. **Proof**: 12–14 hours in fridge.
        6. **Bake**: 245°C for 25-30 min. 15s steam at start.
        """,
        "pro_tips": "Use a generous layer of olive oil in the pan to 'fry' the bottom. Use a water/oil brine in the dimples before baking."
    },
    "Sourdough Cinnamon Buns": {
        "ingredients": {
            "Wheat Bread Flour": 0.5050, "Milk (Cold)": 0.2525, "Sourdough Starter": 0.1500,
            "Butter (Room Temp)": 0.0758, "Sugar": 0.0758, "Egg (Dough)": 0.0505,
            "Cardamom": 0.0051, "Salt": 0.0051, "Cinnamon Filling": 0.1500
        },
        "hydration": 50, "default_weight": 80, "bake_temp": "175–200°C", "bake_time": "15–20 min", "steam": "Egg Wash",
        "instructions": """
        1. **Autolyse**: Mix milk, cardamom, and sugar. Add flour gradually. Knead 2–3 min. Rest **30 min**.
        2. **Mix**: Add starter and knead **10 min**. Add salt and knead **3 more min**.
        3. **Filling**: Mix softened butter, sugar, and cinnamon.
        4. **Shape**: Roll to 1cm thickness. Spread filling, fold, and cut 2cm strips. Twist around 3 fingers into a knot.
        5. **Proof**: 12 hours in fridge (overnight).
        6. **Bake**: Brush with egg wash + pearl sugar. Bake at 175–200°C.
        """,
        "pro_tips": "Check the underside of the bun for a golden caramel color. The 3-finger knot ensures consistent sizing."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "hydration": 80, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m with yeast. Knead 10m. 4 sets of folds. Cold proof 12-14h. Bake with high steam.",
        "pro_tips": "Handle gently like a pillow after proofing to preserve large air bubbles."
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 350, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Add poolish/salt. Knead 5m slow + 4m fast. 4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "Score at a very shallow angle. The slow/fast kneading builds the specific elasticity for long shapes."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Wheat Bread Flour": 0.4965, "Water": 0.3308, "Sourdough Starter": 0.1595, "Salt": 0.0132, "Dry Yeast": 0.0001
        },
        "hydration": 72, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m with yeast. Knead 10m. 4 sets of folds. Cold proof 12-14h. Bake at 245°C.",
        "pro_tips": "Focus on the 'heat burst' at the start for a professional open crumb."
    }
}

# --- SIDEBAR: CALCULATOR & SETTINGS ---
st.sidebar.header("📊 Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units (Loaves/Buns)", min_value=1, value=10)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.header("💰 Economics (LKR)")
raw_cost_per_kg = st.sidebar.number_input("Ingredient Cost (per kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
total_cost = total_batch_kg * raw_cost_per_kg * 1.25 # 25% overhead included
total_revenue = units * selling_price
total_profit = total_revenue - total_cost
margin_pct = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0

# --- MAIN DISPLAY ---
st.header(f"🍞 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["📝 Production Sheet", "🥣 Core Process", "💡 Pro Tips"])
    
    with tab1:
        st.subheader("Ingredients Weight")
        st.write(f"Batch for **{units} units** ({target_weight}g each)")
        
        # Display table headers
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingredient**")
        h2.write("**Weight**")
        h3.write("**Ratio**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 2])
            r1.write(ing)
            r2.write(f"**{display_val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        st.divider()
        st.metric("Total Dough Mass", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.subheader("Step-by-Step Guide")
        st.write(recipe["instructions"])
        
    with tab3:
        st.subheader("Baker's Secrets")
        st.info(recipe["pro_tips"])

with col_right:
    st.subheader("Technical Specs")
    st.info(f"**Oven Temp:** {recipe['bake_temp']}")
    st.info(f"**Time:** {recipe['bake_time']}")
    st.info(f"**Steam/Finish:** {recipe['steam']}")
    
    st.divider()
    st.subheader("Financial Summary")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR", delta=f"{margin_pct:.1f}% Margin")
    st.write(f"**Total Revenue:** {total_revenue:,.0f} LKR")
    st.write(f"**Production Cost:** {total_cost:,.0f} LKR")
    
    st.divider()
    st.success("Happy baking—you’re in for a rewarding bake!")

st.caption("Monde Bakery Digital Handbook | Precision Baking System")
