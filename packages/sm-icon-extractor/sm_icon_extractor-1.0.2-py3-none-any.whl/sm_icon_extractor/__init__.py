import configparser
import pyjson5 as json
import os
import re
from xml.dom import minidom

import PIL.Image


# Exceptions
class GamePathNotConfiguredException(BaseException):
    def __init__(self, message='Game path not configured'):
        super().__init__(message)

class IconMap():
    def __init__(self, name, base_path, xml_name, description_path):
        self.name = name
        self.base_path = base_path
        self.xml_name = xml_name
        self.description_path = description_path

CONFIG_NAME = 'sm-icon-extractor.ini'
CONFIG_GLOBAL_PATH = os.path.expanduser(os.path.join('~', '.config', CONFIG_NAME))

LANGUAGE = 'English'
ICONMAPS = {
    'challenge': IconMap('challenge', os.path.join('ChallengeData', 'Gui'), 'IconMapChallenge.xml', os.path.join('Language', LANGUAGE, 'inventoryDescriptions.json')),
    'creative': IconMap('creative', os.path.join('Data', 'Gui'), 'IconMap.xml', os.path.join('Language', LANGUAGE, 'InventoryItemDescriptions.json')),
    'customization': IconMap('customization', os.path.join('Data', 'Gui'), 'CustomizationIconMap.xml', os.path.join('Language', LANGUAGE, 'CustomizationDescriptions.json')),
    'tool': IconMap('tool', os.path.join('Data', 'Gui'), 'ToolIconMap.xml', os.path.join('Language', LANGUAGE, 'InventoryItemDescriptions.json')),
    'survival': IconMap('survival', os.path.join('Survival', 'Gui'), 'IconMapSurvival.xml', os.path.join('Language', LANGUAGE, 'inventoryDescriptions.json')),
}
INVALID_FILE_CHAR_REGEX = re.compile('[!"#$&\'()*,/:;<=>?[\\]{|}]')

def extract_icon_map(game_path: str, iconmap: IconMap, dest: str, verbose=False) -> None:
    if verbose:
        print(f'Extracting map "{iconmap.name}" ...')
    
    dom = minidom.parse(os.path.join(game_path, iconmap.base_path, iconmap.xml_name))
    with open(os.path.join(game_path, iconmap.base_path, iconmap.description_path), 'r') as f:
        descriptions = json.loads(f.read())
    saved = {} # <title>: <UUID of first icon with this name> - names of saved icons (used to resolve collisions)
    for resource in dom.getElementsByTagName('MyGUI')[0].getElementsByTagName('Resource'):
        for group in resource.getElementsByTagName('Group'):
            size = group.attributes['size'].value.split(' ')
            w = int(size[0])
            h = int(size[1])
            
            with PIL.Image.open(os.path.join(game_path, iconmap.base_path, group.attributes['texture'].value)) as texture:
                for index in group.getElementsByTagName('Index'):
                    uuid = index.attributes['name'].value
                    if uuid == 'Empty':
                        continue
                    if len(uuid) > 36:
                        gender = uuid[37:]
                        uuid = uuid[:36]
                    else:
                        gender = None
                    
                    pos = index.getElementsByTagName('Frame')[0].attributes['point'].value.split(' ')
                    x = int(pos[0])
                    y = int(pos[1])
                    
                    with texture.crop((x, y, x + w, y + h)) as icon:
                        name = descriptions[uuid]['title'] if uuid in descriptions else uuid
                        name = INVALID_FILE_CHAR_REGEX.sub('_', name)
                        if gender:
                            name = f'{name}_{gender}'
                        if name in saved:
                            col_path = os.path.join(dest, f'{name}')
                            col_path_w_ext = f'{col_path}.png'
                            if os.path.exists(col_path_w_ext):
                                os.rename(col_path_w_ext, f'{col_path}_{saved[name]}.png')
                            name = f'{name}_{uuid}'
                        else:
                            saved[name] = uuid
                        icon.save(os.path.join(dest, f'{name}.png'))

def extract(map, dest, verbose=False) -> None:
    config = configparser.ConfigParser()
    config.read([CONFIG_GLOBAL_PATH, CONFIG_NAME])
    if not 'Game' in config:
        config.add_section('Game')
        if not 'Path' in config['Game']:
            raise GamePathNotConfiguredException()
    
    for m in [map] if map else ICONMAPS.values():
        if map:
            real_dest = dest
        else:
            real_dest = os.path.join(dest, m.name)
        os.makedirs(real_dest, exist_ok=True)
        extract_icon_map(config['Game']['Path'], m, real_dest, verbose=verbose)
    
    if verbose:
        print('Finished extracting!')
