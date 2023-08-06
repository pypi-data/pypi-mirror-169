import json
from pathlib import Path

def default_settings():
    return {
        'login_url': '',
        'class_home_url': '',
        'student_home_url': '',
        'theme': 'LightBlue',
        'kudos': 70.0,
        'uhoh': 60.0,
        'output_folder': '',
        'get_new_class_lists': True,
        'newest_class_list_fn': '',
        'xlsx_dir': '',
        'class_lists': [
            {
                'name': 'Placeholder',
                'url': ''
            }
        ],
        'xslx_dir': ''
    }


def settings_path():
    this_path = Path(__file__).parent.as_posix()
    return f'{this_path}/resources/settings.json'

def get_settings():
    try:
        with open(settings_path(), 'r') as f:
            return json.load(f)
    except:
        settings = default_settings()
        save_settings(settings)
        return settings

def edit_settings(key: str, value):
    settings = get_settings()
    settings[key] = value
    with open(settings_path(), 'w') as f:
        json.dump(settings, f, indent=4)

def save_settings(settings):
    with open(settings_path(), 'w') as f:
        json.dump(settings, f, indent=4)
        