import pytest
from playwright.sync_api import Page, expect

def test_edit_education_preview(page: Page, server: str):
    page.goto(server)
    
    # Create new profile
    page.get_by_text("Create New Profile").click()
    
    # Click Add Education
    page.get_by_text("Add Education").click()
    
    # Wait for the input to appear
    page.wait_for_selector('input[name="education[0][degree]"]')
    
    # Fill in education
    page.locator('input[name="education[0][degree]"]').fill("Master of Science")
    page.locator('input[name="education[0][university]"]').fill("Stanford University")
    page.locator('input[name="education[0][years]"]').fill("2018 - 2020")
    
    # Check preview
    preview = page.locator("#resume-preview")
    expect(preview.locator("#education-list")).to_contain_text("Master of Science")
    expect(preview.locator("#education-list")).to_contain_text("Stanford University")
    expect(preview.locator("#education-list")).to_contain_text("2018 - 2020")

def test_remove_education(page: Page, server: str):
    page.goto(server)
    
    # Create new profile
    page.get_by_text("Create New Profile").click()
    
    # Add education
    page.get_by_text("Add Education").click()
    page.wait_for_selector('input[name="education[0][degree]"]')
    page.locator('input[name="education[0][degree]"]').fill("Degree to remove")
    
    preview = page.locator("#resume-preview")
    expect(preview.locator("#education-list")).to_contain_text("Degree to remove")
    
    # Remove it
    page.locator(".remove-edu-btn").click()
    
    # Check it's gone from preview
    expect(preview.locator("#education-list")).not_to_contain_text("Degree to remove")
