import re
import sys
import os

sys.path.insert(0, os.path.abspath('./'))
from utils.constants import PIECE_UNITS, KG_UNITS, GRAM_UNITS, LITRE_UNITS, ML_UNITS, TENPIECE_UNITS 
from utils.tools import wspex_space

def get_weight_by_title(title: str) -> str:
    kg_pattern = r'\s+(?:\d{1,4}[×,.]\d{1,4}|\d{0,4})\s*(?:' + r'|'.join(KG_UNITS) + r')' + '(?:\s+|$)'
    g_pattern = r'\s+(?:\d{1,4}[×,.]\d{1,4}|\d{0,4})\s*(?:' + r'|'.join(GRAM_UNITS) + r')' + '(?:\s+|$)'
    l_pattern = r'\s+(?:\d{1,4}[×,.]\d{1,4}|\d{0,4})\s*(?:' + r'|'.join(LITRE_UNITS) + r')' + '(?:\s+|$)'
    ml_pattern = r'\s+(?:\d{1,4}[×,.]\d{1,4}|\d{0,4})\s*(?:' + r'|'.join(ML_UNITS) + r')' + '(?:\s+|$)'
    piece_pattern = r'\s+(?:\d{1,4}[×,.]\d{1,4}|\d{0,4})\s*(?:' + r'|'.join(PIECE_UNITS) + r')' + '(?:\s+|$)'
    tenpiece_pattern = r'\s*(?:\d{1,4}[×,.]\d{1,4}|\d{0,4})\s*(?:' + r'|'.join(TENPIECE_UNITS) + r')' + '(?:\s+|$)'


    patterns = [piece_pattern, tenpiece_pattern, kg_pattern, g_pattern, l_pattern, ml_pattern]
    site_unit = None
    for pattern in patterns:
        match = re.search(pattern, title.lower())
        if match:
            site_unit = wspex_space(match[0])
            # print(price_dict['site_unit'])

    if site_unit is None:
        site_unit = 'шт.'
    return site_unit