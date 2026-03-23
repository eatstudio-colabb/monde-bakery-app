import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

st.title("Monde Bakery - Professional Recipe Master")

# --- DATA: RECIPES DATABASE ---
recipes = {
    "Sourdough Cinnamon Buns": {
        "ingredients": {
            "Wheat Bread Flour": 0.5050, "Milk (Cold)": 0.2525, "Sourdough Starter": 0.1500,
            "Butter (Room Temp)": 0.0758, "Sugar": 0.0758, "Egg (Dough)": 0.0505,
            "Cardamom": 0.0051, "Salt": 0.0051, "Cinnamon Filling": 0.1500
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "steam": "Egg Wash",
        "instructions": """
        1. Autolyse: Mix milk, cardamom, sugar and flour. Knead 2-3 min. Rest 30 min.
        2. Mix: Add sourdough starter and knead 10 min. 
        3. Salt: Add salt and knead 3 more min until strong and elastic.
        4. Filling: Mix softened butter, sugar, and cinnamon.
        5. Shape: Roll to 1cm thick. Spread filling, fold in three. Cut 2cm strips and twist into knots.
        6. Proof: Cover and cold proof in fridge for 12 hours (overnight).
        7. Bake: Brush with egg wash + milk. Sprinkle pearl sugar. Bake 175–200°C.
        """,
        "pro_tips": """
        ### Deep Dive: Professional Cinnamon Bun Tips
        
        * The Cold Milk Secret: Always use cold milk. The friction during the long kneading process generates heat. Starting cold prevents the dough from getting too warm, which would weaken the gluten and make the butter melt prematurely.
        * Flour Graduality: When mixing, keep a small portion of flour aside. Add it slowly until the dough just clears the sides of the bowl. A slightly tackier dough results in a much softer bun.
        * Butter Integration: If adding butter separately, ensure it is "pliable" (soft like clay but not melted). Adding it after the gluten has developed (after the sourdough knead) creates a brioche-like structure.
        * The Knot Tension: When twisting around your fingers, don't pull too hard. If the knot is too tight, the center will pop out like a volcano in the oven instead of expanding evenly.
        * Fermentation Peak: Sourdough buns need a long, slow rise. The 12-hour cold proof develops the lactic acid which breaks down the starches into sugars, resulting in a superior caramelization (crust color).
        * The Egg Wash Shine: For a professional "bakery shine", whisk your egg with a pinch of salt and a splash of milk. Let the wash sit for 10 minutes before brushing; this breaks down the egg proteins for a smoother coat.
        * Avoiding Dry Buns: Do not overbake! Take them out when the internal temperature hits 92-94°C. Immediately after baking, you can brush them with a simple sugar syrup to trap the moisture inside.
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
        "pro_tips": "Bake until internal temp reaches 98°C. Steam is crucial for volume."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse with yeast 40m. Add starter/salt. Knead 10m. Fold in walnuts.",
        "pro_tips": "Toast walnuts lightly before adding for better flavor."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "hydration": 80, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. 4 sets of folds. Cold proof 12-14h. Handle gently.",
        "pro_tips": "High hydration. Use a well-floured surface and don't degas."
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 350, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 5m slow + 4m fast. Cold proof 12-14h.",
        "pro_tips": "Score at a very shallow angle to get the 'ear'."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Wheat Bread Flour": 0.4965, "Water": 0.3308, "Sourdough Starter": 0.1595, "Salt": 0.0132, "Dry Yeast": 0.0001
        },
        "hydration": 72, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 10m. 4 folds. Cold proof 12-14h.",
        "pro_tips": "Focus on high initial heat and steam."
    }
}

# --- SIDEBAR: CALCULATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=10)
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
