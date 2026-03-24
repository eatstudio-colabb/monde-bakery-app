import streamlit as st

st.set_page_config(page_title="Monde Bakery Receptmaster", layout="wide")

# --- ANPASSAD CSS (Rör ej tidigare design) ---
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

# --- KOMPLETT RECEPTDATABAS MED UTVECKLADE INSTRUKTIONER ---
recipes = {
    "Svenska Kanelbullar": {
        "ingredients": {
            "Deg: Vetemjöl": 0.3350, "Deg: Mjölk": 0.2577, "Deg: Surdeg": 0.1289,
            "Deg: Kallt smör (sist)": 0.0805, "Deg: Socker": 0.0548, "Deg: Kardemumma": 0.0064,
            "Deg: Salt": 0.0045, "Fyllning: Smör": 0.0967, "Fyllning: Socker": 0.0290, "Fyllning: Kanel": 0.0064
        },
        "hydration": 50, "default_weight": 129, "bake_temp": "175–200°C", "bake_time": "15–20 min", "finish": "Äggstrykning & Pärlsocker",
        "instructions": """
        1. **Förberedelse & Autolys:** Blanda kall mjölk, nystött kardemumma, socker och vetemjöl. Kör maskinen på låg hastighet i ca 3 minuter tills ingredienserna precis gått ihop. Låt vila (autolys) i 30–60 minuter för att bygga gluten naturligt.
        2. **Blandning:** Tillsätt den aktiva surdegsgrunden. Öka till medelhastighet och knåda i 8–10 minuter tills degen känns stark och börjar släppa från kanterna.
        3. **Fettemulsion:** Tillsätt saltet. Börja sedan mata in det **kalla tärnade smöret** lite i taget under knådning. Detta tar ca 5–8 minuter. Fortsätt tills degen är helt slät, glansig och klarar ett fönstertest (du kan dra ut degen tunt utan att den spricker).
        4. **Bulkjäsning:** Lägg degen i en lätt inoljad låda. Låt vila i rumstemperatur i ca 3–4 timmar. Gör en "stretch and fold" efter 60 minuter för att öka elasticiteten.
        5. **Kalljäsning & Formning:** Kavla ut degen till en rektangel, bred på fyllningen (vispat smör/socker/kanel). Gör ett treslag, skär remsor och snurra till knutar. Lägg på plåt och ställ i kyl över natten (12–14h).
        6. **Bakning:** Ta ut plåtarna och låt vila i rumstemp 45 min. Pensla med uppvispat ägg och strö över rikligt med pärlsocker. Baka till gyllenbruna (innertemp 92–94°C).
        """,
        "pro_tips": "Att tillsätta smöret kallt och sist förhindrar att fettet 'smörjer' glutenet för tidigt, vilket ger en betydligt luftigare bulle."
    },
    "Focaccia med Surdeg": {
        "ingredients": {
            "Vetemjöl Special": 0.4655, "Vatten": 0.3292, "Surdegsgrund": 0.1587, 
            "Salt": 0.0132, "Olivolja": 0.0333, "Torrjäst": 0.0001
        },
        "hydration": 75, "default_weight": 800, "bake_temp": "245°C", "bake_time": "25-30 min", "finish": "Saltlake & Rosmarin",
        "instructions": """
        1. **Degblandning:** Blanda mjöl, vatten, surdeg och jäst. Kör på låg hastighet i 5 minuter. Låt vila i 20 minuter.
        2. **Salt & Olja:** Tillsätt salt och hälften av olivoljan. Öka farten och knåda tills degen är elastisk men fortfarande mycket klibbig (ca 7–10 min).
        3. **Bulk & Vikning:** Låt degen vila i en inoljad plastlåda. Utför 4 set "Coil Folds" eller "Stretch & Folds" var 30:e minut. Detta ger brödet dess höjd.
        4. **Plåtförberedelse:** Olja en plåt rikligt med olivolja. Stjälp upp degen och vänd den en gång så den är täckt av olja. Sträck försiktigt degen mot kanterna utan att pressa ut luften.
        5. **Långjäsning:** Kalljäs i kylen i 12–18 timmar.
        6. **Dimpling:** Ta ut degen 2 timmar före bakning. Vispa ihop saltlaken (vatten/olja/salt) tills den emulgerar. Häll över degen. Använd fingertopparna för att trycka djupa kratrar ända ner till plåten.
        7. **Finish:** Toppa med rosmarinkvistar och flingsalt. Baka i het ugn tills botten är friterad och gyllene.
        """,
        "pro_tips": "Var inte rädd för saltlaken; vattnet i den skapar ånga som gör inkråmet extremt saftigt."
    },
    "Surdegsbröd med Valnötter": {
        "ingredients": {
            "Vetemjöl Special": 0.3971, "Rågmjöl": 0.0394, "Surdegsgrund": 0.1765, 
            "Vatten": 0.3088, "Salt": 0.0132, "Valnötter": 0.0650, "Torrjäst": 0.0001
        },
        "hydration": 70, "default_weight": 800, "bake_temp": "245°C", "bake_time": "30-35 min", "finish": "15s Ånga",
        "instructions": """
        1. **Rostning:** Rosta valnötterna i ugnen på 180°C i 8 minuter tills de doftar nötigt. Låt svalna helt innan de bryts i mindre bitar.
        2. **Autolys:** Blanda vetemjöl, rågmjöl och vatten. Låt stå i 60 minuter.
        3. **Mixning:** Tillsätt surdeg och jäst. Knåda på medelhastighet i ca 8 minuter. Tillsätt saltet mot slutet.
        4. **Inkorporering:** Under den första vikningen (efter 30 minuter), strö över valnötterna och vik in dem försiktigt i degen.
        5. **Formning:** Utför 3 vikningar till under 2 timmar. Forma sedan degen spänstigt till runda boules eller batarder. Lägg i mjölade jäskorgar.
        6. **Kalljäsning:** Jäs i kyl (4–6°C) i 12–14 timmar.
        7. **Bakning:** Snitta brödet längs med. Baka på baksten eller i gjutjärnsgryta. Spruta in rikligt med ånga under de första 10 minuterna för maximal volym.
        """,
        "pro_tips": "Rostade valnötter innehåller oljor som absorberas av degen och ger hela inkråmet en nötig doft."
    },
    "Monde Multi Grain": {
        "ingredients": {
            "Vetemjöl Special": 0.2947, "Fullkornsvete": 0.0810, "Rågmjöl": 0.0357,
            "Vatten": 0.3051, "Surdegsgrund": 0.1620, "Salt": 0.0162, "Fröblandning": 0.1052
        },
        "hydration": 72, "default_weight": 1000, "bake_temp": "245°C", "bake_time": "45 min", "finish": "Ånga",
        "instructions": """
        1. **Skållning:** Blötlägg fröblandningen i kokande vatten minst 1 timme före (eller kallt vatten över natten). Sila av noga innan de tillsätts degen.
        2. **Deg:** Blanda allt utom salt och fröer. Autolys i 45 min.
        3. **Mix:** Tillsätt salt och knåda i 10 min. När glutenet är starkt, sänk farten och tillsätt fröerna tills de är jämnt fördelade.
        4. **Jäsning:** 4 timmar bulkjäst i rumstemp med vikningar var 45:e minut.
        5. **Kalljäsning:** Forma och lägg i jäskorgar. Plasta in noga och kyl i 12–16 timmar.
        6. **Bakning:** Baka direkt från kylen. Skjut in i ugnen med mycket ånga. Sänk temp till 220°C efter halva tiden för att inte bränna fröerna på ytan.
        """,
        "pro_tips": "Ett fullkornsbröd kräver hög sluttemperatur (98°C) för att inte kännas degigt i mitten."
    },
    "Artisan Fullkornsvete": {
        "ingredients": {
            "Fullkornsvete": 0.3500, "Vetemjöl Special": 0.1000, "Vatten": 0.3500, 
            "Surdegsgrund": 0.1800, "Salt": 0.0120, "Honung/Malt": 0.0080
        },
        "hydration": 80, "default_weight": 850, "bake_temp": "240°C", "bake_time": "40 min", "finish": "Mjölad yta",
        "instructions": """
        1. **Förlängd Autolys:** Blanda fullkornsmjölet med vatten och honung. Låt stå i 2–3 timmar. Detta mjukar upp kliet och gör det lättare för glutenet att expandera.
        2. **Blandning:** Tillsätt surdegsgrund och vetemjöl special. Knåda på låg fart i 12 minuter. Addera saltet sista 2 minuterna.
        3. **Struktur:** Fullkorn degar är tunga. Vik degen var 30:e minut under de första 2 timmarna (totalt 4 gånger).
        4. **Formning:** Forma till batard med hög ytspänning. Var generös med rågmjöl i jäskorgen.
        5. **Kalljäsning:** 15 timmar i kylskåp för optimal smakutveckling och syra.
        6. **Baka:** Snitta med ett rakt, djupt snitt. Baka tills skorpan är djupt mörkbrun.
        """,
        "pro_tips": "Honung eller maltsirap hjälper jästen att jobba med de tunga fullkornen och ger en vacker färg."
    },
    "Artisan French Levain": {
        "ingredients": {
            "Vetemjöl Special": 0.4500, "Vatten": 0.3150, "Surdegsgrund": 0.1350, 
            "Salt": 0.0090, "Torrjäst": 0.0001
        },
        "hydration": 70, "default_weight": 850, "bake_temp": "250°C", "bake_time": "35-40 min", "finish": "Ånga",
        "instructions": """
        1. **Klassisk Mix:** Blanda mjöl, vatten och surdeg. Autolys i 60 minuter.
        2. **Mix:** Knåda in salt och torrjäst (för ökad stabilitet i bagerimiljö). Kör maskinen tills degen är silkeslen.
        3. **Långsam Bulk:** Låt jäsa i rumstemperatur i 3 timmar. Utför 3 set "Stretch & Fold".
        4. **Pre-shape:** Forma degen till runda bollar, låt vila på bänken i 20 minuter (bench rest) innan slutlig formning.
        5. **Shape:** Forma till spända batarder. Kalljäs 12 timmar.
        6. **Finish:** Snitta i 45 graders vinkel för att skapa ett 'öra'. Baka med mycket ånga de första 15 minuterna.
        """,
        "pro_tips": "Bench rest är nyckeln till att få brödet att hålla formen under snittningen."
    },
    "Surdegs-Ciabatta": {
        "ingredients": {
            "Vetemjöl Special": 0.5389, "Surdegsgrund": 0.1796, "Vatten": 0.2695, "Salt": 0.0120, "Torrjäst": 0.0001
        },
        "hydration": 82, "default_weight": 300, "bake_temp": "245°C", "bake_time": "25 min", "finish": "Mjölad yta",
        "instructions": """
        1. **High Hydration Mix:** Denna deg är extremt lös. Blanda allt och knåda länge (ca 15 min) tills degen släpper från botten av bunken och är väldigt elastisk.
        2. **Bulk:** Låt jäsa i en väl inoljad fyrkantig låda.
        3. **Struktur:** Utför "Coil Folds" var 30:e minut (totalt 4 gånger). Degen ska kännas som en luftfylld kudde efter 3 timmar.
        4. **Dela:** Stjälp försiktigt upp degen på ett kraftigt mjölat bord. Tryck inte ut luften! Använd en degskrapa för att skära ut rektanglar (tofflor).
        5. **Final Proof:** Låt jäsa på mjölat bakplåtspapper i 45 minuter under duk.
        6. **Baka:** Skjut in i ugnen. Ingen snittning behövs. Baka tills de känns lätta och ihåliga.
        """,
        "pro_tips": "Hanteringen är allt; rör degen så lite som möjligt efter jäsning för att bevara de stora hålen."
    },
    "Baguette med Poolish": {
        "ingredients": {
            "Vetemjöl": 0.4834, "Vatten": 0.2417, "Poolish": 0.2660, "Salt": 0.0088, "Torrjäst": 0.0001
        },
        "hydration": 68, "default_weight": 350, "bake_temp": "245°C", "bake_time": "22 min", "finish": "Kraftig Ånga",
        "instructions": """
        1. **Poolish:** Blanda hälften av mjölet/vattnet med en nypa jäst 12 timmar före bakning. Den ska bubbla ordentligt.
        2. **Slutlig Deg:** Blanda poolishen med resten av ingredienserna. Knåda i 9–10 minuter till en smidig deg.
        3. **Förjäsning:** Vila 90 minuter i rumstemp.
        4. **Formning:** Dela degen i bitar om 350g. Rulla försiktigt till korta cylindrar. Låt vila 15 min. Rulla sedan ut till långa baguetter med spetsiga ändar.
        5. **Couché:** Låt jäsa i en mjölad linneduk (couché) för att hålla formen i 60–90 minuter.
        6. **Baka:** Flytta till plåt, snitta 5 diagonala snitt som överlappar varandra. Baka med max ånga.
        """,
        "pro_tips": "Snitten ska vara nästan parallella med baguetten, inte tvärsöver, för att den ska expandera på längden."
    }
}

