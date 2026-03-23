import streamlit as st

# Page settings
st.set_page_config(page_title="Monde Bakery Master", layout="wide")

st.title("Monde Bakery - Recipe Master")

# --- DATA: ALL RECIPES ---
# Mapping ratios and specific baking instructions for each type
recipes = {
    "Focaccia with Sourdough": {
        "ingredients": {
            "Wheat Flour": 0.4655, "Water": 0.3335, "Sourdough": 0.1817, 
            "Salt": 0.0111, "Olive Oil": 0.0082
        },
        "default_weight": 5002,
        "instructions": "1. Mix flour, water and sourdough. Rest 30 min. \n2. Add salt and oil. Fold every 30 min (4 times). \n3. Final proof in tray with plenty of olive oil."
    },
    "Artisan Levain French Sourdough": {
        "ingredients": {
            "Wheat Flour": 0.4965, "Water": 0.3308, "Sourdough": 0.1613, "Salt": 0.0114
        },
        "default_weight": 5000,
        "instructions": "1. Autolyse flour and water. \n2. Add levain and salt. \n3. Bulk ferment until 50% increase. Shape and cold proof overnight."
    },
    "Baguette with Poolish": {
        "ingredients": {
            "Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2417, "Salt": 0.0089, "Dry Yeast": 0.0001
        },
        "default_weight": 10000,
        "instructions": "1. Prepare Poolish 12h before. \n2. Mix final dough, rest 45 min. \n3. Shape into baguettes and bake with high steam."
    },
    "Multi Grain Sourdough": {
        "ingredients": {
            "Wheat Flour": 0.2946, "Whole Wheat": 0.0810, "Water": 0.4051, "Sourdough": 0.1539, "Seeds Mix": 0.0654
        },
        "default_weight": 1000,
        "instructions": "1. Soak seeds in water for 2h. \n2. Mix all ingredients. \n3. Longer fermentation due to whole grains."
    },
    "Sourdough Loaf with Walnuts": {
        "ingredients": {
            "Wheat Flour": 0.3971, "Rye Flour": 0.0393, "Water": 0.3090, "Sourdough": 0.1765, "Walnuts": 0.0662, "Salt": 0.0119
        },
        "default_weight": 11333,
        "instructions": "1. Toast walnuts lightly. \n2. Add walnuts during the final set of folds to avoid grey dough."
    },
    "Sourdough Ciabatta": {
        "ingredients": {
            "Wheat Flour": 0.5389, "Water": 0.4001, "Sourdough": 0.0500, "Salt": 0.0110
        },
        "default_weight": 300,
        "instructions": "1. Very high hydration dough. \n2. Use 'slap and fold' technique. \n3. Handle gently after bulk fermentation to keep air bubbles."
    },
    "Swedish Cinnamon Buns": {
        "ingredients": {
            "Wheat Flour": 0.3350, "Milk": 0.2000, "Butter": 0.0966, "Sugar": 0.0644, "Yeast": 0.0161, "Filling": 0.2879
        },
        "default_weight": 130,
        "instructions": "1. Cream butter and sugar for filling. \n2. Roll dough thin, apply filling. \n3. Bake until golden brown (approx 8-10 mins)."
    },
    "Whole Wheat Sourdough": {
        "ingredients": {
            "Whole Wheat": 0.3654, "Wheat Flour": 0.1500, "Water": 0.3500, "Sourdough": 0.1235, "Salt": 0.0111
        },
        "default_weight": 850,
        "instructions": "1. Autolyse whole wheat for 2 hours. \n2. Dough will be stiffer than white levain. \n3. Score deeply before baking."
    }
}

# --- SIDEBAR: SELECTION ---
st.sidebar.header("Select Recipe")
selected_name = st.sidebar.selectbox("Choose what to bake:", list(recipes.keys()))
recipe = recipes[selected_name]

st.sidebar.divider()
st.sidebar.header("Baking Settings")
antal = st.sidebar.number_input("Number of units", min_value=1, value=1)
vikt_per_st = st.sidebar.number_input("Weight per unit (grams)", min_value=1, value=recipe["default_weight"])
price_per_kg = st.sidebar.number_input("Flour Price (LKR/kg)", value=224.0)

# --- CALCULATIONS ---
total_weight_kg = (antal * vikt_per_st) / 1000

# --- MAIN DISPLAY ---
st.header(selected_name)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Recipe Ingredients")
    for name, ratio in recipe["ingredients"].items():
        weight = total_weight_kg * ratio
        unit = "kg" if weight >= 1 else "g"
        val = weight if unit == "kg" else weight * 1000
        st.write(f"**{name}:** {val:.2f} {unit}")

with col2:
    st.subheader("Baking Instructions")
    st.info(recipe["instructions"])

st.divider()

# --- ECONOMICS ---
st.subheader("Economics")
# Simple cost estimation (primarily flour based as per previous requests)
est_cost = total_weight_kg * price_per_kg * 0.5 # Estimated average cost factor
st.write(f"Estimated Total Ingredient Cost: **{est_cost:.0f} LKR**")
st.write(f"Total Dough Weight: **{total_weight_kg:.2f} kg**")

st.caption("Instructions and ratios are synchronized with Monde Bakery master sheets.")
