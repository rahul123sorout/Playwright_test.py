from pages.form_page import FormPage
from pages.combo_page import ComboPage
from pages.tree_page import TreePage
from pages.list_page import ListPage
from pages.table_page import TablePage
from pages.toolbar_menu_page import ToolbarMenuPage
from pages.window_page import WindowPage
from pages.tab_page import TabPage
from pages.control_page import ControlPage
from pages.embed_page import EmbedPage
from pages.embedframe_page import EmbedFramePage
from pages.basic_page import BasicPage
from pages.misc_page import MiscPage


def test_widgetbrowser(page):

    # Create Page Objects
    form = FormPage(page)
    combo = ComboPage(page)
    tree = TreePage(page)
    list_page = ListPage(page)
    table = TablePage(page)
    toolbar = ToolbarMenuPage(page)
    window = WindowPage(page)
    tab = TabPage(page)
    control = ControlPage(page)
    embed = EmbedPage(page)
    embedframe = EmbedFramePage(page)
    basic = BasicPage(page)
    misc = MiscPage(page)

    # FORM
    form.fill_required_field("Rahul")
    form.fill_password("Test@123")

    # COMBOBOX
    combo.select_item_9()
    combo.select_item_299()

    selected_value = combo.get_selected_virtual_item()

    assert selected_value == "Item 299"

    # TREE
    tree.open_tree()
    tree.select_files()
    tree.select_sent()

    # LIST
    list_page.open_list()
    list_page.select_binder()
    list_page.select_heiden()

    # TABLE
    table.open_table()
    table.select_id_cell()
    table.select_number_cell()
    table.click_number_header()

    # TOOLBAR / MENU
    toolbar.open_toolbar_menu()
    toolbar.select_menu_radio_button()
    toolbar.select_menu_checkbox()

    # WINDOW
    window.open_window()
    window.uncheck_show_close()
    window.uncheck_resize_frame()
    window.open_modal_dialog()
    window.uncheck_modal()

    # TAB
    tab.open_tab_section()
    tab.select_notes()
    tab.select_calculator()

    # CONTROL
    control.open_control()
    control.select_red()
    control.select_next_month()
    control.select_date_one()

    # EMBED
    embed.open_embed()
    embed.scroll_html_to_bottom()

    # EMBED FRAME
    embedframe.open_embedframe()
    embedframe.scroll_first_frame()
    embedframe.scroll_themed_frame()

    # BASIC
    basic.open_basic()
    basic.click_disabled_button_three_times()

    # MISC
    misc.open_misc()
    misc.click_disabled_button_twice()
    misc.drag_item_1()