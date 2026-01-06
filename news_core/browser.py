import os
from playwright.async_api import async_playwright
from .config import CARPETA_PERFIL

class RobotNavegador:
    def __init__(self):
        self.playwright = None
        self.context = None
        self.page = None

    def _limpiar_basura(self):
        """Borra archivos que causan el crash de Firefox."""
        files = ["lock", ".parentlock", "parent.lock", "sessionstore.jsonlz4"]
        for f in files:
            try:
                p = os.path.join(CARPETA_PERFIL, f)
                if os.path.exists(p): os.remove(p)
            except: pass

    async def iniciar(self):
        self._limpiar_basura()
        self.playwright = await async_playwright().start()
        
        self.context = await self.playwright.firefox.launch_persistent_context(
            user_data_dir=CARPETA_PERFIL,
            headless=False,
            viewport={"width": 1280, "height": 720},
            args=["--no-remote"],
            ignore_default_args=["--enable-automation"],
            java_script_enabled=True
        )
        
        # Ocultar que somos robot
        await self.context.add_init_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
        
        self.page = self.context.pages[0] if self.context.pages else await self.context.new_page()
        await self.page.bring_to_front()
        return self.page

    async def cerrar(self):
        if self.context: await self.context.close()
        if self.playwright: await self.playwright.stop()