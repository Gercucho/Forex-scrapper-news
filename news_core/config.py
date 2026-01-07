import os

# --- RUTAS ---
CARPETA_PERFIL = os.path.join(os.getcwd(), "perfil_forex_v1")
ARCHIVO_SALIDA = "market_events.json"

# --- URLs MULTI-MERCADO (HOY Y MAÑANA) ---
# El bot barrerá Forex, Metales, Energía y Crypto en una sola ronda.
URLS_OBJETIVO = [
    # --- FOREX (Divisas y Economía Global) ---
    "https://www.forexfactory.com/calendar?day=today",
    "https://www.forexfactory.com/calendar?day=tomorrow",
    
    # --- METALES (Oro, Plata - Vital para XAUUSD) ---
    "https://www.metalsmine.com/calendar?day=today",
    "https://www.metalsmine.com/calendar?day=tomorrow",
    
    # --- ENERGÍA (Petróleo, Gas - Vital para Rublo/CAD) ---
    "https://www.energyexch.com/calendar?day=today",
    "https://www.energyexch.com/calendar?day=tomorrow",

    # --- CRYPTO (Bitcoin, Blockchain) ---
    "https://www.cryptocraft.com/calendar?day=today",
    "https://www.cryptocraft.com/calendar?day=tomorrow"
]

# --- SELECTORES (Son idénticos en toda la red Fair Economy) ---
SELECTOR_TABLA = "table.calendar__table"
SELECTOR_VERIFY_HUMAN = "text=Verify you are human"
SELECTOR_IMPACTO = ".calendar__impact span" 
SELECTOR_EVENTO = ".calendar__event-title"
SELECTOR_CURRENCY = ".calendar__currency"
SELECTOR_TIME = ".calendar__time"
SELECTOR_ACTUAL = ".calendar__actual"
SELECTOR_FORECAST = ".calendar__forecast"
SELECTOR_PREVIOUS = ".calendar__previous"