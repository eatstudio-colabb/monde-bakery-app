import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES ---
recipes = {
    "Swedish Cinnamon Buns (Sourdough)": {
        "ingredients": {
            "Wheat Bread Flour": 0.5050, 
            "Milk (Cold)": 0.2525, 
            "Sourdough Starter": 0.1500,
            "Butter (Room Temp)": 0.0758,
            "Sugar": 0.0758,
            "Egg (for dough)": 0.0505,
            "Cardamom (Ground)": 0.0051,
            "Salt": 0.0051,
            "Cinnamon Filling (Butter/Sugar/Cinnamon)": 0.1500
        },
        "hydration": 50, 
        "default_weight": 80,
        "bake_temp": "175–200°C",
        "bake_time": "15–20 min",
        "steam": "None (Egg wash)",
        "instructions": """
        1. **Prepare the Dough & Autolyse**: Mix milk, ground cardamom, and sugar. Gradually add flour until you have a smooth dough. Knead for **2–3 minutes**, then let it rest (**Autolyse**) for **30 minutes**.
        2. **Incorporate Starter**: Add the sourdough starter and knead for **10 minutes**.
        3. **Salt Integration**: Add salt and knead for **3 more minutes** until the dough is strong and elastic.
        4. **The Filling**: In a separate bowl, mix softened butter, sugar, and cinnamon until well combined.
        5. **Shaping**: Roll out the dough into a rectangle (one finger thick). Spread filling over two-thirds of the dough. Fold the unfilled part over, then fold the remaining part over that. Stretch into an even rectangle.
        6. **Knots**: Cut into 2 cm strips. Twist each strip around three fingers twice to form a knot, tucking the end into the center.
        7. **Cold Proof**: Cover with plastic wrap and place in the refrigerator for **12 hours** (overnight).
        8. **Finishing**: Brush with egg wash (egg + splash of milk) and sprinkle with pearl sugar.
        9. **Baking**: Bake at **175–200°C** for 15–20 minutes. Check the underside for a nice golden color.
        """,
        "pro_tips": """
        * **Autolyse Benefit:** The 30-minute rest after the initial mix allows the flour to hydrate fully, making the 10-minute knead with the starter much more effective.
        * **The "Knot" Technique:** Using three fingers as a guide ensures consistent size and tension in your buns.
        
        
        
        * **Overnight Proof:** The 12-hour cold proof is the secret to the complex sourdough flavor and a perfect, soft texture.
        * **Bottom Check:** Don't just look at the top; use a spatula to lift a bun and check that the bottom is caramelized and firm.
        """
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix": 0.1052
        },
        "hydration": 70, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "steam": "15 sec",
        "instructions": "Autolyse 40m, add starter/salt, knead 10m. Stretch & Fold with seeds. Cold proof 12-14h.",
        "pro_tips": "Bake to 98°C internal temp."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 10m. Stretch & Fold. Cold proof 12-14h.",
        "pro_tips": "Generous olive oil in pan. Brine the dimples."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 10m. Stretch & Fold. Cold proof 12-14h.",
        "pro_tips": "Toast walnuts first. Fold in during 2nd set of folds."
    }
}

# --- SIDEBAR & CALCULATIONS ---
st.sidebar.header("Bakery Management")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=20)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

total_batch_kg = (units * target_weight) / 1000

# --- MAIN DISPLAY ---
st.header(f"🥖 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Core Process", "Pro Tips (English)"])
    
    with tab1:
        st.subheader("Ingredients List")
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_weight = ing_weight if unit == "kg" else ing_weight * 1000
            st.write(f"{ing}: **{display_weight:.2f} {unit}**")
        st.divider()
        st.metric("Total Batch Weight", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.subheader("Professional Process")
        st.write(recipe["instructions"])
        
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"**Oven Temp:** {recipe['bake_temp']}")
    st.info(f"**Time:** {recipe['bake_time']}")
    st.info(f"**Steam/Finish:** {recipe['steam']}")
    
    st.divider()
    st.success("💡 Happy baking—you’re in for a rewarding bake!")

st.caption("Monde Bakery Digital Handbook | 2026")
