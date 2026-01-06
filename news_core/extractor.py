from datetime import datetime
from .config import (
    SELECTOR_IMPACTO, SELECTOR_EVENTO, SELECTOR_CURRENCY, 
    SELECTOR_TIME, SELECTOR_ACTUAL, SELECTOR_FORECAST, SELECTOR_PREVIOUS
)

async def extraer_noticias_rojas(rows, fecha_referencia):
    """Recibe filas HTML y devuelve una lista de diccionarios limpios."""
    datos = []
    last_valid_time = "All Day"

    for row in rows:
        impact_el = await row.query_selector(SELECTOR_IMPACTO)
        clase_impacto = await impact_el.get_attribute("class") if impact_el else ""
        
        es_rojo = "impact-red" in clase_impacto or "High" in clase_impacto

        if es_rojo:
            event_el = await row.query_selector(SELECTOR_EVENTO)
            event_name = await event_el.inner_text() if event_el else "Evento"
            
            currency_el = await row.query_selector(SELECTOR_CURRENCY)
            currency = await currency_el.inner_text() if currency_el else ""
            
            time_el = await row.query_selector(SELECTOR_TIME)
            time_text = await time_el.inner_text() if time_el else ""

            # Extraer Forecast/Actual
            actual_el = await row.query_selector(SELECTOR_ACTUAL)
            actual = await actual_el.inner_text() if actual_el else ""
            
            forecast_el = await row.query_selector(SELECTOR_FORECAST)
            forecast = await forecast_el.inner_text() if forecast_el else ""
            
            previous_el = await row.query_selector(SELECTOR_PREVIOUS)
            previous = await previous_el.inner_text() if previous_el else ""

            if not time_text or time_text.strip() == "":
                time_text = last_valid_time
            else:
                last_valid_time = time_text

            datos.append({
                "date": fecha_referencia, # Le pasamos la fecha de la URL
                "time": time_text,
                "currency": currency,
                "impact": "HIGH",
                "event": event_name,
                "actual": actual.strip(),
                "forecast": forecast.strip(),
                "previous": previous.strip()
            })
            print(f"🔥 [{fecha_referencia}] {time_text} {currency} - {event_name}")
    
    return datos