# =========================================================
# CALCULADORA WEB DE PROTEINA EQUIVALENTEpip install streamlit
# =========================================================

# =========================================================
# INSTALACION AUTOMATICA
# =========================================================

import subprocess
import sys

def instalar(paquete):
    subprocess.check_call(
        [sys.executable, "-m", "pip", "install", paquete]
    )

try:
    import streamlit as st
except ImportError:
    print("Instalando Streamlit...")
    instalar("streamlit")
    import streamlit as st

# =========================================================
# CONFIGURACION PAGINA
# =========================================================

st.set_page_config(
    page_title="Calculadora de Proteína",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================================================
# ESTILOS CSS
# =========================================================

st.markdown("""
<style>

/* Fondo general */
.stApp {
    background: linear-gradient(
        135deg,
        #0f172a,
        #111827,
        #1e293b
    );
    color: white;
}

/* Titulo principal */
.titulo {
    text-align: center;
    font-size: 55px;
    font-weight: bold;
    color: #4ADE80;
    margin-top: 20px;
}

/* Subtitulo */
.subtitulo {
    text-align: center;
    font-size: 22px;
    color: #CBD5E1;
    margin-bottom: 40px;
}

/* Tarjetas */
.card {
    background-color: rgba(255,255,255,0.05);
    padding: 30px;
    border-radius: 25px;
    box-shadow: 0px 4px 25px rgba(0,0,0,0.35);
    margin-top: 20px;
}

/* Resultado naranja */
.resultado1 {
    background: linear-gradient(
        135deg,
        #FF7043,
        #F4511E
    );

    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
}

/* Resultado azul */
.resultado2 {
    background: linear-gradient(
        135deg,
        #42A5F5,
        #1E88E5
    );

    padding: 25px;
    border-radius: 20px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
}

/* Boton */
.stButton>button {

    width: 100%;
    height: 65px;

    background: linear-gradient(
        135deg,
        #22C55E,
        #16A34A
    );

    color: white;
    font-size: 22px;
    font-weight: bold;

    border-radius: 18px;
    border: none;

    transition: 0.3s;
}

.stButton>button:hover {

    transform: scale(1.02);

    background: linear-gradient(
        135deg,
        #16A34A,
        #15803D
    );
}

/* Input */
.stNumberInput input {

    font-size: 28px !important;
    text-align: center;
}

/* Footer */
.footer {
    text-align: center;
    color: #94A3B8;
    margin-top: 40px;
    font-size: 16px;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# TITULO
# =========================================================

st.markdown(
    """
    <div class='titulo'>
    🌱 Calculadora de Proteína Equivalente
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class='subtitulo'>
    Convierte proteína animal en proteína vegetal
    usando lentejas germinadas y no germinadas
    </div>
    """,
    unsafe_allow_html=True
)

# =========================================================
# COLUMNAS
# =========================================================

col1, col2 = st.columns([1, 1])

# =========================================================
# COLUMNA IZQUIERDA
# =========================================================

with col1:

    st.markdown(
        """
        <div class='card'>
        <h2>🥩 Proteína Animal</h2>
        <p>
        Ingrese la cantidad de proteína animal
        consumida en gramos.
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    proteina_animal = st.number_input(
        "",
        min_value=0.0,
        step=1.0,
        placeholder="Ejemplo: 150"
    )

    st.write("")

    calcular = st.button(
        "CALCULAR EQUIVALENCIA"
    )

    st.write("")

    st.info(
        "💡 Las lentejas germinadas poseen "
        "mayor digestibilidad y mejor "
        "aprovechamiento proteico."
    )

# =========================================================
# VALORES NUTRICIONALES
# =========================================================

proteina_lenteja_no_germinada = 9
proteina_lenteja_germinada = 13

# =========================================================
# COLUMNA DERECHA
# =========================================================

with col2:

    st.markdown(
        """
        <div class='card'>
        <h2>📊 Resultados</h2>
        <p>
        Equivalencia vegetal requerida
        </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    if calcular:

        if proteina_animal <= 0:

            st.error(
                "Ingrese una cantidad válida"
            )

        else:

            # =============================================
            # CALCULOS
            # =============================================

            porcion_no_germinada = (
                proteina_animal /
                proteina_lenteja_no_germinada
            ) * 100

            porcion_germinada = (
                proteina_animal /
                proteina_lenteja_germinada
            ) * 100

            st.write("")

            # =============================================
            # RESULTADO 1
            # =============================================

            st.markdown(
                f"""
                <div class='resultado1'>
                🟠 Lenteja NO germinada<br><br>
                {porcion_no_germinada:.2f} g
                </div>
                """,
                unsafe_allow_html=True
            )

            st.write("")

            # =============================================
            # RESULTADO 2
            # =============================================

            st.markdown(
                f"""
                <div class='resultado2'>
                🔵 Lenteja germinada<br><br>
                {porcion_germinada:.2f} g
                </div>
                """,
                unsafe_allow_html=True
            )

# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class='footer'>
    Alimentación consciente • Nutrición vegetal • Ciencia nutricional
    </div>
    """,
    unsafe_allow_html=True
)
