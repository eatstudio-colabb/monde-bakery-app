import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES WITH HYDRATION & DETAILED RATIOS ---
recipes = {
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, 
            "Water": 0.2417, 
            "Poolish": 0.2417, 
            "Salt": 0.0089, 
            "Dry Yeast": 0.0001
        },
        "hydration": 65,
        "default_weight": 350,
        "instructions": """
        1. **Autolyse & Mix**: Mix your flour and water first and let it rest for 40 minutes before adding the poolish and salt. This ensures the flour is fully hydrated and the gluten is primed before the salt begins its tightening effect. Knead the dough slow for 5 minutes and fast for 4 minutes.

        2. **Stretch and Folds**: Even at a lower hydration, using the Stretch and Fold method builds strength. Perform 3–4 sets of folds during the first 2 hours of bulk fermentation, spaced 30 minutes apart. This builds a strong gluten network gradually, allowing the dough to hold the gases without collapsing.

        3. **Bulk Fermentation**: Keep your dough at a stable 24–26°C (75–78°F). Do not rely solely on a timer. Look for a 30-50% increase in volume and a "jiggly" surface before shaping (the Poke Test).

        4. **Cold Proofing (Highly Recommended)**: It is best if you can proof the dough in the fridge for 12–14 hours for slow proofing. This develops flavor and makes it much easier to make the scars (score) in the dough!

        5. **Maximize Oven Spring (Preheat & Loading)**: To get a professional "ear" and open crumb, you need a high initial heat burst. Preheat your oven and baking stone to 250°C (480°F). Score the baguettes cleanly.

        6. **Steam & Bake**: Bake at 245°C for 25-30 minutes. Inject 15 seconds of steam right at the start. Use plenty of steam during the first 15–20 minutes to keep the crust supple, allowing the bread to expand fully.
        """,
        "tips": "Steaming is vital for baguettes! Cold-fermenting makes cutting overlapping decorative scores infinitely easier."
    },
    "Artisan Levain French Sourdough": {
        "ingredients": {
            "Wheat Flour": 0.4965, 
            "Water": 0.3308, 
            "Sourdough Starter": 0.1613, 
            "Salt": 0.0114
        },
        "hydration": 67,
        "default_weight": 800,
        "instructions": """
        1. **Autolyse & Mix**: Mix flour and water first. Let rest for 40 minutes. Add starter and salt. Knead for 10 minutes.
        2. **Stretch and Fold**: Perform 3–4 sets of folds in the first 2 hours (every 30 mins).
        3. **Bulk Fermentation**: Stable 24–26°C. Look for a 30-50% volume increase. 
        4. **Cold Proof**: Retard in the fridge for 12-14 hours.
        5. **Baking**: Preheat to 250°C. Score and drop heat to 245°C. Inject 15 sec steam at start.
        """,
        "tips": "Hold your scoring blade at a 45-degree angle to lift a beautiful 'ear' flap."
    },
    "Focaccia with Sourdough": {
        "ingredients": {"Wheat Flour": 0.4655, "Water": 0.3335, "Sourdough": 0.1817, "Salt": 0.0111, "Olive Oil": 0.0082},
        "hydration": 72,
        "default_weight": 500,
        "instructions": "Mix flour, water, and starter. Autolyse 30 min. Add salt/oil. 4 sets of folds. Proof in tray with plenty of olive oil. Dimple heavily and bake at 230°C.",
        "tips": "Use your fingertips to create deep craters just before baking to trap olive oil and salt pockets."
    },
    "Sourdough Ciabatta": {
        "ingredients": {"Wheat Flour": 0.5389, "Water": 0.4001, "Sourdough": 0.0500, "Salt": 0.0110},
        "hydration": 82,
        "default_weight": 300,
        "instructions": "Mix until shiny. Perform coil folds every 30-45 mins. Tip onto heavily floured surface, cut into slippers, and do not de-gas.",
        "tips": "Extremely sticky dough! Use wet hands during folds and pull the edges gently to avoid tearing."
    }
}

# --- SIDEBAR: SETTINGS & LIVE ECONOMICS ---
st.sidebar.header("Recipe Settings")
selected_name = st.sidebar.selectbox("Select Bread Type", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of units (pcs)", min_value=1, value=1)
target_weight = st.sidebar.number_input("Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.header("Costing & Profit")
flour_price = st.sidebar.number_input("Average Flour Price (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price per unit (LKR)", value=900.0)

# Real-time Economic Logic
total_batch_kg = (units * target_weight) / 1000
raw_cost = total_batch_kg * flour_price * 0.6  # Standard baseline factor
total_sales = units * selling_price
total_profit = total_sales - raw_cost
margin_percent = (total_profit / total_sales) * 100 if total_sales > 0 else 0

# Sidebar Output Box
st.sidebar.info(f"""
**Financial Overview Summary**
* **Total Cost:** {raw_cost:.0f} LKR
* **Total Sales:** {total_sales:.0f} LKR
* **Estimated Profit:** {total_profit:.0f} LKR
* **Profit Margin: {margin_percent:.1f}%**
""")


# --- MAIN UI DISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Ingredient Scaling", "Baking Step-by-Step Instructions"])
    
    with tab1:
        st.write("### Production Scaling (Grams and Kilos)")
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingredient Component**")
        h2.write("**Scaled Amount**")
        h3.write("**% of Total Dough Mass**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 2])
            r1.write(ing)
            r2.write(f"**{val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
            
        st.divider()
        st.metric("Total Overall Batch Weight", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.write("### Detailed Execution Steps")
        st.write(recipe["instructions"])

with col_right:
    st.subheader("Baking Dashboard Overview")
    st.metric("Calculated Hydration (Water/Flour)", f"{recipe['hydration']}%")
    
    st.divider()
    st.subheader("Master Professional Tips")
    st.success(recipe["tips"])
    
    st.divider()
    st.write("Happy baking—you’re in for a rewarding baker experience! 🧑‍🍳🥖")

st.caption("Monde Bakery Digital Hand-Book Platform – Designed for cellular metrics precision.")
