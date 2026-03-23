import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES ---
recipes = {
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Flour": 0.4655, 
            "Water": 0.3335, 
            "Sourdough Starter": 0.1817, 
            "Salt": 0.0111, 
            "Olive Oil": 0.0082
        },
        "hydration": 72,
        "default_weight": 500,
        "instructions": """
        1. **Autolyse & Yeast Prep**: Mix your flour, dry yeast, and water first. Let it rest for 40 minutes. This ensures the flour is fully hydrated and the gluten is primed before the salt begins its tightening effect.
        
        2. **Mixing**: Add the sourdough starter and salt. Knead the dough for 10 minutes.
        
        3. **Build Strength (Stretch & Fold)**: At 70%+ hydration, you don't need aggressive kneading. Perform 3–4 sets of "Stretch and Folds" during the first 2 hours of bulk fermentation, spaced 30 minutes apart. This builds a strong gluten network gradually.
        
        4. **Bulk Fermentation**: Keep the dough at a stable 24–26°C (75–78°F). Use the "Poke Test"—look for a 30-50% increase in volume and a "jiggly" surface before shaping (usually 3-4 hours).
        
        5. **Cold Proof**: For the best flavor and texture, proof the dough in the fridge for 12–14 hours. This slow proof makes it easier to handle and improves the crumb.
        
        6. **Maximize Oven Spring**: Preheat your oven and baking stone to 250°C (480°F). Load the focaccia and set the oven to 245°C.
        
        7. **Steam Control**: Inject 15 seconds of steam immediately at the start. Use plenty of steam for the first 15–20 minutes to keep the crust supple, allowing the bread to expand fully. Bake for 25-30 minutes total.
        """,
        "tips": "Use high initial heat and plenty of olive oil in the tray to get that signature crispy bottom and airy top!"
    },
    "Artisan Levain French Sourdough": {
        "ingredients": {"Wheat Flour": 0.4965, "Water": 0.3308, "Sourdough Starter": 0.1613, "Salt": 0.0114},
        "hydration": 67,
        "default_weight": 800,
        "instructions": "Autolyse 40 min, mix salt/starter, 4 folds, cold proof 12-14h, bake at 245°C with steam.",
        "tips": "Ensure the dough is 'jiggly' before cold proofing."
    },
    "Baguette with Poolish": {
        "ingredients": {"Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2417, "Salt": 0.0089, "Dry Yeast": 0.0001},
        "hydration": 65,
        "default_weight": 300,
        "instructions": "5 min slow/4 min fast mix. Autolyse included. Cold proof 12-14h. Bake with 15s steam.",
        "tips": "Steam is critical for the baguette's crust color and shine."
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
flour_price = st.sidebar.number_input("Flour/Ingredient Cost (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price per Unit (LKR)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
# Cost estimation (adjusted for overhead like oil/salt/utilities)
est_unit_cost = (total_batch_kg * flour_price * 1.25) / units 
total_cost = est_unit_cost * units
total_revenue = units * selling_price
total_profit = total_revenue - total_cost
margin = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0

# Sidebar Financial Summary
st.sidebar.info(f"""
**Financial Overview:**
* Total Batch Cost: {total_cost:.0f} LKR
* Total Revenue: {total_revenue:.0f} LKR
* **Profit Margin: {margin:.1f}%**
""")

# --- MAIN DISPLAY ---
st.header(f"🍞 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Production Sheet", "Baking Instructions"])
    
    with tab1:
        st.write("### Ingredient Breakdown")
        # Custom Table Header
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingredient**")
        h2.write("**Weight**")
        h3.write("**% of Total Dough**")
        
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

st.caption("Monde Bakery Digital Handbook | Precision Sourdough Management")
