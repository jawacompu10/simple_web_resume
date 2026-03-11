import pytest
from playwright.sync_api import Page, expect

def test_edit_social_links_preview(page: Page, server: str):
    page.goto(server)
    
    # Create new profile
    page.get_by_text("Create New Profile").click()
    
    # Fill in social links
    page.get_by_label("LinkedIn URL").fill("https://linkedin.com/in/testuser")
    page.get_by_label("GitHub URL").fill("https://github.com/testuser")
    page.get_by_label("Website URL (Optional)").fill("https://testuser.me")
    
    # Check preview
    preview = page.locator("#resume-preview")
    expect(preview.locator("#linkedin")).to_have_attribute("href", "https://linkedin.com/in/testuser")
    expect(preview.locator("#github")).to_have_attribute("href", "https://github.com/testuser")
    expect(preview.locator("#website")).to_have_attribute("href", "https://testuser.me")
    expect(preview.locator("#website-container")).to_be_visible()

def test_website_optional_hides_when_empty(page: Page, server: str):
    page.goto(server)
    
    # Create new profile
    page.get_by_text("Create New Profile").click()
    
    # Website should be hidden initially
    preview = page.locator("#resume-preview")
    expect(preview.locator("#website-container")).not_to_be_visible()
    
    # Fill it
    page.get_by_label("Website URL (Optional)").fill("https://testuser.me")
    expect(preview.locator("#website-container")).to_be_visible()
    
    # Clear it
    page.get_by_label("Website URL (Optional)").fill("")
    expect(preview.locator("#website-container")).not_to_be_visible()
