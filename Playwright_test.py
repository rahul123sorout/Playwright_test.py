from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:

    browser = playwright.chromium.launch(
        channel="msedge",
        headless=False
    )
    page = browser.new_page()
    page.goto(
        "https://qooxdoo.org/qxl.widgetbrowser/",
        wait_until="domcontentloaded"
    )

    required_field = page.locator(
        'css=input[placeholder="required"]'
    )
    required_field.fill("Rahul")

    print("1. Required field filled")

    password_field = page.locator(
        "xpath=//input[@type='password' and @placeholder='password']"
    )
    password_field.fill("Test@123")

    print("2. Password field filled")

    normal_combo = page.locator(
        'css=div[role="combobox"][tabindex="4"]'
    )

    normal_combo_button = normal_combo.locator(
        'css=div[role="button"]'
    )

    normal_combo_button.click()
    print("3. Normal ComboBox opened")

    item_9 = page.locator(
        "xpath=//div[@role='option' and normalize-space(.)='Item 9']"
    )

    item_9.click()

    print("4. Normal ComboBox -> Item 9 selected")

    virtual_combo = page.locator(
        'css=div[tabindex="5"]'
    )

    virtual_combo_button = virtual_combo.locator(
        'css=div[role="button"]'
    )

    virtual_combo_button.click()

    print("5. Virtual ComboBox opened")

    item_299 = page.locator(
        "xpath=//div[normalize-space(.)='Item 299' "
        "and not(contains(@style,'visibility: hidden'))]"
    )

    virtual_combo.hover()
    for _ in range(300):
        if item_299.count() > 0 and item_299.last.is_visible():
            print("6. Item 299 is visible")
            break

        page.mouse.wheel(0, 1000)
        page.wait_for_timeout(60)

    else:
        raise Exception(
            "Item 299 could not be reached in VirtualComboBox"
        )

    item_299.last.click()

    print("7. Item 299 clicked")


    virtual_input = virtual_combo.locator(
        'css=input[placeholder="Pick an item"]'
    )

    selected_value = virtual_input.input_value()

    print("8. Virtual ComboBox selected:", selected_value)

    if selected_value == "Item 299":
        print("9. SUCCESS -> Item 299 selected")
    else:
        raise Exception(
            f"Item 299 selection failed. Current value: {selected_value}"
        )

#Tree section


    tree_tab = page.get_by_role("tab", name="Tree")
    tree_tab.click()

    print("10. Tree section opened")
    page.wait_for_timeout(1500)

    files_item = page.locator(
        "xpath=//div[normalize-space(.)='Files']"
    )

    files_item.first.click()

    print("11. Tree -> Files selected")
    page.wait_for_timeout(1500)


    sent_item = page.locator(
        "xpath=//span[normalize-space(.)='Sent']/ancestor::div[@role='gridcell']"
    )

    sent_item.click()

    print("12. TreeVirtual -> Sent selected")
    page.wait_for_timeout(1500)

#List section 

    list_tab = page.get_by_role("tab", name="List")
    list_tab.click()

    print("13. List section opened")
    page.wait_for_timeout(1500)
 
    binder_item = page.locator(
       "xpath=//div[normalize-space(.)='Binder, Marita']"
)

    binder_item.last.click()

    print("14. Normal List -> Binder, Marita selected")
    page.wait_for_timeout(1500)


    heiden_item = page.locator(
       "xpath=//div[normalize-space(.)='Heiden, Notfried']"
)

    heiden_item.last.click()

    print("15. Virtual Grouped List -> Heiden, Notfried selected")
    page.wait_for_timeout(1500)


# TABLE SECTION

    table_tab = page.get_by_role("tab", name="Table")
    table_tab.click()

    print("16. Table section opened")
    page.wait_for_timeout(1500)

    id_cells = page.locator(
        "css=div[role='gridcell'][data-qx-table-cell-col='0']"
    )

    for i in range(id_cells.count()):
       if id_cells.nth(i).is_visible():
        id_cells.nth(i).click()
        break

    print("17. Table -> ID cell selected")
    page.wait_for_timeout(1500)

    number_cells = page.locator(
        "css=div[role='gridcell'][data-qx-table-cell-col='1']"
    )

    for i in range(number_cells.count()):
      if number_cells.nth(i).is_visible():
        number_cells.nth(i).click()
        break

    print("18. Table -> A number cell selected")
    page.wait_for_timeout(1500)


    number_header = page.locator(
       "xpath=//div[@role='columnheader']"
       "[.//div[normalize-space(.)='A number']]"
    )

    number_header.click()

    print("19. Table -> A number column header clicked")
    page.wait_for_timeout(2000)


