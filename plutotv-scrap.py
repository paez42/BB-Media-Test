import asyncio
from playwright.async_api import async_playwright
import pandas as pd
import time

async def scrape_pluto_on_demand():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_viewport_size({"width": 1920, "height": 1080})
        await page.goto("https://pluto.tv/latam/on-demand")

        # Hacer scroll inicial para cargar contenido
        await page.evaluate('window.scrollTo(0, document.body.scrollHeight)')
        await page.wait_for_timeout(4000)
        print("Initial scroll complete.")

        # Buscar y hacer clic en el span con texto "Películas"
        peliculas_span = await page.query_selector('span:has-text("Películas")')
        if peliculas_span:
            await peliculas_span.click()
            print("Clicked on 'Películas'.")
            
            # Mover el ratón al centro de la página
            viewport = await page.evaluate('({ width: window.innerWidth, height: window.innerHeight })')
            center_x = viewport['width'] / 2
            center_y = viewport['height'] / 2
            await page.mouse.move(center_x, center_y)
            print("Mouse moved to center.")

            # Hacer scroll hacia abajo simulando el desplazamiento de la rueda del ratón
            for _ in range(4):  # Cambiar el número de iteraciones si es necesario
                await page.mouse.wheel(0, 100)  # Simula el scroll hacia abajo
                await page.wait_for_timeout(2000)  # Esperar un tiempo para que el contenido se cargue
            print("Scrolled down after clicking 'Películas'.")
        else:
            print("No se encontró el span con texto 'Películas'.")

        # Extraer datos de las secciones de Películas y Series
        data = []
        while True:
            sections = await page.query_selector_all('section')
            if len(sections) == 0:
                print("No sections found. Ending.")
                break

            for section in sections:
                category = await section.evaluate('el => el.querySelector("h2") ? el.querySelector("h2").innerText : ""')
                ul = await section.query_selector('ul.categoryList')
                if ul:
                    items = await ul.query_selector_all('li')
                    for item in items:
                        try:
                            link = await item.query_selector('a')
                            if link:
                                href = await link.get_attribute('href')
                                img_src = await link.query_selector('img').get_attribute('src')
                                title = await link.query_selector('img').get_attribute('alt')
                                data.append({
                                    'Title': title,
                                    'URL': href,
                                    'Image URL': img_src,
                                    'Category': category
                                })
                                print(f"Processed item: {title}")

                                # Volver a la lista de secciones
                                await page.go_back()
                                await page.wait_for_timeout(5000)
                            else:
                                print("No link found in item.")
                        except Exception as e:
                            print(f"Error processing item: {e}")

                    # Simular el scroll hacia abajo usando la rueda del ratón después de procesar todos los `li` en el `ul`
                    for _ in range(4):
                        await page.mouse.wheel(0, 100)
                        await page.wait_for_timeout(2000)
                    print("Scrolled down after processing section.")
                else:
                    print("No ul.categoryList found in section.")

        # Guardar los datos en un archivo CSV
        df = pd.DataFrame(data)
        df.to_csv('pluto_tv_data.csv', index=False)
        print("Data saved to pluto_tv_data.csv")

        await browser.close()

# Medir tiempo de ejecución
start_time = time.time()
asyncio.run(scrape_pluto_on_demand())
end_time = time.time()
print(f"Tiempo de ejecución: {end_time - start_time} segundos")
