from playwright.sync_api import Page, expect


def test_storage_info_auto_shows_on_first_visit(page: Page, server: str):
    # Clear flag specifically for this test
    page.goto(server)
    page.evaluate("localStorage.removeItem('hasSeenStorageInfo')")
    page.reload()

    # Wait for the setTimeout (500ms) and check if modal is visible
    expect(page.get_by_text("About Local Storage")).to_be_visible(timeout=5000)

    # Refresh without dismissing - should still show
    page.reload()
    expect(page.get_by_text("About Local Storage")).to_be_visible(timeout=5000)

    # Dismiss modal
    page.get_by_text("Got it!").click()
    expect(page.get_by_text("About Local Storage")).not_to_be_visible()

    # Refresh after dismissing - should NOT show
    page.reload()
    page.wait_for_timeout(1000)
    expect(page.get_by_text("About Local Storage")).not_to_be_visible()
