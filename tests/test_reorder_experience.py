import re
from playwright.sync_api import Page, expect

def test_reorder_experience_items(page: Page, server: str):
    page.goto(server)
    page.get_by_text("Create New Profile").click()

    # Add 3 experience items
    for title in ["Experience One", "Experience Two", "Experience Three"]:
        page.get_by_text("Add Experience").click()
        # Find all inputs for title and fill the last one
        page.locator('input[placeholder="Job Title"]').last.fill(title)

    # Helper to get titles in order
    def get_titles():
        return [el.input_value() for el in page.locator('input[placeholder="Job Title"]').all()]

    # Initial order check
    assert get_titles() == ["Experience One", "Experience Two", "Experience Three"]
    
    # Check preview initial order
    preview = page.locator("#resume-preview")
    expect(preview).to_contain_text("Experience One")
    expect(preview).to_contain_text("Experience Two")
    expect(preview).to_contain_text("Experience Three")

    # Check button visibility for Experience One (index 0)
    exp_0 = page.locator(".experience-item-form").nth(0)
    expect(exp_0.locator(".move-up-exp-btn")).not_to_be_visible()
    expect(exp_0.locator(".move-down-exp-btn")).to_be_visible()

    # Check button visibility for Experience Two (index 1)
    exp_1 = page.locator(".experience-item-form").nth(1)
    expect(exp_1.locator(".move-up-exp-btn")).to_be_visible()
    expect(exp_1.locator(".move-down-exp-btn")).to_be_visible()

    # Check button visibility for Experience Three (index 2)
    exp_2 = page.locator(".experience-item-form").nth(2)
    expect(exp_2.locator(".move-up-exp-btn")).to_be_visible()
    expect(exp_2.locator(".move-down-exp-btn")).not_to_be_visible()

    # Move "Experience One" down
    exp_0.locator(".move-down-exp-btn").click()
    assert get_titles() == ["Experience Two", "Experience One", "Experience Three"]
    
    # Check preview updated order
    exp_list = page.locator("#experience-list .experience-item")
    expect(exp_list.nth(0)).to_contain_text("Experience Two")
    expect(exp_list.nth(1)).to_contain_text("Experience One")
    expect(exp_list.nth(2)).to_contain_text("Experience Three")

    # Now "Experience One" is at index 1. Move it down again.
    page.locator(".experience-item-form").nth(1).locator(".move-down-exp-btn").click()
    assert get_titles() == ["Experience Two", "Experience Three", "Experience One"]
    expect(exp_list.nth(0)).to_contain_text("Experience Two")
    expect(exp_list.nth(1)).to_contain_text("Experience Three")
    expect(exp_list.nth(2)).to_contain_text("Experience One")

    # Now "Experience One" is at index 2. Move it up.
    page.locator(".experience-item-form").nth(2).locator(".move-up-exp-btn").click()
    assert get_titles() == ["Experience Two", "Experience One", "Experience Three"]

    # Move "Experience One" up again.
    page.locator(".experience-item-form").nth(1).locator(".move-up-exp-btn").click()
    assert get_titles() == ["Experience One", "Experience Two", "Experience Three"]
