from consolemenu import *
from consolemenu.items import *
from consolemenu.format import *
from consolemenu.menu_component import Dimension

#### All the code below is for the setup of the main menu ####

# Prettying up the window with some formatting
menu_format = MenuFormatBuilder().set_border_style_type(MenuBorderStyleType.DOUBLE_LINE_OUTER_LIGHT_INNER_BORDER)\
    .set_prompt("SELECT>") \
    .set_title_align('center') \
    .set_subtitle_align('center') \
    .set_left_margin(4) \
    .set_right_margin(4) \
    .show_header_bottom_border(True)

# Creating the initial Menu
main_menu = ConsoleMenu("Kieran's Useful Web Scripts",
    epilogue_text="Select an Option from the choices above",
    formatter=menu_format)




#### This section is for you youtube menu ####

youtube_menu = SelectionMenu(["download"],title="Selection Menu",
                            subtitle="These menu items return to the previous menu",
                            formatter=menu_format)
# Create the menu item that opens the Selection submenu
youtube_menu = SubmenuItem("Youtube Menu", submenu=youtube_menu)
youtube_menu.set_menu(main_menu)
    
### Adding all submenu items to the main menu ###
main_menu.append_item(youtube_menu)


# Finally, we call show to show the main menu
main_menu.show()