from playwright.sync_api import Page, expect


def test_edit_skills_preview(page: Page, server: str):
    page.goto(server)

    # Create new profile
    page.get_by_text("Create New Profile").click()

    # Click Add Skill Category
    page.get_by_text("Add Skill Category").click()

    # Wait for the input to appear
    input_selector = 'input[name="skills[0][name]"]'
    page.wait_for_selector(input_selector)

    # Fill in category name and items
    page.locator(input_selector).fill("Frontend")
    page.locator('textarea[name="skills[0][items]"]').fill("React\nTailwind\nAlpine JS")

    # Check preview
    preview = page.locator("#resume-preview")
    expect(preview.locator("#skills-list")).to_contain_text("Frontend")
    expect(preview.locator("#skills-list")).to_contain_text("React")
    expect(preview.locator("#skills-list")).to_contain_text("Tailwind")
    expect(preview.locator("#skills-list")).to_contain_text("Alpine JS")


def test_add_multiple_skill_categories(page: Page, server: str):
    page.goto(server)

    # Create new profile
    page.get_by_text("Create New Profile").click()

    # Add first
    page.get_by_text("Add Skill Category").click()
    page.wait_for_selector('input[name="skills[0][name]"]')
    page.locator('input[name="skills[0][name]"]').fill("Backend")
    page.locator('textarea[name="skills[0][items]"]').fill("Python\nFastAPI")

    # Add second
    page.get_by_text("Add Skill Category").click()
    page.wait_for_selector('input[name="skills[1][name]"]')
    page.locator('input[name="skills[1][name]"]').fill("Database")
    page.locator('textarea[name="skills[1][items]"]').fill("PostgreSQL\nSQLite")

    # Check preview for both
    preview = page.locator("#resume-preview")
    expect(preview.locator("#skills-list")).to_contain_text("Backend")
    expect(preview.locator("#skills-list")).to_contain_text("Python")
    expect(preview.locator("#skills-list")).to_contain_text("Database")
    expect(preview.locator("#skills-list")).to_contain_text("PostgreSQL")


def test_remove_skill_category(page: Page, server: str):
    page.goto(server)

    # Create new profile
    page.get_by_text("Create New Profile").click()

    # Add a category
    page.get_by_text("Add Skill Category").click()
    page.wait_for_selector('input[name="skills[0][name]"]')
    page.locator('input[name="skills[0][name]"]').fill("To Remove")

    preview = page.locator("#resume-preview")
    expect(preview.locator("#skills-list")).to_contain_text("To Remove")

    # Remove it
    page.locator(".remove-skill-btn").click()

    # Check it's gone from preview
    expect(preview.locator("#skills-list")).not_to_contain_text("To Remove")