#ToolBar/Menu section

    toolbar_tab = page.get_by_role("tab", name="Toolbar/Menu")
    toolbar_tab.click()

    print("20. Toolbar/Menu section opened")
    page.wait_for_timeout(1500)

    toolbar_menu_button = page.locator(
       "xpath=//div[@role='button' and @aria-haspopup='menu']"
       "[.//div[normalize-space(.)='Toolbar MenuButton']]"
)

    toolbar_menu_button.click()

    print("21. Toolbar MenuButton opened")
    page.wait_for_timeout(1500)

    menu_radio_button = page.locator(
      "xpath=//div[normalize-space(.)='Menu RadioButton']"
)

    menu_radio_button.last.click()

    print("22. Toolbar Menu -> Menu RadioButton selected")
    page.wait_for_timeout(1500)


    menubar_button = page.locator(
       "xpath=//div[@role='button' and @aria-haspopup='menu']"
       "[.//div[normalize-space(.)='Menubar Button']]"
).first

    menubar_button.click()

    print("23. Menubar Button opened")
    page.wait_for_timeout(1500)


    menu_checkbox = page.locator(
       "xpath=//div[normalize-space(.)='Menu MenuCheckBox']"
)

    menu_checkbox.last.click()
    print("24. Menubar -> Menu MenuCheckBox selected")
    page.wait_for_timeout(1500)


# WINDOW SECTION

    window_tab = page.get_by_role("tab", name="Window")
    window_tab.click()

    print("25. Window section opened")
    page.wait_for_timeout(1500)

    show_close = page.locator(
       "xpath=//div[@role='checkbox' and .//div[normalize-space(.)='Show Close']]"
)

    if show_close.get_attribute("aria-checked") == "true":
       show_close.click()

    print("26. Window -> Show Close unchecked")
    page.wait_for_timeout(1500)


    resize_frame = page.locator(
       "xpath=//div[@role='checkbox' and .//div[normalize-space(.)='Use resize frame']]"
)

    if resize_frame.get_attribute("aria-checked") == "true":
       resize_frame.click()

    print("27. Window -> Use resize frame unchecked")
    page.wait_for_timeout(1500)

    modal_button_1 = page.locator(
       "xpath=//div[@role='button' and "
       ".//div[normalize-space(.)='Open Modal Dialog 1']]"
)

    modal_button_1.click()
    print("28. Window -> Open Modal Dialog 1 clicked")


    modal_checkbox = page.locator(
      "xpath=//div[@role='checkbox' and .//div[normalize-space(.)='Modal']]"
)

    if modal_checkbox.get_attribute("aria-checked") == "true":
     modal_checkbox.click()

    print("29. Modal Dialog -> Modal unchecked")
    page.wait_for_timeout(2000)


# TAB SECTION

    tab_section = page.get_by_role("tab", name="Tab", exact=True)
    tab_section.click()

    print("30. Tab section opened")
    page.wait_for_timeout(1500)

    notes_tabs = page.locator(
       "xpath=//div[@role='tab' and .//div[normalize-space(.)='Notes']]"
)

    notes_tabs.nth(0).click()

    print("31. Top Left -> Notes selected")
    page.wait_for_timeout(1500)


    calculator_tabs = page.locator(
       "xpath=//div[@role='tab' and .//div[normalize-space(.)='Calculator']]"
)

    calculator_tabs.nth(1).click()

    print("32. Top Right -> Calculator selected")
    page.wait_for_timeout(1500)


