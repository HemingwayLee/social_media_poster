import asyncio
from playwright.async_api import Playwright, async_playwright, expect

async def search_automation():
    async with async_playwright() as playwright:
        browser = await playwright.chromium.launch(headless=False)
        
        page = await browser.new_page()

        print("Navigating to Google...")
        await page.goto("https://www.google.com")

        cookie_accept_button = page.locator('button:has-text("I agree")')
        if await cookie_accept_button.is_visible():
            print("Accepting cookie consent...")
            await cookie_accept_button.click()
            await page.wait_for_load_state("domcontentloaded") # or "networkidle"

        print("Locating search bar...")
        search_bar = page.locator("textarea[name='q']")
        
        await expect(search_bar).to_be_visible()
        await expect(search_bar).to_be_enabled()

        search_query = "Playwright automation example"
        print(f"Typing '{search_query}' into the search bar...")
        await search_bar.fill(search_query)

        print("Performing search by pressing Enter...")
        await search_bar.press("Enter")

        print("Waiting for search results to load...")
        await page.wait_for_load_state("networkidle")

        print(f"Search completed. Current URL: {page.url}")

        screenshot_path = "screenshot_results.png"
        await page.screenshot(path=screenshot_path)
        print(f"Screenshot saved to {screenshot_path}")

        print(f"Page title: {await page.title()}")

        await browser.close()
        print("Browser closed.")

if __name__ == "__main__":
    asyncio.run(search_automation())
