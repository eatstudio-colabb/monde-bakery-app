import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES ---
recipes = {
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix (Chia/Flax/Sesam/Quinoa)": 0.1052
        },
        "hydration": 70,
        "default_weight": 1000,
        "bake_temp": "245°C",
        "bake_time": "45 min (Inner temp 98°C)",
        "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour and water. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds** every 30 min. **Add all seeds** during the folds.
        4. **Bulk**: 3–4 hours at 24–26°C until "jiggly" (30-50% growth).
        5. **Proof**: 12–14 hours in fridge (Cold Proof).
        6. **Bake**: 245°C for 45 min (or 98°C core). 15s steam at start.
        """
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650, "Dry Yeast": 0.0001
        },
        "hydration": 70,
        "default_weight": 800,
        "bake_temp": "245°C",
        "bake_time": "25-30 min",
        "steam": "15 sec",
        "instructions": """
        1. **Autolyse & Salt Integration**: Mix your flour, water and dry yeast first. Let it rest for **40 minutes**. This ensures the flour is fully hydrated and the gluten is primed. After rest, add starter and salt. Knead for **10 minutes**.
        2. **Strength (Stretch and Folds)**: Perform **3–4 sets of folds** during the first 2 hours of bulk fermentation, spaced 30 minutes apart. This builds a strong gluten network gradually.
        3. **Bulk Fermentation**: Keep dough at **24–26°C**. Use the **"Poke Test"**: look for 30-50% increase in volume and a "jiggly" surface (usually 3–4 hours).
        4. **Cold Proof**: Proof in fridge for **12–14 hours**. This makes it much easier to make the scars (scoring) in the dough.
        5. **Oven Spring**: Preheat oven and stone to **250°C**. Bake at **245°C for 25-30 min**. Inject **15 seconds of steam** at the start.
        """
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, "Sourdough Starter": 0.1796, 
            "Water": 0.2695, "Salt": 0.0120, "Dry Yeast": 0.0001
        },
        "hydration": 80,
        "default_weight": 300,
        "bake_temp": "245°C",
        "bake_time": "25-30 min",
        "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour, water and dry yeast. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds** every 30 min. 
        4. **Bulk**: 3–4 hours at 24–26°C.
        5. **Proof**: 12–14 hours in fridge.
        6. **Bake**: 245°C for 25-30 min. 15s steam at start.
        """
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2660, 
            "Salt": 0.0088, "Dry Yeast": 0.0001
        },
        "hydration": 70,
        "default_weight": 350,
        "bake_temp": "245°C",
        "bake_time": "25-30 min",
        "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour and water. Rest **40 min**.
        2. **Mix**: Add poolish and salt. Knead slow 5 min, then fast 4 min.
        3. **Strength**: 3–4 sets of **Stretch and Folds** every 30 min.
        4. **Bulk**: 3–4 hours at 24–26°C.
        5. **Proof**: 12–14 hours in fridge.
        6. **Bake**: 245°C for 25-30 min. 15s steam at start.
        """
    },
    "Artisan French Levain": {
        "ingredients": {
            "Wheat Bread Flour": 0.4965, "Water": 0.3308, "Sourdough Starter": 0.1595, 
            "Salt": 0.0132, "Dry Yeast": 0.0001
        },
        "hydration": 72,
        "default_weight": 800,
        "bake_temp": "245°C",
        "bake_time": "25-30 min",
        "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour, water and dry yeast. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds** every 30 min.
        4. **Bulk**: 3–4 hours at 24–26°C.
        5. **Proof**: 12–14 hours in fridge.
        6. **Bake**: 245°C for 25-30 min. 15s steam at start.
        """
    }
}

# --- SIDEBAR: SETTINGS ---
st.sidebar.header("Bakery Management")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Loaves/Pieces", min_value=1, value=5)
target_weight = st.sidebar.number_input("Target Weight (g)", value=recipe["default_weight"])

st.sidebar.divider()
raw_cost_per_kg = st.sidebar.number_input("Ingredient Cost (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (LKR/pc)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
total_cost = total_batch_kg * raw_cost_per_kg * 1.25 
total_revenue = units * selling_price
total_profit = total_revenue - total_cost

# --- MAIN DISPLAY ---
st.header(f"🍞 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Production Sheet", "Baking Steps"])
    
    with tab1:
        st.subheader("Ingredients List")
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_weight = ing_weight if unit == "kg" else ing_weight * 1000
            
            c1, c2, c3 = st.columns([3, 2, 2])
            c1.write(ing)
            c2.write(f"**{display_weight:.2f} {unit}**")
            c3.write(f"({ratio*100:.1f}%)")
        st.divider()
        st.metric("Total Dough Weight", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.subheader("Professional Process")
        st.write(recipe["instructions"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"**Oven Temp:** {recipe['bake_temp']}")
    st.info(f"**Time:** {recipe['bake_time']}")
    st.info(f"**Steam:** {recipe['steam']}")
    
    st.divider()
    st.subheader("Financials")
    st.metric("Estimated Profit", f"{total_profit:,.0f} LKR")
    st.metric("Total Revenue", f"{total_revenue:,.0f} LKR")

st.info("💡 **Happy baking—you’re in for a rewarding bake!**")
st.caption("Monde Bakery Digital Handbook")
