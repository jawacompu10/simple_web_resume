from playwright.sync_api import Page, expect


def test_autosave_persists_on_refresh(page: Page, server: str):
    page.goto(server)

    # Create new profile
    page.get_by_text("Create New Profile").click()

    # Wait for form
    page.wait_for_selector("#form-name")

    # Fill in some data
    page.locator("#form-name").fill("Autosave Tester")
    page.get_by_label("Title").fill("Persistence Engineer")

    # Wait for autosave to trigger (debounce is 2s now)
    expect(page.get_by_text("AUTOSAVED")).to_be_visible(timeout=5000)

    # Refresh the page
    page.reload()

    # Wait for form to re-render from DB
    page.wait_for_selector("#form-name")

    # Check if data persisted
    expect(page.locator("#form-name")).to_have_value("Autosave Tester")
    expect(page.get_by_label("Title")).to_have_value("Persistence Engineer")


def test_autosave_toggle_disables_saving(page: Page, server: str):
    page.goto(server)
    page.get_by_text("Create New Profile").click()
    page.wait_for_selector("#form-name")

    # 1. Disable Autosave
    page.get_by_label("Autosave").click()
    expect(page.get_by_text("DISABLED")).to_be_visible()

    # 2. Type something
    page.locator("#form-name").fill("Manual Save Only")

    # 3. Wait a bit - should NOT see "AUTOSAVED"
    page.wait_for_timeout(3000)
    expect(page.get_by_text("AUTOSAVED")).not_to_be_visible()

    # 4. Refresh - data should be lost (or at least not updated to the new name)
    page.reload()
    page.wait_for_selector("#form-name")
    expect(page.locator("#form-name")).not_to_have_value("Manual Save Only")


def test_autosave_toggle_persistence(page: Page, server: str):
    page.goto(server)
    page.get_by_text("Create New Profile").click()
    page.wait_for_selector("#form-name")

    # Disable it
    page.get_by_label("Autosave").click()
    expect(page.get_by_text("DISABLED")).to_be_visible()

    # Refresh
    page.reload()
    page.wait_for_selector("#form-name")

    # Should still be disabled
    expect(page.get_by_text("DISABLED")).to_be_visible()
    expect(page.get_by_label("Autosave")).not_to_be_checked()
