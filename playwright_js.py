from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        "https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login",
        wait_until='networkidle'  # Ждем полной загрузки страницы
    )

    new_text_title = "DDD"
    page.evaluate(f"""
        const title = document.getElementById('authentication-ui-course-title-text');
        title.textContent = '{new_text_title}';
    """)
