from pathlib import Path

import PySimpleGUIQt as sg

import data_minion.handle_settings as hs

# pylint: disable=no-member
def make_layout(settings):
    
    kudos_tip = 'The number above which ALL grades must be to be grouped with "Kudos" students.'
    uhoh_tip = 'ANY grade below this number will group a student in "Uhoh"'
    
    split_students_frame = [
        [sg.Text('"Kudos" Threshold:'), 
            sg.Input(settings['kudos'], key='-kudos_thresh-', tooltip=kudos_tip)],
        [sg.Text('"Uhoh" Threshold:'), sg.Input(settings['uhoh'], key='-uhoh_thresh-', tooltip=uhoh_tip)]
    ]

    app_settings_frame = [
        [sg.Text('Output Folder'), 
                sg.Input(settings['output_folder'], key='-output_folder-'), 
                sg.FolderBrowse('Browse', 
                        tooltip='This is where all output form data_minion (data files, Excel files, etc.) will be saved', 
                        initial_folder=settings['output_folder'])],
        [sg.Text('Color Theme:'), 
            sg.Drop(['Black', 'BrightColors', 'Dark', 'DarkBrown', 'LightBlue', 'LightPurple', 'LightTeal'],
                      default_value=settings['theme'], key='-theme-', readonly=True)],
    ]

    return [
        [sg.Text('Settings for your data_minion')],
        [sg.Frame('Groupings Thresholds', split_students_frame)],
        [sg.Frame('data_minion Application Settings', app_settings_frame)],
        [sg.Button('Save Settings'), sg.Button('Cancel'), sg.Button('Done')]
    ]

def save_settings(main_dir, settings, values):
    settings['output_folder'] = Path(values['-output_folder-']).absolute().as_posix()
    try:
        settings['kudos'] = float(values['-kudos_thresh-'])
        settings['uhoh'] = float(values['-uhoh_thresh-'])
    except:
        sg.popup_quick_message('"Kudos" and "Uhoh" inputs must be numbers.')
        return
    settings['theme'] = values['-theme-']

    hs.save_settings(settings)

    sg.popup_quick_message('Settings Saved!\n\
Theme change take affect on app restart.')

def set_settings(main_dir, icon):
    settings = hs.get_settings()
    sg.theme(settings['theme'])
    sg.set_options(border_width=1)
    layout = make_layout(settings)
    window = sg.Window('data_minion: Settings', layout, icon=icon)
    window.finalize()

    while True:
        event, values = window.read()

        if event in ['Cancel', sg.WIN_CLOSED, None, 'Done']:
            break

        elif event == 'Save Settings':
            save_settings(main_dir, settings, values)

    window.close()