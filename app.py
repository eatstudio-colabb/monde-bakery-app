import streamlit as st

st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# --- CUSTOM CSS FÖR FÄRGAD KNAPP ---
st.markdown("""
    <style>
    div[data-testid="stExpander"] {
        border: 2px solid #FF4B4B;
        border-radius: 5px;
        background-color: #FFF5F5;
    }
    .st-emotion-cache-p4mowd {
        color: #FF4B4B;
        font-weight: bold;
    }
    </style>
    """, unsafe_all_tags=True)

st.title("Monde Bakery - Professional Recipe Master")

# --- DATA: RECIPES DATABASE ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            "Dough: Wheat Flour": 0.3350,
            "Dough: Milk": 0.2577,
            "Dough: Sourdough": 0.1289,
            "Dough: Cold Butter": 0.0805,
            "Dough: Sugar": 0.0548,
            "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045,
            "Filling: Butter": 0.0967,
            "Filling: Sugar": 0.0290,
            "Filling: Cinnamon": 0.0064
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "steam": "Egg Wash",
        "instructions": "1. Autolyse milk/sugar/flour (30m). 2. Mix starter (10m). 3. Add salt (3m). 4. Shape with filling. 5. Cold proof 12h.",
        "pro_tips": "Use cold milk to control friction heat. Do not over-tighten knots. Internal temp: 92-94°C."
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt. 3-4 sets of folds. Cold proof 12-14h.",
        "pro_tips": "Use a heavy brine of water and olive oil in the dimples before baking."
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, 
            "Seeds Mix": 0.1052
        },
        "hydration": 70, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "steam": "15 sec",
        "instructions": "Autolyse 40m. Mix starter/salt. Stretch & Fold. Cold proof 12-14h.",
        "pro_tips": "Bake until internal temp reaches 98°C."
    }
}

# --- SIDEBAR: CALCULATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()

# --- NY PLACERING: SURDEGSGUIDE PÅ ENGELSKA ---
with st.sidebar.expander("📖 Sourdough Care Guide"):
    st.info("Professional maintenance for your starter.")
    st.write("""
    **1. What is a Sourdough Starter?**
    A living culture of wild yeast and lactic acid bacteria. Keep it healthy by regular feeding.

    **2. Daily Care (Frequent Baking)**
    Feed 1-2 times/day at room temp. 
    * Ratio: 1 part starter + 1 part water + 1 part flour.
    * Ready when doubled in volume (approx. 4-8 hours).

    **3. Cold Storage (Infrequent Baking)**
    * Keep in fridge, feed once a week.
    * Weekly: Keep 1kg starter, add 2kg water + 2kg flour. Let sit for 1-2h before refrigerating.

    **4. Before Baking**
    Take out of fridge and feed (e.g., 1kg water + 1kg flour). Wait 4-6h until peak activity.

    **5. Flour Choice**
    Wheat, Whole Wheat, or Rye. Adding a bit of Rye makes it more active.

    **6. Signs of Health**
    Fruity/yogurty smell, active bubbling, doubling in size.

    **7. Troubleshooting**
    * *Acetone smell:* Hungry starter, feed more often.
    * *Liquid on top (Hooch):* Normal hunger sign. Stir in or pour off, then feed.
    """)

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
        st.write(f"Calculating for {units} units at {target_weight}g each.")
        st.markdown("---")
        
        c1, c2, c3 = st.columns([3, 2, 1])
        c1.write("**Ingredient Name**")
        c2.write("**Required Weight**")
        c3.write("**Ratio**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            display_val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(ing)
            r2.write(f"**{display_val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
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
        st.subheader("Process")
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

st.caption("Monde Bakery Digital Handbook | 2026")
