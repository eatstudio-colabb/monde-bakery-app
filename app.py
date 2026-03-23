import streamlit as st

# Page settings
st.set_page_config(page_title="Monde Bakery Master", layout="wide")

st.title("Monde Bakery - Recipe Master & Pro Guide")

# --- DATA: RECIPES, INSTRUCTIONS & TIPS ---
recipes = {
    "Focaccia with Sourdough": {
        "ingredients": {"Wheat Flour": 0.4655, "Water": 0.3335, "Sourdough": 0.1817, "Salt": 0.0111, "Olive Oil": 0.0082},
        "default_weight": 5002,
        "instructions": """
        1. **Initial Mix**: Combine flour, water, and sourdough starter. Mix until no dry flour remains. Let rest (autolyse) for 30-45 minutes.
        2. **Salt & Oil**: Add salt and a portion of the olive oil. Mix until the dough is smooth and starts to pull away from the bowl.
        3. **Bulk Fermentation**: Transfer to a greased tub. Perform 4 sets of 'stretch and folds' every 30 minutes. The dough should be bubbly and jiggly.
        4. **Panning**: Pour plenty of olive oil into a baking tray. Gently transfer the dough. Do not force it to the corners yet. Let rest 30 min, then gently stretch to fill the tray.
        5. **Final Proof**: Let rise until doubled in height and covered in large bubbles.
        6. **Dimpling**: Drizzle more oil, use your fingertips to create deep dimples. Bake at 230°C until golden and crisp.
        """,
        "tips": "Use a high-quality extra virgin olive oil for the best crust. If the dough resists stretching in the tray, give it 15 minutes to relax the gluten."
    },
    "Artisan Levain French Sourdough": {
        "ingredients": {"Wheat Flour": 0.4965, "Water": 0.3308, "Sourdough": 0.1613, "Salt": 0.0114},
        "default_weight": 800,
        "instructions": """
        1. **Autolyse**: Mix flour and water and let sit for 1-2 hours. This develops gluten naturally.
        2. **Mix**: Add sourdough starter and salt. Mix using the Rubaud method or a stand mixer until the dough is strong.
        3. **Bulk Ferment**: Keep at 25-26°C. Perform 3-4 folds. Total bulk time approx 4-6 hours until 50% growth.
        4. **Shaping**: Pre-shape into a ball. Rest 20 min. Final shape into a batard or boule.
        5. **Cold Proof**: Place in banneton and refrigerate for 12-18 hours.
        6. **Baking**: Score deeply. Bake in a preheated Dutch oven or with steam at 240°C.
        """,
        "tips": "For a 'wild' ear (crust opening), ensure your sourdough starter is at its peak (doubled or tripled) before mixing."
    },
    "Baguette with Poolish": {
        "ingredients": {"Wheat Flour": 0.4834, "Water": 0.2417, "Poolish": 0.2417, "Salt": 0.0089, "Dry Yeast": 0.0001},
        "default_weight": 350,
        "instructions": """
        1. **Poolish**: Mix equal parts flour and water with a tiny pinch of yeast 12 hours before. It should be bubbly and slightly sunken in the middle when ready.
        2. **Final Dough**: Mix Poolish with the rest of the ingredients. 
        3. **Bulk**: 2 hours with one fold at 60 mins.
        4. **Divide & Shape**: Divide into 350g pieces. Pre-shape into short logs. Rest 20 min. Final shape into long baguettes.
        5. **Proof**: Use a floured 'couche' (cloth) to support the shape. Proof for 45-60 min.
        6. **Bake**: Score with 3-5 overlapping cuts. Bake with high steam at 250°C.
        """,
        "tips": "Steam is critical for baguettes! Use a tray with lava stones or pour boiling water into a preheated tray when loading the oven."
    },
    "Multi Grain Sourdough": {
        "ingredients": {"Wheat Flour": 0.2946, "Whole Wheat": 0.0810, "Water": 0.4051, "Sourdough": 0.1539, "Seeds Mix": 0.0654},
        "default_weight": 1000,
        "instructions": """
        1. **Soaker**: Mix all seeds with a portion of the water 4 hours before. This prevents the seeds from sucking moisture out of the dough.
        2. **Mixing**: Mix flours, water, and starter. Add salt and the seed soaker during the final stage of mixing.
        3. **Bulk**: Perform folds gently to avoid tearing the gluten with the seeds.
        4. **Shape & Proof**: Shape tightly and coat the outside with extra seeds if desired. Cold proofing is recommended.
        """,
        "tips": "To get seeds to stick to the crust, roll the shaped loaf on a wet towel and then directly into a bowl of seeds before placing in the banneton."
    },
    "Sourdough Ciabatta": {
        "ingredients": {"Wheat Flour": 0.5389, "Water": 0.4001, "Sourdough": 0.0500, "Salt": 0.0110},
        "default_weight": 300,
        "instructions": """
        1. **Mixing**: This is a very high hydration dough (80%+). Mix until the dough is very strong and shiny.
        2. **Bulk**: Use a square tub. Perform 'coil folds' every 45 minutes. The dough should look like a giant pillow.
        3. **Dividing**: Dust the counter heavily with flour. Flip the dough out gently. Do NOT de-gas. Cut into rectangles.
        4. **Final Proof**: Rest on floured cloth for 45 min. 
        5. **Bake**: Carefully transfer to the oven. Bake at 240°C with steam.
        """,
        "tips": "Handle the dough as little as possible after bulk fermentation to preserve the large irregular 'holes' characteristic of Ciabatta."
    },
    "Swedish Cinnamon Buns": {
        "ingredients": {"Wheat Flour": 0.3350, "Milk": 0.2000, "Butter": 0.0966, "Sugar": 0.0644, "Yeast": 0.0161, "Filling": 0.2879},
        "default_weight": 130,
        "instructions": """
        1. **Dough**: Mix milk, yeast, sugar, and flour. Add room-temp butter in small cubes while mixing. Knead until the dough is silky and passes the windowpane test.
        2. **First Rise**: Let rise until doubled (approx 1-2 hours).
        3. **Filling**: Mix butter, sugar, and cinnamon into a spreadable paste.
        4. **Assembly**: Roll dough into a large rectangle. Spread filling. Fold and cut into strips. Twist into knots.
        5. **Proof**: Proof on trays until they feel light and airy (approx 45-60 min).
        6. **Bake**: Brush with egg wash and top with pearl sugar. Bake at 225°C for 8-10 mins.
        """,
        "tips": "Don't melt the butter! Using room-temperature butter gives a much better dough structure and fluffier buns."
    },
    "Sourdough with Walnuts": {
        "ingredients": {"Wheat Flour": 0.3971, "Rye": 0.0393, "Water": 0.3090, "Sourdough": 0.1765, "Walnuts": 0.0662, "Salt": 0.0119},
        "default_weight": 900,
        "instructions": """
        1. **Prep**: Toast walnuts at 180°C for 8 mins. Let cool completely.
        2. **Mix**: Mix flours, water, and starter. Autolyse 1h. Add salt.
        3. **Lamination**: During the first fold, spread the dough out and sprinkle the walnuts evenly. Fold the dough back up.
        4. **Bulk & Shape**: Follow standard sourdough procedure.
        """,
        "tips": "Toasted walnuts provide a much deeper flavor and prevent the dough from turning too purple/grey from the raw nut oils."
    }
}

