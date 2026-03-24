import streamlit as st

# Grundinställningar för appen
st.set_page_config(page_title="Monde Bakery Recipe Master", layout="wide")

# CSS för att färglägga surdegsguiden i sidomenyn
st.markdown("""
    <style>
    /* Styling för expandern (knappen) i sidomenyn */
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 2px solid #FF4B4B;
        border-radius: 8px;
        background-color: #FFF5F5;
    }
    /* Gör texten på knappen röd och fetstilt */
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: #FF4B4B !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Monde Bakery - Professional Recipe Master")

# --- RECEPTDATABAS ---
recipes = {
    "Swedish Cinnamon Buns": {
        "ingredients": {
            # Deg (Proportioner från din originalfil)
            "Dough: Wheat Flour": 0.3350,
            "Dough: Milk": 0.2577,
            "Dough: Sourdough": 0.1289,
            "Dough: Cold Butter": 0.0805,
            "Dough: Sugar": 0.0548,
            "Dough: Cardamom": 0.0064,
            "Dough: Salt": 0.0045,
            # Fyllning
            "Filling: Butter": 0.0967,
            "Filling: Sugar": 0.0290,
            "Filling: Cinnamon": 0.0064
        },
        "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Egg Wash",
        "instructions": "1. Autolyse milk/sugar/flour (30m). 2. Mix starter (10m). 3. Add salt (3m). 4. Shape with filling. 5. Cold proof 12h.",
        "pro_tips": """
        * **The Cold Milk Secret:** Always use cold milk to prevent the dough from overheating during kneading.
        * **Knot Tension:** Do not pull too hard when twisting; tight knots will erupt in the center.
        * **Fermentation:** A 12-hour cold proof is essential for the best flavor and color.
        * **Egg Wash Shine:** Mix egg with a pinch of salt and milk for a professional bakery shine.
        * **Internal Temp:** Bake until 92-94°C for perfect moisture.
        """
    },
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.4655, "Water": 0.3292, "Sourdough Starter": 0.1587, 
            "Salt": 0.0132, "Olive Oil": 0.0333, "Dry Yeast": 0.0001
        },
        "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "15s Steam",
        "instructions": "1. Autolyse (40m). 2. Mix starter/salt (10m). 3. Stretch & Fold (3-4 sets). 4. Cold proof (12-14h).",
        "pro_tips": """
        * **The Pan Prep:** Use a generous layer of olive oil (2-3 tbsp) for a 'confit' crust.
        * **The Brine Secret:** Whisk 2 tbsp water, 1 tbsp oil, and salt until milky. Pour into dimples before baking.
        * **Bubble Control:** Be gentle when dimpling to preserve the large CO2 bubbles.
        """
    },
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, "Whole Wheat Flour": 0.0810, "Rye Flour": 0.0357,
            "Water": 0.3051, "Sourdough Starter": 0.1620, "Salt": 0.0162, "Seeds Mix": 0.1052
        },
        "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "15s Steam",
        "instructions": "Autolyse 40m. Mix starter/salt. Stretch & Fold. Add seeds. Cold proof 12-14h.",
        "pro_tips": "Bake until internal temp reaches 98°C. Steam is crucial for the first 15 mins."
    }
}

# --- SIDOMENY: KALKYLATOR ---
st.sidebar.header("Production Calculator")
selected_name = st.sidebar.selectbox("Select Recipe", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units", min_value=1, value=24)
target_weight = st.sidebar.number_input("Target Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()

# --- SIDOMENY: SURDEGSGUIDE (KNAPPEN) ---
with st.sidebar.expander("📖 Sourdough Care Guide"):
    st.info("Professional maintenance for your starter.")
    st.write("""
    **1. What is a Sourdough Starter?**
    A living culture of wild yeast and bacteria. Keep it healthy by regular feeding.

    **2. Daily Care (Frequent Baking)**
    Feed 1-2 times/day at room temp (Ratio: 1:1:1 starter/water/flour). Ready when doubled.

    **3. Cold Storage (Infrequent Baking)**
    Keep in fridge, feed once a week. Weekly: Keep 1kg starter, add 2kg water + 2kg flour. 

    **4. Before Baking**
    Take out and feed (e.g., 1kg water + 1kg flour). Wait 4-6h until peak activity.

    **5. Troubleshooting**
    * *Acetone smell:* Hungry starter, feed more often.
    * *Liquid on top (Hooch):* Stir in or pour off, then feed.
    """)

st.sidebar.divider()
st.sidebar.subheader("Custom Ingredient")
custom_ing_name = st.sidebar.text_input("Ingredient Name", value="Extra Ingredient")
custom_ing_amount = st.sidebar.number_input("Amount (g per unit)", min_value=0, value=0)

st.sidebar.divider()
st.sidebar.header("Economics (LKR)")
raw_cost_per_kg = st.sidebar.number_input("Ingredient Cost (per kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (per unit)", value=900.0)

# --- BERÄKNINGAR ---
total_batch_kg = (units * target_weight) / 1000
total_custom_kg = (units * custom_ing_amount) / 1000
total_dough_mass = total_batch_kg + total_custom_kg

# --- HUVUDLAYOUT ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Production Sheet", "Process", "Pro Tips"])
    
    with tab1:
        st.subheader("Ingredients Weight")
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
        st.subheader("Step-by-Step Guide")
        st.write(recipe["instructions"])
        
    with tab3:
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Baking Specs")
    st.info(f"Oven Temp: {recipe['bake_temp']}")
    st.info(f"Time: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")
    
    st.divider()
    total_cost = total_dough_mass * raw_cost_per_kg * 1.25
    total_revenue = units * selling_price
    total_profit = total_revenue - total_cost
    
    st.subheader("Financial Summary")
    st.metric("Net Profit", f"{total_profit:,.0f} LKR")
    st.write(f"Total Revenue: {total_revenue:,.0f} LKR")
    st.write(f"Production Cost: {total_cost:,.0f} LKR")

st.caption("Monde Bakery Digital Handbook | 2026")