# CONTROL SECTION

    control_tab = page.get_by_role("tab", name="Control")
    control_tab.click()
   
    print("33. Control section opened")
    page.wait_for_timeout(1500)

    red_color = page.locator(
      "css=div.qx-main-dark[style*='background-color:red']"
)

    red_color.click()

    print("34. ColorSelector -> Red selected")
    page.wait_for_timeout(1500)


    next_month_button = page.locator(
    "css=div[role='button'] div[style*='right.gif']"
).locator("..")

    next_month_button.click()

    print("35. DateChooser -> Next month clicked")
    page.wait_for_timeout(2000)

    date_one = page.locator(
       "xpath=//div[normalize-space(.)='1']"
)

    for i in range(date_one.count()):
      if date_one.nth(i).is_visible():
        date_one.nth(i).click()
        break

    print("36. DateChooser -> Date 1 selected")
    page.wait_for_timeout(2000)


# EMBED SECTION

    embed_tab = page.get_by_role("tab", name="Embed", exact=True)
    embed_tab.click()

    print("37. Embed section opened")
    page.wait_for_timeout(1500)


    html_scroll_box = page.locator(
       'css=div[tabindex="1"][qxselectable="on"]'
       '[style*="overflow-y:auto"]'
       '[style*="top:60px"]'
       '[style*="height:150px"]'
).first

    html_scroll_box.evaluate(
       "element => element.scrollTop = element.scrollHeight"
)

    print("38. Embed -> HTML content scrolled to bottom")
    page.wait_for_timeout(2000)

    
# EMBEDFRAME SECTION

    embedframe_tab = page.get_by_role("tab", name="EmbedFrame", exact=True)
    embedframe_tab.click()

    print("39. EmbedFrame section opened")
    page.wait_for_timeout(1500)

    iframes = page.locator("css=iframe")

    first_frame = iframes.nth(0)
    first_frame.evaluate(
       "element => element.contentWindow.scrollTo(0, element.contentDocument.body.scrollHeight)"
)

    print("40. Iframe -> Scrolled to bottom")
    page.wait_for_timeout(1500)


    themed_iframe = page.locator("css=iframe").nth(1)
    themed_iframe.evaluate(
       "element => element.contentWindow.scrollTo(0, element.contentDocument.body.scrollHeight)"
)
    print("41. ThemedIframe -> Scrolled to bottom")
    page.wait_for_timeout(2000)


# BASIC SECTION

    basic_tab = page.get_by_role("tab", name="Basic", exact=True)
    basic_tab.click()

    print("42. Basic section opened")
    page.wait_for_timeout(1500)

    disabled_buttons = page.locator(
       "xpath=//div[@role='button' and .//div[normalize-space(.)='Disabled']]"
)

    for i in range(disabled_buttons.count()):
     if disabled_buttons.nth(i).is_visible():
        disabled_button = disabled_buttons.nth(i)
        break

    disabled_button.click()
    page.wait_for_timeout(500)

    disabled_button.click()
    page.wait_for_timeout(500)

    disabled_button.click()

    print("43. Basic -> Disabled button clicked 3 times")
    page.wait_for_timeout(1500)

    
# MISC SECTION

    misc_tab = page.get_by_role("tab", name="Misc", exact=True)
    misc_tab.click()

    print("44. Misc section opened")
    page.wait_for_timeout(1500)

    disabled_buttons = page.locator(
       "xpath=//div[@role='button' and .//div[normalize-space(.)='Disabled']]"
)

    for i in range(disabled_buttons.count()):
      if disabled_buttons.nth(i).is_visible():
        disabled_button = disabled_buttons.nth(i)
        break

    disabled_button.click()
    page.wait_for_timeout(500)

    disabled_button.click()

    print("45. Misc -> Disabled button clicked 2 times")
    page.wait_for_timeout(1000)

 
    item_1_list = page.locator(
       "xpath=//div[normalize-space(.)='Item 1']"
)

    for i in range(item_1_list.count()):
      if item_1_list.nth(i).is_visible():
        item_1 = item_1_list.nth(i)
        break

    right_drop_box = page.locator(
        'css=div[qxdroppable="on"][aria-orientation="vertical"]'
)

    item_1.drag_to(right_drop_box)

    print("46. DragDrop -> Item 1 moved to right box")
    page.wait_for_timeout(2000)

    print("\nWidgetBrowser Playwright demo completed successfully.")
    page.wait_for_timeout(3000)

    browser.close()

with sync_playwright() as playwright:
    run(playwright)