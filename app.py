import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

st.title("Monde Bakery - Professional Recipe Master")

# --- DATA: RECIPES DATABASE ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            # Deg (Baserat på total degvikt 3104g i originalfilen)
            "Dough: Wheat Flour": 0.3350,  # 1040g
            "Dough: Milk": 0.2577,         # 800g
            "Dough: Sourdough": 0.1289,    # 400g
            "Dough: Cold Butter": 0.0805,  # 250g
            "Dough: Sugar": 0.0548,        # 170g
            "Dough: Cardamom": 0.0064,     # 20g
            "Dough: Salt": 0.0045,         # 14g
            # Fyllning
            "Filling: Butter": 0.0967,     # 300g
            "Filling: Sugar": 0.0290,      # 90g
            "Filling: Cinnamon": 0.0064    # 20g
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "steam": "Egg Wash",
        "instructions": """
        1. Autolyse: Mix milk, cardamom, sugar and flour. Knead 2-3 min. Rest 30 min.
        2. Mix: Add sourdough starter and knead 10 min. 
        3. Salt: Add salt and knead 3 more min until strong and elastic.
        4. Filling: In a separate bowl, mix softened butter, sugar, and cinnamon until smooth.
        5. Shape: Roll to 1cm thick. Spread filling, fold in three. Cut 2cm strips and twist into knots.
        6. Proof: Cover and cold proof in fridge for 12 hours (overnight).
        7. Bake: Brush with egg wash + milk. Sprinkle pearl sugar. Bake 175–200°C.
        """,
        "pro_tips": """
        ### Deep Dive: Professional Cinnamon Bun Tips
        * The Cold Milk Secret: Always use cold milk to prevent the dough from overheating during the long knead.
        * Filling Distribution: Ensure your filling butter is soft but not melted for an even spread that stays inside the bun.
        * The Knot Tension: Twist gently; tight knots will "erupt" in the center during baking.
        * Post-Bake: Brush with sugar syrup immediately after the oven to lock in moisture.
        """
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt (10m). 3-4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "The Brine Secret: Mix water, olive oil, and salt into an emulsion. Pour into dimples before baking."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix": 0.1052
        },
        "hydration": 70, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt (10m). Stretch & Fold. Cold proof 12-14h.",
        "pro_tips": "Bake until internal temp reaches 98°C."
    },
    # Övriga recept (Walnuts, Ciabatta, Baguette, Levain) behålls som tidigare...
}

# --- SIDEBAR: CALCULATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

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
total_dough_mass = total_batch_kg + total_custom_kg

# --- MAIN DISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Core Process", "Pro Tips"])
    
    with tab1:
        st.subheader("Full Ingredients Breakdown")
        st.write(f"Production: {units} units at {target_weight}g")
        
        st.markdown("---")
        c1, c2, c3 = st.columns([3, 2, 1])
        c1.write("**Ingredient Name**")
        c2.write("**Required Weight**")
        c3.write("**Ratio**")
        
        # Display each flour and liquid
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 1])
            # Sätt fetstilt på "Dough:" eller "Filling:" för tydlighet
            r1.write(ing)
            r2.write(f"**{display_val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        # Display custom ingredient
        if custom_ing_amount > 0:
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(custom_ing_name)
            c_unit = "kg" if total_custom_kg >= 1 else "g"
            c_val = total_custom_kg if c_unit == "kg" else total_custom_kg * 1000
            r2.write(f"**{c_val:.2f} {c_unit}**")
            r3.write("Extra")

        st.markdown("---")
        st.metric("Total Batch Dough Weight", f"{total_dough_mass:.2f} kg")

    with tab2:
        st.subheader("Professional Process")
        st.write(recipe["instructions"])
        
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"Oven Temp: {recipe['bake_temp']}")
    st.info(f"Time: {recipe['bake_time']}")
    st.info(f"Steam/Finish: {recipe['steam']}")
    
    st.divider()
    total_cost = total_dough_mass * raw_cost_per_kg * 1.25
    total_revenue = units * selling_price
    total_profit = total_revenue - total_cost
    
    st.subheader("Financial Summary")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Total Revenue: {total_revenue:,.0f} LKR")
    st.write(f"Est. Production Cost: {total_cost:,.0f} LKR")
    
    st.divider()
    st.success("Happy baking—you are in for a rewarding bake!")

st.caption("Monde Bakery Digital Handbook | 2026")