# --- SIDEBAR ---
st.sidebar.header("Select Recipe")
selected_name = st.sidebar.selectbox("Bread Type", list(recipes.keys()))
recipe = recipes[selected_name]

st.sidebar.divider()
st.sidebar.header("Baking Volume")
units = st.sidebar.number_input("Number of units", min_value=1, value=1)
weight = st.sidebar.number_input("Weight per unit (g)", value=recipe["default_weight"])
price_flour = st.sidebar.number_input("Flour Price (LKR/kg)", value=224.0)

# --- CALCULATIONS ---
total_kg = (units * weight) / 1000

# --- MAIN UI ---
st.subheader(selected_name)

tab1, tab2 = st.tabs(["Calculation", "Baking Guide"])

with tab1:
    c1, c2 = st.columns(2)
    with c1:
        st.write("### Ingredients")
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_kg * ratio
            u = "kg" if ing_weight >= 1 else "g"
            v = ing_weight if u == "kg" else ing_weight * 1000
            st.write(f"{ing}: **{v:.2f} {u}**")
            
    with c2:
        st.write("### Economics")
        cost = total_kg * price_flour * 0.6 # rough estimate
        st.metric("Estimated Cost", f"{cost:.0f} LKR")
        st.write(f"Total Dough: **{total_kg:.2f} kg**")

with tab2:
    st.write("### Step-by-Step Instructions")
    st.write(recipe["instructions"])
    st.divider()
    st.write("### Pro Baking Tips")
    st.success(recipe["tips"])

st.divider()
st.caption("Monde Bakery Digital Handbook")
