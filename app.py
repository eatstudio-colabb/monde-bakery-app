import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

st.title("Monde Bakery - Professional Recipe Master")

# --- DATA: RECIPES DATABASE ---
recipes = {
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": """
        1. Autolyse: Mix flour, dry yeast, and water. Rest 40 min.
        2. Mix: Add starter and salt. Knead 10 min.
        3. Strength: 3–4 sets of Stretch and Folds every 30 min.
        4. Bulk: 3–4 hours at 24–26°C until jiggly.
        5. Proof: 12–14 hours in fridge (Cold Proof).
        6. Bake: 245°C for 25-30 min. 15s steam at start.
        """,
        "pro_tips": """
        ### Deep Dive: The Ultimate Focaccia Guide
        
        * The Pan Prep: Focaccia is essentially shallow-fried. Pour a generous layer of olive oil (at least 2-3 tbsp) into the bottom. This creates the golden, crunchy crust underneath.
        * The Big Stretch: After cold proof, let the dough rest in the pan for 30–60 min to relax. Once spread, oil hands and press fingers deep until you feel the pan.
        * The Brine Secret: Mix 2 tbsp warm water with 1 tbsp olive oil and salt. Whisk until emulsified. Pour into dimples before baking to keep the top soft.
        * Bubble Control: The cold fermentation creates large bubbles. Work around them during dimpling to preserve structure.
        * Post-Bake Care: Move to a wire rack after 5 mins to prevent the bottom from getting soggy.
        """
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix": 0.1052
        },
        "hydration": 70, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt (10m knead). Stretch & Fold (3-4 sets). Add seeds. Cold proof 12-14h. Bake 245°C.",
        "pro_tips": "Bake until internal temp reaches 98°C. Steam is crucial for the first 15 mins."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m with yeast. Add starter/salt (10m knead). Fold in walnuts. Cold proof 12-14h.",
        "pro_tips": "Toast walnuts lightly first. Cold proof makes scoring much easier."
    },
    "Sourdough Cinnamon Buns": {
        "ingredients": {
            "Wheat Bread Flour": 0.5050, "Milk (Cold)": 0.2525, "Sourdough Starter": 0.1500,
            "Butter (Room Temp)": 0.0758, "Sugar": 0.0758, "Egg (Dough)": 0.0505,
            "Cardamom": 0.0051, "Salt": 0.0051, "Cinnamon Filling": 0.1500
        },
        "hydration": 50, "default_weight": 80, "bake_temp": "175–200°C", "bake_time": "15–20 min", "steam": "Egg Wash",
        "instructions": "Autolyse 30m. Add starter (10m knead). Add salt (3m knead). Shape knots. Cold proof 12h.",
        "pro_tips": "Check the underside for caramel color. Use the 3-finger twist for knots."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "hydration": 80, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "80% hydration. Autolyse 40m. 4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "Handle gently. Do not degas during shaping."
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 350, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 5m slow + 4m fast. 4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "Fast kneading builds tension. Score at a shallow angle."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Wheat Bread Flour": 0.4965, "Water": 0.3308, "Sourdough Starter": 0.1595, "Salt": 0.0132, "Dry Yeast": 0.0001
        },
        "hydration": 72, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 10m. 4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "Focus on the initial heat burst and steam for an open crumb."
    }
}

# --- SIDEBAR: CALCULATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=10)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

# New Feature: Optional Custom Ingredient
st.sidebar.divider()
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Ingredient Name", value="Extra Ingredient")
custom_ing_amount = st.sidebar.number_input("Amount (g per unit)", min_value=0, value=0)

st.sidebar.divider()
st.sidebar.header("Economics (LKR)")
raw_cost_per_kg = st.sidebar.number_input("Ingredient Cost (per kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
total_custom_kg = (units * custom_ing_amount) / 1000

total_cost = (total_batch_kg + total_custom_kg) * raw_cost_per_kg * 1.25 
total_revenue = units * selling_price
total_profit = total_revenue - total_cost

# --- MAIN DISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Core Process", "Pro Tips"])
    
    with tab1:
        st.subheader("Ingredients Weight")
        
        # Table Headers
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingredient**")
        h2.write("**Weight**")
        h3.write("**Ratio**")
        
        # Base Ingredients
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 2])
            r1.write(ing)
            r2.write(f"**{display_val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        # Optional Custom Ingredient
        if custom_ing_amount > 0:
            c1, c2, c3 = st.columns([3, 2, 2])
            c1.write(f"{custom_ing_name}")
            c_unit = "kg" if total_custom_kg >= 1 else "g"
            c_display = total_custom_kg if c_unit == "kg" else total_custom_kg * 1000
            c2.write(f"**{c_display:.2f} {c_unit}**")
            c3.write("Custom")
            
        st.divider()
        st.metric("Total Batch Weight", f"{(total_batch_kg + total_custom_kg):.2f} kg")

    with tab2:
        st.subheader("Step-by-Step Guide")
        st.write(recipe["instructions"])
        
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"Oven Temp: {recipe['bake_temp']}")
    st.info(f"Time: {recipe['bake_time']}")
    st.info(f"Steam/Finish: {recipe['steam']}")
    
    st.divider()
    st.subheader("Financial Summary")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Total Revenue: {total_revenue:,.0f} LKR")
    
    st.divider()
    st.success("Happy baking—you are in for a rewarding bake!")

st.caption("Monde Bakery Digital Handbook | 2026")