# --- SIDOMENY (Rör ej tidigare logik) ---
st.sidebar.header("Produktionskalkylator")
selected_name = st.sidebar.selectbox("Välj Recept", list(recipes.keys()))
recipe = recipes[selected_name]

units = st.sidebar.number_input("Antal Enheter", min_value=1, value=24)
target_weight = st.sidebar.number_input("Målvikt per styck (g)", value=recipe["default_weight"])

st.sidebar.divider()

# VALUTAINSTÄLLNINGAR
st.sidebar.header("Valuta & Ekonomi")
lkr_to_sek = st.sidebar.number_input("Växelkurs (100 LKR = X SEK)", value=3.50) / 100
flour_price_lkr = st.sidebar.number_input("Pris mjöl (LKR/kg)", value=224.0)
selling_price_lkr = st.sidebar.number_input("Försäljningspris (LKR/st)", value=900.0)

# SURDEGSGUIDE
with st.sidebar.expander("📖 SURDEGSGUIDE"):
    st.markdown("Mata 1:1:1. Förvara i kyl. Mata 4-6h innan bak.")

# --- BERÄKNINGAR ---
total_dough_kg = (units * target_weight) / 1000
cost_lkr = (total_dough_kg * flour_price_lkr) * 1.25
revenue_lkr = units * selling_price_lkr
profit_lkr = revenue_lkr - cost_lkr

cost_sek = cost_lkr * lkr_to_sek
profit_sek = profit_lkr * lkr_to_sek
revenue_sek = revenue_lkr * lkr_to_sek

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
    c1, c2 = st.columns(2)
    c1.metric("Vinst (LKR)", f"{profit_lkr:,.0f}")
    c2.metric("Vinst (SEK)", f"{profit_sek:,.0f}")
    
    st.divider()
    st.write(f"**Kostnad:** {cost_lkr:,.0f} LKR ({cost_sek:,.2f} SEK)")
    st.write(f"**Intäkt:** {revenue_lkr:,.0f} LKR ({revenue_sek:,.2f} SEK)")
    
    st.divider()
    st.info(f"Ugn: {recipe['bake_temp']} | Tid: {recipe['bake_time']}")
    st.info(f"Finish: {recipe['finish']}")

st.caption("Monde Bakery Digital Handbook | 2026")
