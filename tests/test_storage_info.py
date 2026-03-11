import pytest
from playwright.sync_api import Page, expect

def test_storage_info_modal(page: Page, server: str):
    page.goto(server)
    
    # We want to test manual trigger, so first ensure it's not showing automatically
    # (The autouse fixture already dismissed it, so it should be hidden)
    expect(page.get_by_text("About Local Storage")).not_to_be_visible()

    # Check if question mark icon is present
    question_btn = page.get_by_title("What does this mean?")
    expect(question_btn).to_be_visible()
    
    # Click it
    question_btn.click()
    
    # Check modal content
    expect(page.get_by_text("About Local Storage")).to_be_visible()
    expect(page.get_by_text("Privacy: Your data stays with you")).to_be_visible()
    
    # Close it
    page.get_by_text("Got it!").click()
    
    # Should be hidden again
    expect(page.get_by_text("About Local Storage")).not_to_be_visible()
