PO_DIR = 'po'
MO_DIR = 'locale'
LOCALE_DOMAIN = "indicator-stickynotes"

SETTINGS_FILE = "~/.config/indicator-stickynotes"
DEBUG_SETTINGS_FILE = "~/.stickynotes"

FALLBACK_PROPERTIES = { "bgcolor_hsv": [48./360, 1, 1],
                        "textcolor": [32./255, 32./255, 32./255],
                        "font": "",
                        "shadow": 60}
                        
THEMES_FOLDER = "themes"
DEFAULT_THEME_NAME = "default"
DEFAULT_ICONS_FOLDER_NAME = "icons"
DEFAULT_CSS_FOLDER_NAME = "css"

DEFAULT_ICON_FILES = {"imgAdd":"note_add.svg", 
                        "imgClose":"delete.svg", 
                        "imgDropdown":"menu.svg",
                        "imgLock":"lock.svg", 
                        "imgUnlock":"lock_open.svg", 
                        "imgResizeR":"resizer.svg"}
TEMPLATES_FOLDER = "templates"
DEFAULT_TEMPLATE = "default"

def get_theme_icons_folder():
    return THEMES_FOLDER + "/" + DEFAULT_THEME_NAME + "/" + DEFAULT_ICONS_FOLDER_NAME + "/"
    
def get_theme_css_folder():
    return THEMES_FOLDER + "/" + DEFAULT_THEME_NAME + "/" + DEFAULT_CSS_FOLDER_NAME + "/"
    
def get_template_folder():
    return TEMPLATES_FOLDER + "/" + DEFAULT_TEMPLATE + "/"