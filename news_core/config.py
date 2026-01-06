import os

# --- RUTAS ---
CARPETA_PERFIL = os.path.join(os.getcwd(), "perfil_forex_v1")
ARCHIVO_SALIDA = "market_events.json"

# --- URLs (HOY Y MAÑANA) ---
URLS_OBJETIVO = [
    "https://www.forexfactory.com/calendar?day=today",
    "https://www.forexfactory.com/calendar?day=tomorrow"
]

# --- SELECTORES (CSS) ---
SELECTOR_TABLA = "table.calendar__table"
SELECTOR_VERIFY_HUMAN = "text=Verify you are human"
SELECTOR_IMPACTO = ".calendar__impact span" 
SELECTOR_EVENTO = ".calendar__event-title"
SELECTOR_CURRENCY = ".calendar__currency"
SELECTOR_TIME = ".calendar__time"
SELECTOR_ACTUAL = ".calendar__actual"
SELECTOR_FORECAST = ".calendar__forecast"
SELECTOR_PREVIOUS = ".calendar__previous"