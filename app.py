import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

st.title("🥖 Monde Bakery - Professional Recipe Master")

# --- DATA: RECIPES DATABASE ---
recipes = {
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour, dry yeast, and water. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds** every 30 min.
        4. **Bulk**: 3–4 hours at 24–26°C until "jiggly".
        5. **Proof**: 12–14 hours in fridge (Cold Proof).
        6. **Bake**: 245°C for 25-30 min. 15s steam at start.
        """,
        "pro_tips": """
        ### 🏆 Deep Dive: The Ultimate Focaccia Guide
        
        * **The Pan Prep (Crucial!):** Focaccia is essentially "shallow-fried" in the oven. Pour a **generous layer of olive oil** (at least 2-3 tbsp) into the bottom of the pan. This creates the golden, crunchy "confit" crust underneath.
        * **The Big Stretch (Dimpling):** After the cold proof, transfer the dough to the pan. **Do not force it.** Let it rest for 30–60 min at room temp to relax the gluten. Once it has spread naturally, oil your hands and press your fingers deep into the dough until you feel the metal of the pan.
        * **The "Brine" Secret:** Mix 2 tbsp warm water with 1 tbsp olive oil and a pinch of salt. Whisk until it turns milky (emulsified). Pour this into the dimples right before baking. It keeps the holes from closing and makes the top incredibly soft while the bottom stays crispy.
        * **Bubble Control:** The 12–14 hour cold fermentation creates large CO2 bubbles. Be careful not to pop them! When dimpling, work *around* the biggest bubbles to keep that airy structure.
        * **Topping Placement:** If using rosemary, soak the sprigs in water for 5 minutes first; this prevents them from burning in the high heat. Press tomatoes or olives deep into the dough so they are "embraced" by the bread.
        * **Bottom Crispiness:** For an extra-crunchy base, bake on the lowest rack for the first 15 minutes, then move it to the middle. Internal temp should be **96–98°C**.
        * **Post-Bake Care:** As soon as it comes out, brush the top with a little more fresh olive oil. Let it rest in the pan for only 5 minutes, then move to a wire rack so the bottom doesn't get soggy from steam.
        """
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix (Chia/Flax/Sesam/Quinoa)": 0.1052
        },
        "hydration": 70, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt (10m knead). Stretch & Fold (3-4 sets). Add seeds. Cold proof 12-14h. Bake 245°C.",
        "pro_tips": "Bake until internal temp reaches **98°C**. Steam is crucial for the first 15 mins to allow full expansion."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m with yeast. Add starter/salt (10m knead). Fold in walnuts. Cold proof 12-14h.",
        "pro_tips": "Toast walnuts lightly first. The cold proof makes 'scars' (scoring) much easier and cleaner."
    },
    "Sourdough Cinnamon Buns": {
        "ingredients": {
            "Wheat Bread Flour": 0.5050, "Milk (Cold)": 0.2525, "Sourdough Starter": 0.1500,
            "Butter (Room Temp)": 0.0758, "Sugar": 0.0758, "Egg (Dough)": 0.0505,
            "Cardamom": 0.0051, "Salt": 0.0051, "Cinnamon Filling": 0.1500
        },
        "hydration": 50, "default_weight": 80, "bake_temp": "175–200°C", "bake_time": "15–20 min", "steam": "Egg Wash",
        "instructions": "Autolyse milk/cardamom/sugar/flour (30m). Add starter (10m knead). Add salt (3m knead). Shape knots. Cold proof 12h.",
        "pro_tips": "Check the underside for caramel color. Use the 3-finger twist for perfect knots."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "hydration": 80, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "80% hydration. Autolyse 40m. 4 sets of folds. Handle like a pillow. Cold proof 12-14h.",
        "pro_tips": "Very slack dough; use plenty of flour on the bench and don't degas during shaping."
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Dry Yeast": 0.0001
        },
        "hydration": 70, "default_weight": 350, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 5m slow + 4m fast. 4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "The fast kneading builds specific tension. Score at a shallow angle."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Wheat Bread Flour": 0.4965, "Water": 0.3308, "Sourdough Starter": 0.1595, "Salt": 0.0132, "Dry Yeast": 0.0001
        },
        "hydration": 72, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Knead 10m. 4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "Focus on the initial heat burst and steam to get the professional 'ear' and shine."
    }
}

# --- SIDEBAR: CALCULATOR ---
st.sidebar.header("📊 Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=10)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.header("💰 Economics (LKR)")
raw_cost_per_kg = st.sidebar.number_input("Ingredient Cost (per kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
total_cost = total_batch_kg * raw_cost_per_kg * 1.25 
total_revenue = units * selling_price
total_profit = total_revenue - total_cost

# --- MAIN DISPLAY ---
st.header(f"🍞 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["📝 Production Sheet", "🥣 Core Process", "💡 Pro Tips (English)"])
    
    with tab1:
        st.subheader("Ingredients Weight")
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            st.write(f"{ing}: **{display_val:.2f} {unit}** ({ratio*100:.1f}%)")
        st.divider()
        st.metric("Total Dough Weight", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.subheader("Step-by-Step Guide")
        st.write(recipe["instructions"])
        
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"**Oven Temp:** {recipe['bake_temp']}")
    st.info(f"**Time:** {recipe['bake_time']}")
    st.info(f"**Steam/Finish:** {recipe['steam']}")
    
    st.divider()
    st.subheader("Financial Summary")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"**Total Revenue:** {total_revenue:,.0f} LKR")
    
    st.divider()
    st.success("Happy baking—you’re in for a rewarding bake!")

st.caption("Monde Bakery Digital Handbook | 2026")
