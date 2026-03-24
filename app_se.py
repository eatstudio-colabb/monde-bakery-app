import streamlit as st

st.set_page_config(page_title="Monde Bakery Receptmaster", layout="wide")

# --- ANPASSAD CSS ---
st.markdown("""
    <style>
    h1 { 
        font-weight: 800 !important; 
        color: #FF4B4B !important;
        letter-spacing: -0.5px; 
    }
    
    div[data-testid="stSidebar"] div[data-testid="stExpander"] {
        border: 2px solid #0066CC;
        border-radius: 10px;
        background-color: #0066CC;
    }
    
    div[data-testid="stSidebar"] .st-emotion-cache-p4mowd {
        color: white !important;
        font-weight: 600 !important;
        text-transform: uppercase;
    }
    
    div[data-testid="stSidebar"] [data-testid="stExpanderDetails"] {
        background-color: white;
        color: black;
        border-radius: 0 0 8px 8px;
        padding: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Monde Bakery - Professionell Receptmaster")

# --- RECEPTDATABAS ---
recipes = {
    "Svenska Kanelbullar": {
        "ingredients": {
            "Deg: Vetemjöl": 0.3350, "Deg: Mjölk": 0.2577, "Deg: Surdeg": 0.1289,
            "Deg: Kallt smör (sist)": 0.0805, "Deg: Socker": 0.0548, "Deg: Kardemumma": 0.0064,
            "Deg: Salt": 0.0045, "Fyllning: Smör": 0.0967, "Fyllning: Socker": 0.0290, "Fyllning: Kanel": 0.0064
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Äggstrykning & Pärlsocker",
        "instructions": """
        1. **Förberedelse & Autolys:** Blanda kall mjölk, nystött kardemumma, socker och vetemjöl. Kör maskinen på låg hastighet i ca 3 minuter. Låt vila i 30–60 minuter.
        2. **Blandning:** Tillsätt aktiv surdeg. Knåda i 8–10 minuter tills degen släpper från kanterna.
        3. **Fettemulsion:** Tillsätt salt och mata in **kallt tärnat smör** lite i taget under knådning (ca 5–8 min). Kör till godkänt fönstertest.
        4. **Bulk:** Vila 3–4 timmar. Gör en "stretch and fold" efter 60 minuter.
        5. **Formning:** Kavla, bred på fyllning, gör knutar. Kalljäs i kyl 12–14h.
        6. **Bakning:** Pensla med ägg och pärlsocker. Baka till innertemp 92–94°C.
        """,
        "pro_tips": "Att tillsätta smöret kallt och sist ger en betydligt luftigare bulle."
    },
    "Focaccia med Surdeg": {
        "ingredients": {
            "Vetemjöl Special": 0.4655, "Vatten": 0.3292, "Surdegsgrund": 0.1587, 
            "Salt": 0.0132, "Olivolja": 0.0333, "Torrjäst": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Olivolja & Rosmarin",
        "instructions": """
        1. **Mix:** Blanda mjöl, vatten, surdeg och jäst. Vila 20 min.
        2. **Knådning:** Tillsätt salt och hälften av oljan. Knåda till elastisk deg.
        3. **Bulk:** Utför 4 set "Coil Folds" var 30:e minut.
        4. **Alternativ Jäsning:** Det går också utmärkt att kalljäsa degen 12–14 timmar direkt i bulkbehållaren i kylen och därefter placera ut degen på ett mjölat bord för hantering.
        5. **Plåt:** Olja en plåt rikligt, lägg i degen och sträck försiktigt.
        6. **Kalljäsning:** 12–18 timmar i kyl (om steg 4 hoppades över).
        7. **Dimpling:** Ta ut degen 2 timmar före bakning. Ringla över generöst med högkvalitativ olivolja och tryck djupa hål med fingertopparna ända ner till plåten så att oljan fyller groparna.
        8. **Bakning:** Toppa med rosmarin och flingsalt. Baka till gyllene.
        """,
        "pro_tips": "Tryck hålen ordentligt så att oljan kapslas in, det ger de karaktäristiska saftiga groparna."
    },
    "Surdegsbröd med Valnötter": {
        "ingredients": {
            "Vetemjöl Special": 0.3971, "Rågmjöl": 0.0394, "Surdegsgrund": 0.1765, 
            "Vatten": 0.3088, "Salt": 0.0132, "Valnötter": 0.0650, "Torrjäst": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "30-35 min", "finish": "15s Ånga",
        "instructions": """
        1. **Rostning:** Rosta valnötter i 180°C i 8 min. Låt svalna.
        2. **Autolys:** Mjöl och vatten i 60 min.
        3. **Mix:** Tillsätt surdeg, jäst och salt. Knåda 8–10 min.
        4. **Vikning:** Vid första "Stretch & Fold", vik in valnötterna.
        5. **Formning:** Totalt 3 vikningar. Forma spänstigt och lägg i jäskorg.
        6. **Kalljäsning:** 12–14 timmar i kyl.
        7. **Bakning:** Snitta och baka med mycket ånga de första 10 minuterna.
        """,
        "pro_tips": "Rostade valnötter ger hela inkråmet en nötig doft."
    },
    "Monde Multi Grain": {
        "ingredients": {
            "Vetemjöl Special": 0.2947, "Fullkornsvete": 0.0810, "Rågmjöl": 0.0357,
            "Vatten": 0.3051, "Surdegsgrund": 0.1620, "Salt": 0.0162, "Fröblandning": 0.1052
        },
        "hydration": 72, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "Ånga",
        "instructions": """
        1. **Skållning:** Blötlägg frön i kokande vatten i 1h. Sila noga.
        2. **Deg:** Blanda mjöl/vatten. Autolys 45 min.
        3. **Mix:** Tillsätt surdeg och salt. Knåda 10 min. Vik in fröna på låg fart.
        4. **Bulk:** 4 timmar med vikningar var 45:e min.
        5. **Kalljäsning:** Forma och kyl i 12–16 timmar.
        6. **Bakning:** Baka direkt från kyl med mycket ånga. Innertemp 98°C.
        """,
        "pro_tips": "Skållningen ser till att fröna inte stjäl fukt från degen."
    },
    "Artisan Fullkornsvete": {
        "ingredients": {
            "Fullkornsvete": 0.3500, "Vetemjöl Special": 0.1000, "Vatten": 0.3500, 
            "Surdegsgrund": 0.1800, "Salt": 0.0120, "Honung/Malt": 0.0080
        },
        "hydration": 80, "default_weight": 850, "bake_temp": "240°C", "bake_time": "40 min", "finish": "Mjölad yta",
        "instructions": """
        1. **Autolys:** Mjöl, vatten och honung i 2–3 timmar (viktigt för kliet).
        2. **Blandning:** Tillsätt surdeg och salt. Knåda 12 min.
        3. **Struktur:** Vik var 30:e minut (totalt 4 gånger).
        4. **Formning:** Forma batard med hög spänning.
        5. **Kalljäsning:** 15 timmar i kyl.
        6. **Bakning:** Snitta djupt. Baka tills skorpan är djupt mörkbrun.
        """,
        "pro_tips": "Honung hjälper jästen och ger fullkornet en fin färg."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Vetemjöl Special": 0.4500, "Vatten": 0.3150, "Surdegsgrund": 0.1350, 
            "Salt": 0.0090, "Torrjäst": 0.0001
        },
        "hydration": 70, "default_weight": 850, "bake_temp": "250°C", "bake_time": "35-40 min", "finish": "Ånga",
        "instructions": """
        1. **Autolys:** Mjöl, vatten och surdeg i 60 min.
        2. **Mix:** Knåda in salt och jäst till silkeslen deg.
        3. **Bulk:** 3 timmar med 3 set vikningar.
        4. **Bench rest:** Forma bollar, vila på bänk 20 min.
        5. **Shape:** Forma till batarder. Kalljäs 12 timmar.
        6. **Baka:** Snitta 45°. Baka med kraftig ånga.
        """,
        "pro_tips": "Bench rest gör formningen mycket enklare."
    },
    "Surdegs-Ciabatta": {
        "ingredients": {
            "Vetemjöl Special": 0.5389, "Surdegsgrund": 0.1796, "Vatten": 0.2695, "Salt": 0.0120, "Torrjäst": 0.0001
        },
        "hydration": 82, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25 min", "finish": "Mjölad yta",
        "instructions": """
        1. **Knådning:** Knåda länge (15 min) tills degen släpper från bunken trots hög vätska.
        2. **Struktur:** Vik degen (Coil Fold) var 30:e min 4 gånger i en oljad låda.
        3. **Dela:** Stjälp upp på mjölat bord. Skär försiktigt ut rektanglar.
        4. **Jäs:** Vila 45 min under duk.
        5. **Baka:** Skjut in i het ugn. Ingen snittning.
        """,
        "pro_tips": "Tryck aldrig ut luften ur en ciabatta-deg."
    },
    "Baguette med Poolish": {
        "ingredients": {
            "Vetemjöl": 0.4834, "Vatten": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Torrjäst": 0.0001
        },
        "hydration": 68, "default_weight": 350, "bake_temp": "245°C", "bake_time": "22 min", "finish": "Kraftig Ånga",
        "instructions": """
        1. **Poolish:** Blanda hälften av mjöl/vatten/jäst 12 timmar innan.
        2. **Mix:** Knåda ihop allt i 10 min. Vila 90 min.
        3. **Shape:** Dela 350g bitar. Rulla cylindrar. Vila 15 min. Rulla ut till baguetter.
        4. **Couché:** Jäs i linneduk 60–90 min.
        5. **Baka:** Snitta 5 omlott-snitt. Baka med max ånga.
        """,
        "pro_tips": "Snitten ska ligga nästan parallellt med baguetten."
    }
}

# --- SIDOMENY ---
st.sidebar.header("Produktionskalkylator")
selected_name = st.sidebar.selectbox("Välj Recept", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Antal Enheter", min_value=1, value=24)
target_weight = st.sidebar.number_input("Målvikt per styck (g)", value=recipe["default_weight"])

st.sidebar.divider()

# EKONOMI (ENBART SEK)
st.sidebar.header("Ekonomi (SEK)")
flour_price_sek = st.sidebar.number_input("Pris mjöl (kr/kg)", value=12.50)
selling_price_sek = st.sidebar.number_input("Försäljningspris (kr/st)", value=45.0)

# SURDEGSGUIDE
with st.sidebar.expander("📖 SURDEGSGUIDE"):
    st.markdown("Mata 1:1:1. Förvara i kyl. Mata 4-6h innan bak.")

# --- BERÄKNINGAR ---
total_dough_kg = (units * target_weight) / 1000
cost_sek = (total_dough_kg * flour_price_sek) * 1.25 # Inkl. 25% overhead
revenue_sek = units * selling_price_sek
profit_sek = revenue_sek - cost_sek

# --- HUVUDDISPLAY ---
st.header(selected_name)

col_left, col_right = st.columns([3, 2])

with col_left:
    tab1, tab2, tab3 = st.tabs(["Produktionsblad", "Process", "Bagar-tips"])
    
    with tab1:
        st.subheader("Ingredienser & Vikt")
        st.write(f"Batch: {units} st x {target_weight}g | **Hydrering: {recipe['hydration']}%**")
        st.markdown("---")
        
        for ing, ratio in recipe["ingredients"].items():
            ing_weight = total_dough_kg * ratio
            unit = "kg" if ing_weight >= 1 else "g"
            val = ing_weight if unit == "kg" else ing_weight * 1000
            
            r1, r2, r3 = st.columns([3, 2, 1])
            r1.write(ing)
            r2.write(f"**{val:.2f} {unit}**")
            r3.write(f"{ratio*100:.1f}%")
        
        st.markdown("---")
        st.metric("Total Batchvikt", f"{total_dough_kg:.2f} kg")

    with tab2:
        st.subheader("Steg-för-steg Instruktioner")
        st.write(recipe["instructions"])
    with tab3:
        st.subheader("Professionella Tips")
        st.write(recipe["pro_tips"])

with col_right:
    st.subheader("Ekonomi")
    st.metric("Vinst (SEK)", f"{profit_sek:,.2f} kr")
    
    st.divider()
    st.write(f"**Total Kostnad:** {cost_sek:,.2f} kr")
    st.write(f"**Total Intäkt:** {revenue_sek:,.2f} kr")
    
    st.divider()
    st.info(f"Ugn: {recipe['bake_temp']} | Tid: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
