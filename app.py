import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES ---
recipes = {
    # ... (Här finns dina andra recept: Multi Grain, Baguette, etc. De förblir oförändrade)
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75,
        "default_weight": 800,
        "bake_temp": "245°C",
        "bake_time": "25-30 min",
        "steam": "15 sec",
        "instructions": """
        1. **Autolyse**: Mix flour, dry yeast and water. Rest **40 min**.
        2. **Mix**: Add starter and salt. Knead **10 min**.
        3. **Strength**: 3–4 sets of **Stretch and Folds** every 30 min.
        4. **Bulk**: 3–4 hours at 24–26°C until "jiggly".
        5. **Cold Proof**: 12–14 hours in fridge.
        6. **Bake**: 245°C for 25-30 min. 15s steam at start.
        """,
        "pro_tips": """
        ### Deep Dive: Professional Focaccia Tips
        
        * **Preparing the Pan:** Focaccia is essentially "shallow-fried". Use a **generous layer of olive oil** in the bottom of the pan to create that golden, crunchy underside.
        * **The Big Stretch (Dimpling):** After cold proof, let the dough rest in the pan for 30–60 min to relax the gluten. Once bubbly, oil your hands and press your fingers deep into the dough until you feel the bottom.
        
        
        
        * **The Secret Brine:** Mix 2 tbsp water + 1 tbsp olive oil + salt. Pour this emulsion into the dimples before baking. This keeps the holes open and the top incredibly moist.
        * **Toppings:** Press rosemary or tomatoes deep into the dough so they don't burn.
        * **Placement:** Bake in the lower part of the oven for the first 15 mins for a crispy base, then move to the middle. Target internal temp: **96–98°C**.
        """
    },
    # ... (Resten av dina recept fortsätter här)
}

# --- SIDEBAR & CALCULATIONS (Samma som tidigare) ---
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Loaves/Pieces", min_value=1, value=5)
target_weight = st.sidebar.number_input("Target Weight (g)", value=recipe["default_weight"])

total_batch_kg = (units * target_weight) / 1000
# (Finansiella beräkningar här...)

# --- MAIN DISPLAY ---
st.header(f"🥖 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Baking Steps", "Pro Tips"])
    
    with tab1:
        st.subheader("Ingredients List")
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_weight = ing_weight if unit == "kg" else ing_weight * 1000
            st.write(f"{ing}: **{display_weight:.2f} {unit}**")

    with tab2:
        st.subheader("Professional Process")
        st.write(recipe["instructions"])
        
    with tab3:
        if "pro_tips" in recipe:
            st.write(recipe["pro_tips"])
        else:
            st.write("No specific pro tips added for this recipe yet.")

with col_right:
    st.subheader("Baking Specs")
    st.info(f"**Oven Temp:** {recipe['bake_temp']}")
    st.info(f"**Time:** {recipe['bake_time']}")
    st.info(f"**Steam:** {recipe['steam']}")

st.info("💡 **Happy baking—you’re in for a rewarding bake!**")
