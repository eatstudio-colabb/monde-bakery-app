import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES WITH HYDRATION & DETAILED RATIOS ---
recipes = {
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
        1. **Autolyse & Mix**: Mix flour, water, and dry yeast (if using) first. Let rest for 40 minutes. Then add the sourdough starter and salt. Knead the dough for 10 minutes. This ensures the flour is fully hydrated before the salt tightens the gluten.
        
        2. **Stretch and Fold**: At 70% hydration, aggressive kneading isn't needed. Perform 3–4 sets of "stretch and folds" during the first 2 hours of bulk fermentation, spaced 30 minutes apart.
        
        3. **Bulk Fermentation**: Keep dough at 24–26°C. Don't rely solely on a timer; look for a 30-50% increase in volume and a "jiggly" surface (usually 3-4 hours).
        
        4. **Cold Proof (Recommended)**: Proof in the fridge for 12-14 hours. This develops flavor and makes the dough much easier to score (scar).
        
        5. **Baking**: Preheat oven and baking stone to 250°C. Score the bread and load it. Lower temperature to 245°C.
        
        6. **Steam**: Inject 15 seconds of steam immediately at the start. Use plenty of steam for the first 15–20 minutes to keep the crust supple for maximum oven spring. Bake for 25-30 minutes total.
        """,
        "tips": "For a professional 'ear', ensure high initial heat and consistent steam in the first phase!"
    },
    "Focaccia with Sourdough": {
        "ingredients": {"Wheat Flour": 0.4655, "Water": 0.3335, "Sourdough": 0.1817, "Salt": 0.0111, "Olive Oil": 0.0082},
        "hydration": 72,
        "default_weight": 500,
        "instructions": "Mix flour, water, and starter. Autolyse 30 min. Add salt/oil. 4 sets of folds. Proof in tray with plenty of olive oil. Dimple and bake at 230°C.",
        "tips": "Use your fingertips to create deep dimples just before baking to trap the oil."
    },
    "Baguette with Poolish": {
        "ingredients": {"Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2417, "Salt": 0.0089, "Dry Yeast": 0.0001},
        "hydration": 65,
        "default_weight": 300,
        "instructions": "Prepare poolish 12h ahead. Mix dough, rest 45 min. Shape into long baguettes. Score 5 times overlapping. Bake with heavy steam.",
        "tips": "Resting is key to being able to stretch the baguettes without them snapping back."
    },
    "Sourdough Ciabatta": {
        "ingredients": {"Wheat Flour": 0.5389, "Water": 0.4001, "Sourdough": 0.0500, "Salt": 0.0110},
        "hydration": 82,
        "default_weight": 300,
        "instructions": "Develop gluten fully. Perform coil folds every 30 min. Handle extremely gently during dividing to preserve large air pockets.",
        "tips": "Use plenty of flour on the bench during shaping – the dough is very sticky!"
    }
}

# --- SIDEBAR: SETTINGS & COSTING ---
st.sidebar.header("Recipe Settings")
selected_name = st.sidebar.selectbox("Select Bread", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of units (pcs)", min_value=1, value=1)
target_weight = st.sidebar.number_input("Weight per unit (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.header("Costing & Margin")
flour_price = st.sidebar.number_input("Flour Price (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price per unit (LKR)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
raw_material_cost = total_batch_kg * flour_price * 0.6  # Estimated ingredient overhead
total_sales = units * selling_price
total_profit = total_sales - raw_material_cost
margin_percent = (total_profit / total_sales) * 100 if total_sales > 0 else 0

# Sidebar Cost Summary
st.sidebar.info(f"""
**Financial Summary:**
* Total Cost: {raw_material_cost:.0f} LKR
* Total Sales: {total_sales:.0f} LKR
* **Margin: {margin_percent:.1f}%**
""")

# --- MAIN DISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Ingredients & Percentages", "Baking Instructions"])
    
    with tab1:
        st.write("### Production Sheet")
        # Table Header
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
            r3.write(f"{ratio*100:.1f}%")
            
        st.divider()
        st.metric("Total Batch Weight", f"{total_batch_kg:.2f} kg")

    with tab2:
        st.write("### Step-by-Step Guide")
        st.write(recipe["instructions"])

with col_right:
    st.subheader("Baker's Stats")
    st.metric("Hydration", f"{recipe['hydration']}%")
    
    st.divider()
    st.subheader("Pro Baking Tips")
    st.success(recipe["tips"])
    
    # Adding a visual guide for the Artisan Levain scoring
    if selected_name == "Artisan Levain French Sourdough":
        st.write("#### Scoring Technique")
        st.write("Hold the blade at a 45-degree angle to get that perfect 'ear' and expansion.")

st.caption("Monde Bakery Digital Handbook - Built for professional precision.")
