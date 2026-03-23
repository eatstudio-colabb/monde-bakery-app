import streamlit as st

st.set_page_config(page_title="Monde Bakery Pro", layout="wide")

st.title("Monde Bakery - Recipe Master Pro")

# --- DATA: RECIPES ---
recipes = {
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Bread Flour": 0.5389, 
            "Sourdough Starter": 0.1796, 
            "Water": 0.2695, 
            "Salt": 0.0120
        },
        "hydration": 80,  # Justerad för Ciabatta-stil baserat på mjöl/vatten-förhållandet
        "default_weight": 300,
        "instructions": """
        1. **Autolyse & Mixing**: Mix the flour and water first. Let it rest for **40 minutes**. This ensures the flour is fully hydrated before the salt begins its tightening effect. After the rest, add the sourdough starter and salt. Knead the dough for **10 minutes**.
        
        2. **Stretch and Fold**: Use the **Stretch and Fold** method to build strength without aggressive kneading. Perform **3–4 sets** of folds during the first 2 hours of bulk fermentation, spaced 30 minutes apart. This builds a strong gluten network to hold the gases.
        
        3. **Bulk Fermentation**: Keep the dough at a stable **24–26°C (75–78°F)**. Use the **"Poke Test"**: Look for a 30-50% increase in volume and a "jiggly" surface. Due to the starter percentage, this usually takes 3–4 hours.
        
        4. **Cold Proofing (Recommended)**: For best results and easier handling, proof the dough in the fridge for **12–14 hours**. This slow proof makes it much easier to cut and handle the slack Ciabatta dough.
        
        5. **Maximize Oven Spring**: 
           - **Preheat**: Get your oven and baking stone to **250°C (480°F)**.
           - **Baking**: Bake at **245°C** for 25–30 minutes.
           - **Steam**: Inject **15 seconds of steam** at the very start to keep the crust supple and allow for maximum expansion.
        """,
        "tips": "Handle the dough very gently after the cold proof to preserve the large air bubbles characteristic of a great Ciabatta."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Bread Flour": 0.3971, "Rye Flour": 0.0394, "Sourdough Starter": 0.1765, 
            "Water": 0.3088, "Salt": 0.0132, "Walnuts": 0.0650
        },
        "hydration": 70,
        "default_weight": 800,
        "instructions": "Autolyse 40 min, add starter/salt, knead 10 min. 4 sets of folds. Cold proof 12-14h. Bake at 245°C with 15s steam.",
        "tips": "Add walnuts during the second fold."
    }
}

# --- SIDEBAR: SETTINGS & CALCULATIONS ---
st.sidebar.header("Settings")
selected_name = st.sidebar.selectbox("Select Bread Type", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Number of Loaves/Pieces", min_value=1, value=20)
target_weight = st.sidebar.number_input("Weight per Piece (g)", value=recipe["default_weight"])

st.sidebar.divider()
st.sidebar.header("Economics & Profit")
raw_cost_per_kg = st.sidebar.number_input("Ingredient Cost (LKR/kg)", value=224.0)
selling_price = st.sidebar.number_input("Selling Price (LKR/pc)", value=900.0)

# --- CALCULATIONS ---
total_batch_kg = (units * target_weight) / 1000
total_cost = total_batch_kg * raw_cost_per_kg * 1.25 # Includes 25% overhead
total_revenue = units * selling_price
total_profit = total_revenue - total_cost
margin_pct = (total_profit / total_revenue) * 100 if total_revenue > 0 else 0

# Sidebar Summary
st.sidebar.subheader("Financial Overview")
st.sidebar.metric("Calculated Margin", f"{margin_pct:.1f}%")
st.sidebar.write(f"**Total Revenue:** {total_revenue:,.0f} LKR")
st.sidebar.write(f"**Total Cost:** {total_cost:,.0f} LKR")
st.sidebar.write(f"**Net Profit:** {total_profit:,.0f} LKR")

# --- MAIN DISPLAY ---
st.header(f"🍞 {selected_name}")

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2 = st.tabs(["Production Sheet", "Bakery Instructions"])
    
    with tab1:
        st.write("### Ingredients")
        h1, h2, h3 = st.columns([3, 2, 2])
        h1.write("**Ingredient**")
        h2.write("**Weight**")
        h3.write("**Percentage**")
        
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
        st.write("### Professional Guide")
        st.write(recipe["instructions"])

with col_right:
    st.subheader("Technical Specifications")
    st.metric("Hydration", f"{recipe['hydration']}%")
    st.metric("Baking Temperature", "245°C")
    st.metric("Initial Steam", "15 sec")
    
    st.divider()
    st.subheader("Baker's Tips")
    st.success(recipe["tips"])
    
    st.info("💡 **Happy baking—you’re in for a rewarding bake!**")

st.caption("Monde Bakery Digital Handbook | Precision Management")
