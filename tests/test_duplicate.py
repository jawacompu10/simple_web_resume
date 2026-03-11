import pytest
from playwright.sync_api import Page, expect

def test_duplicate_profile(page: Page, server: str, import_profile):
    page.goto(server)
    
    # Import a profile first
    import_profile()
    expect(page.get_by_text("Jawahar Vignesh")).to_be_visible()
    
    # Click Copy
    page.get_by_title("Duplicate Profile").click()
    
    # Check if duplicate is present
    expect(page.get_by_text("Jawahar Vignesh (Copy)")).to_be_visible()
    
    # Check that original is still there
    expect(page.get_by_text("Jawahar Vignesh", exact=True)).to_be_visible()
