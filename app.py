import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES ---
recipes = {
    "Monde Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Bread Flour": 0.2947, 
            "Whole Wheat Flour": 0.0810, 
            "Rye Flour": 0.0357,
            "Water": 0.3051, 
            "Sourdough Starter": 0.1620, 
            "Salt": 0.0162,
            "Dry Yeast": 0.0162,
            "Honey": 0.0081,
            "Pumpkin seeds": 0.0243,
            "Sunflower seeds": 0.0243,
            "Red quinoa": 0.0162
        },
        "hydration": 70,
        "default_weight": 800,
        "instructions": """
        1. **Autolyse**: Mix your flour (Wheat, Whole Wheat, Rye) and water first. Let it rest for 40 minutes. This ensures the flour is fully hydrated and the gluten is primed before the salt and starter begin their tightening effect.
        
        2. **Mixing & Kneading**: Add the sourdough starter, dry yeast, honey, and salt. Knead the dough thoroughly for 10 minutes.
        
        3. **Build Strength & Add Seeds**: Perform 3–4 sets of "Stretch and Fold" during the first 2 hours of bulk fermentation, spaced 30 minutes apart. **Fold in all the seeds** (Pumpkin, Sunflower, Quinoa) during these sets to ensure even distribution.
        
        4. **Bulk Fermentation**: Keep your dough at a stable 24–26°C (75–78°F). 
        
        5. **The Poke Test**: Don't rely solely on a timer. Because of the high starter percentage, the dough may reach its limit in 3–4 hours. Look for a 30-50% increase in volume and a "jiggly" surface before shaping.
        
        6. **Slow Proofing**: For best results, proof the dough in the fridge for 12–14 hours. This slow proof develops deeper flavor and makes it much easier to make the scars (scores) in the dough before baking.
        
        7. **Maximize Oven Spring**: To get a professional "ear" and open crumb, you need a high initial heat burst. Ensure your oven and stone are fully preheated.
        """,
        "tips": "Adding the seeds during the folds prevents them from tearing the gluten network during the initial knead!"
    },
    "Focaccia with Sourdough": {
        "ingredients": {"Wheat Flour": 0.4655, "Water": 0.3335, "Sourdough Starter": 0.1817, "Salt": 0.0111, "Olive Oil": 0.0082},
        "hydration": 72,
        "default_weight": 500,
        "instructions": "Autolyse 40 min (flour/water/yeast), add starter/salt, 10 min knead, 4 folds, cold proof 12-14h. Bake at 245°C with 15s steam.",
        "tips": "Use high initial heat and plenty of olive oil for a crispy base!"
    },
    "Artisan Levain French Sourdough": {
        "ingredients": {"Wheat Flour": 0.4965, "Water": 0.3308, "Sourdough Starter": 0.1613, "Salt": 0.0114},
        "hydration": 67,
        "default_weight": 800,
        "instructions": "Autolyse 40 min, 4 folds, cold proof 12-14h. Bake at 245°C with steam.",
        "tips": "Look for a jiggly surface before cold proofing."
    }
}

# --- SIDEBAR: SETTINGS & COSTING ---
st.sidebar.header("Recipe Settings")
selected_name = st.sidebar.selectbox("Select Bread Type", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Units (pcs)", min_value=1, value=1)
target_weight = st.sidebar.number_input("Weight per Unit (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.header("Costing & Profit Planning")
# Raw material cost (LKR/kg)
raw_cost_per_kg = st.sidebar.number_input("Raw Material Cost (LKR/kg)", value=224.0)
# Planned out-price (Selling price per unit)
selling_price = st.sidebar.number_input("Planned Selling Price (LKR/unit)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
# Estimated total cost = total weight * raw material cost (including ~25% overhead for power/labor)
total_cost = total_batch_kg * raw_cost_per_kg * 1.25 
total_revenue = units * selling_price
total_profit = total_revenue - total_cost
margin_pct = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0

# Sidebar Financial Summary
st.sidebar.subheader("Profit Summary")
st.sidebar.metric("Estimated Margin", f"{margin_pct:.1f}%")
st.sidebar.write(f"**Total Revenue:** {total_revenue:,.0f} LKR")
st.sidebar.write(f"**Total Cost:** {total_cost:,.0f} LKR")
st.sidebar.write(f"**Net Profit:** {total_profit:,.0f} LKR")

# --- MAIN DISPLAY ---
st.header(f"🍞 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Production Sheet", "Baking Instructions"])
    
    with tab1:
        st.write("### Ingredient Breakdown")
        # Table Header
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingredient**")
        h2.write("**Weight**")
        h3.write("**% of Total**")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_batch_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 2])
            r1.write(ing)
            r2.write(f"**{val:.2f} {unit}**")
            r3.write(f"{ratio*100:.2f}%")
            
        st.divider()
        st.metric("Total Batch Weight", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.write("### Professional Step-by-Step Guide")
        st.write(recipe["instructions"])

with col_right:
    st.subheader("Technical Specs")
    st.metric("Hydration Level", f"{recipe['hydration']}%")
    
    st.divider()
    st.subheader("Pro Baker's Tips")
    st.success(recipe["tips"])
    
    st.info("💡 **Happy baking—you’re in for a rewarding baker!**")

st.caption("Monde Bakery Digital Handbook | Precision Management")
