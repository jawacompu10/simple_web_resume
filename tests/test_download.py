import pytest
from playwright.sync_api import Page, expect

def test_dashboard_download_buttons(page: Page, server: str, import_profile):
    page.goto(server)
    
    # Import a profile first
    import_profile()
    
    # Check if JSON and PDF buttons are present in the profile card
    expect(page.get_by_title("Download JSON")).to_be_visible()
    expect(page.get_by_title("Print to PDF")).to_be_visible()

def test_view_page_download_buttons(page: Page, server: str, import_profile):
    page.goto(server)
    
    # Import a profile first
    import_profile()
    
    # Click View
    page.get_by_title("View Resume").first.click()
    
    # Check if floating bar buttons are present
    expect(page.get_by_text("Download JSON")).to_be_visible()
    expect(page.get_by_text("Print / Save PDF")).to_be_visible()
    expect(page.get_by_text("Dashboard")).to_be_visible()
