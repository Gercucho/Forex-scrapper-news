import asyncio
import json
import time
from datetime import datetime, timedelta

# Importamos nuestros módulos especialistas
from news_core.config import URLS_OBJETIVO, ARCHIVO_SALIDA, SELECTOR_TABLA, SELECTOR_VERIFY_HUMAN
from news_core.browser import RobotNavegador
from news_core.extractor import extraer_noticias_rojas
from news_core.utils import escribir_humano

async def tarea_diaria():
    print(f"\n⏰ INICIANDO RONDA: {datetime.now()}")
    
    # 1. Iniciar Navegador
    bot = RobotNavegador()
    page = await bot.iniciar()
    
    todas_las_noticias = []

    try:
        # 2. Bucle por URLs (Hoy y Mañana)
        for i, url in enumerate(URLS_OBJETIVO):
            dia_label = "HOY" if "today" in url else "MAÑANA"
            print(f"\n🌍 Navegando a ({dia_label}): {url}")
            
            # Navegación
            await page.goto("about:blank")
            await asyncio.sleep(1)
            await page.goto(url, wait_until="domcontentloaded")
            
            # Anti-Cloudflare
            try:
                if await page.locator(SELECTOR_VERIFY_HUMAN).is_visible(timeout=5000):
                    print("🛑 Cloudflare detectado. Esperando...")
                    await page.wait_for_selector(SELECTOR_TABLA, timeout=60000)
                else:
                    await page.wait_for_selector(SELECTOR_TABLA, timeout=30000)
            except:
                print("⚠️ Tiempo agotado esperando tabla.")

            # Extracción
            if await page.locator(SELECTOR_TABLA).is_visible():
                rows = await page.query_selector_all("tr.calendar__row")
                
                # Calculamos fecha real para guardar en el JSON
                fecha_ref = (datetime.now() + timedelta(days=i)).strftime("%Y-%m-%d")
                
                noticias = await extraer_noticias_rojas(rows, fecha_ref)
                todas_las_noticias.extend(noticias)
            else:
                print("❌ No se encontró tabla.")

        # 3. Guardar Todo Junto
        with open(ARCHIVO_SALIDA, "w") as f:
            json.dump(todas_las_noticias, f, indent=4)
        print(f"\n💾 REPORTE FINAL: {len(todas_las_noticias)} noticias guardadas.")

    except Exception as e:
        print(f"❌ Error crítico: {e}")
    finally:
        await bot.cerrar()

async def sistema_24h():
    print("🛡️  SISTEMA DE NOTICIAS ACTIVO (Ciclo 24h)")
    
    while True:
        # Ejecutar la tarea
        await tarea_diaria()
        
        # Calcular tiempo para siguiente ejecución (o dormir 24h fijo)
        print("\n💤 Durmiendo 24 horas...")
        # Dormir 86400 segundos (24 horas)
        # Usamos asyncio.sleep para no bloquear si quisieras agregar más tareas
        await asyncio.sleep(86400) 

if __name__ == "__main__":
    try:
        asyncio.run(sistema_24h())
    except KeyboardInterrupt:
        print("\n👋 Sistema detenido manual.")