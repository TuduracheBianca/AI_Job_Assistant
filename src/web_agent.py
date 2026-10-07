def simulate_job_application(name, email, cover_letter):
    from playwright.sync_api import sync_playwright
    import time

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # launch chromium
        page = browser.new_page()
        page.goto("https://demoqa.com/text-box")
        page.locator("#userName").fill(name)
        page.locator("#userEmail").fill(email)
        page.locator("#currentAddress").fill(cover_letter)
        page.locator("#submit").click()
        time.sleep(5)