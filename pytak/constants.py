#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Python Team Awareness Kit (PyTAK) Module Constants."""

import logging
import os

__author__ = "Greg Albrecht W2GMD <oss@undef.net>"
__copyright__ = "Copyright 2021 Orion Labs, Inc."
__license__ = "Apache License, Version 2.0"


if bool(os.environ.get('DEBUG')):
    LOG_LEVEL: int = logging.DEBUG
    LOG_FORMAT: logging.Formatter = logging.Formatter(
        ('%(asctime)s pytak %(levelname)s %(name)s.%(funcName)s:%(lineno)d - '
         '%(message)s'))
    logging.debug('pytak Debugging Enabled via DEBUG Environment Variable.')
else:
    LOG_LEVEL: int = logging.INFO
    LOG_FORMAT: logging.Formatter = logging.Formatter(
        ('%(asctime)s pytak %(levelname)s - %(message)s'))


DEFAULT_COT_PORT: int = 8087
DEFAULT_ATAK_PORT: int = 4242
DEFAULT_BROADCAST_PORT: int = 6969
DEFAULT_BACKOFF: int = 120
DEFAULT_SLEEP: int = 5
DEFAULT_COT_STALE: int = 120
DEFAULT_FIPS_CIPHERS: str = "ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-ECDSA-AES256-GCM-SHA384"
ISO_8601_UTC = "%Y-%m-%dT%H:%M:%S.%fZ"

DOMESTIC_AIRLINES: list = [
    "AAL",
    "UAL",
    "FDX",
    "UPS",
    "SWA"
]

DEFAULT_HEX_RANGES: dict = {
    "US-CIV": {"start": 0xA00000, "end": 0xADF7C7},
    "US-MIL": {"start": 0xADF7C8, "end": 0xAFFFFF},
    "CAN-CIV": {"start": 0xC00000, "end": 0xC0CDF8},
    "CAN-MIL": {"start": 0xC0CDF9, "end": 0xC3FFFF},
    "NZ-CIV": {"start": 0xC80000, "end": 0xC87FFF},
    "NZ-MIL": {"start": 0xC87F00, "end": 0xC87FFF},
    "AUS-CIV": {"start": 0x7C0000, "end": 0x7FFFFF},
    "AUS-MIL": {"start": 0x7CF800, "end": 0x7CFAFF},
    "UK-CIV": {"start": 0x400000, "end": 0x43FFFF},
    "UK-MIL": {"start": 0x43C000, "end": 0x43CFFF}
}

ICAO_RANGES = [
    {"start": 0x700000, "end": 0x700FFF, "country": "Afghanistan"},
    {"start": 0x501000, "end": 0x5013FF, "country": "Albania"},
    {"start": 0x0A0000, "end": 0x0A7FFF, "country": "Algeria"},
    {"start": 0x090000, "end": 0x090FFF, "country": "Angola"},
    {"start": 0x0CA000, "end": 0x0CA3FF, "country": "Antigua and Barbuda"},
    {"start": 0xE00000, "end": 0xE3FFFF, "country": "Argentina"},
    {"start": 0x600000, "end": 0x6003FF, "country": "Armenia"},
    # { "start": 0x7C0000, "end": 0x7FFFFF, "country": "Australia" },
    {"start": 0x440000, "end": 0x447FFF, "country": "Austria"},
    {"start": 0x600800, "end": 0x600BFF, "country": "Azerbaijan"},
    {"start": 0x0A8000, "end": 0x0A8FFF, "country": "Bahamas"},
    {"start": 0x894000, "end": 0x894FFF, "country": "Bahrain"},
    {"start": 0x702000, "end": 0x702FFF, "country": "Bangladesh"},
    {"start": 0x0AA000, "end": 0x0AA3FF, "country": "Barbados"},
    {"start": 0x510000, "end": 0x5103FF, "country": "Belarus"},
    {"start": 0x448000, "end": 0x44FFFF, "country": "Belgium"},
    {"start": 0x0AB000, "end": 0x0AB3FF, "country": "Belize"},
    {"start": 0x094000, "end": 0x0943FF, "country": "Benin"},
    {"start": 0x680000, "end": 0x6803FF, "country": "Bhutan"},
    {"start": 0xE94000, "end": 0xE94FFF, "country": "Bolivia"},
    {"start": 0x513000, "end": 0x5133FF, "country": "Bosnia & Herzegovina"},
    {"start": 0x030000, "end": 0x0303FF, "country": "Botswana"},
    {"start": 0xE40000, "end": 0xE7FFFF, "country": "Brazil"},
    {"start": 0x895000, "end": 0x8953FF, "country": "Brunei Darussalam"},
    {"start": 0x450000, "end": 0x457FFF, "country": "Bulgaria"},
    {"start": 0x09C000, "end": 0x09CFFF, "country": "Burkina Faso"},
    {"start": 0x032000, "end": 0x032FFF, "country": "Burundi"},
    {"start": 0x70E000, "end": 0x70EFFF, "country": "Cambodia"},
    {"start": 0x034000, "end": 0x034FFF, "country": "Cameroon"},
    # { "start": 0xC00000, "end": 0xC3FFFF, "country": "Canada" },
    {"start": 0x096000, "end": 0x0963FF, "country": "Cape Verde"},
    {"start": 0x06C000, "end": 0x06CFFF,
     "country": "Central African Republic"},
    {"start": 0x084000, "end": 0x084FFF, "country": "Chad"},
    {"start": 0xE80000, "end": 0xE80FFF, "country": "Chile"},
    {"start": 0x780000, "end": 0x7BFFFF, "country": "China"},
    {"start": 0x0AC000, "end": 0x0ACFFF, "country": "Colombia"},
    {"start": 0x035000, "end": 0x0353FF, "country": "Comoros"},
    {"start": 0x036000, "end": 0x036FFF, "country": "Congo"},
    {"start": 0x901000, "end": 0x9013FF, "country": "Cook Islands"},
    {"start": 0x0AE000, "end": 0x0AEFFF, "country": "Costa Rica"},
    {"start": 0x038000, "end": 0x038FFF, "country": "Cote d'Ivoire"},
    {"start": 0x501C00, "end": 0x501FFF, "country": "Croatia"},
    {"start": 0x0B0000, "end": 0x0B0FFF, "country": "Cuba"},
    {"start": 0x4C8000, "end": 0x4C83FF, "country": "Cyprus"},
    {"start": 0x498000, "end": 0x49FFFF, "country": "Czech Republic"},
    {"start": 0x720000, "end": 0x727FFF, "country": "DPRK(North Korea)"},
    {"start": 0x08C000, "end": 0x08CFFF, "country": "Dem Rep of the Congo"},
    {"start": 0x458000, "end": 0x45FFFF, "country": "Denmark"},
    {"start": 0x098000, "end": 0x0983FF, "country": "Djibouti"},
    {"start": 0x0C4000, "end": 0x0C4FFF, "country": "Dominican Republic"},
    {"start": 0xE84000, "end": 0xE84FFF, "country": "Ecuador"},
    {"start": 0x010000, "end": 0x017FFF, "country": "Egypt"},
    {"start": 0x0B2000, "end": 0x0B2FFF, "country": "El Salvador"},
    {"start": 0x042000, "end": 0x042FFF, "country": "Equatorial Guinea"},
    {"start": 0x202000, "end": 0x2023FF, "country": "Eritrea"},
    {"start": 0x511000, "end": 0x5113FF, "country": "Estonia"},
    {"start": 0x040000, "end": 0x040FFF, "country": "Ethiopia"},
    {"start": 0xC88000, "end": 0xC88FFF, "country": "Fiji"},
    {"start": 0x460000, "end": 0x467FFF, "country": "Finland"},
    {"start": 0x380000, "end": 0x3BFFFF, "country": "France"},
    {"start": 0x03E000, "end": 0x03EFFF, "country": "Gabon"},
    {"start": 0x09A000, "end": 0x09AFFF, "country": "Gambia"},
    {"start": 0x514000, "end": 0x5143FF, "country": "Georgia"},
    {"start": 0x3C0000, "end": 0x3FFFFF, "country": "Germany"},
    {"start": 0x044000, "end": 0x044FFF, "country": "Ghana"},
    {"start": 0x468000, "end": 0x46FFFF, "country": "Greece"},
    {"start": 0x0CC000, "end": 0x0CC3FF, "country": "Grenada"},
    {"start": 0x0B4000, "end": 0x0B4FFF, "country": "Guatemala"},
    {"start": 0x046000, "end": 0x046FFF, "country": "Guinea"},
    {"start": 0x048000, "end": 0x0483FF, "country": "Guinea-Bissau"},
    {"start": 0x0B6000, "end": 0x0B6FFF, "country": "Guyana"},
    {"start": 0x0B8000, "end": 0x0B8FFF, "country": "Haiti"},
    {"start": 0x0BA000, "end": 0x0BAFFF, "country": "Honduras"},
    {"start": 0x470000, "end": 0x477FFF, "country": "Hungary"},
    {"start": 0x4CC000, "end": 0x4CCFFF, "country": "Iceland"},
    {"start": 0x800000, "end": 0x83FFFF, "country": "India"},
    {"start": 0x8A0000, "end": 0x8A7FFF, "country": "Indonesia"},
    {"start": 0x730000, "end": 0x737FFF, "country": "Iran"},
    {"start": 0x728000, "end": 0x72FFFF, "country": "Iraq"},
    {"start": 0x4CA000, "end": 0x4CAFFF, "country": "Ireland"},
    {"start": 0x738000, "end": 0x73FFFF, "country": "Israel"},
    {"start": 0x300000, "end": 0x33FFFF, "country": "Italy"},
    {"start": 0x0BE000, "end": 0x0BEFFF, "country": "Jamaica"},
    {"start": 0x840000, "end": 0x87FFFF, "country": "Japan"},
    {"start": 0x740000, "end": 0x747FFF, "country": "Jordan"},
    {"start": 0x683000, "end": 0x6833FF, "country": "Kazakhstan"},
    {"start": 0x04C000, "end": 0x04CFFF, "country": "Kenya"},
    {"start": 0xC8E000, "end": 0xC8E3FF, "country": "Kiribati"},
    {"start": 0x706000, "end": 0x706FFF, "country": "Kuwait"},
    {"start": 0x601000, "end": 0x6013FF, "country": "Kyrgyzstan"},
    {"start": 0x708000, "end": 0x708FFF, "country": "Laos"},
    {"start": 0x502C00, "end": 0x502FFF, "country": "Latvia"},
    {"start": 0x748000, "end": 0x74FFFF, "country": "Lebanon"},
    {"start": 0x04A000, "end": 0x04A3FF, "country": "Lesotho"},
    {"start": 0x050000, "end": 0x050FFF, "country": "Liberia"},
    {"start": 0x018000, "end": 0x01FFFF,
     "country": "Libyan Arab Jamahiriya"},
    {"start": 0x503C00, "end": 0x503FFF, "country": "Lithuania"},
    {"start": 0x4D0000, "end": 0x4D03FF, "country": "Luxembourg"},
    {"start": 0x054000, "end": 0x054FFF, "country": "Madagascar"},
    {"start": 0x058000, "end": 0x058FFF, "country": "Malawi"},
    {"start": 0x750000, "end": 0x757FFF, "country": "Malaysia"},
    {"start": 0x05A000, "end": 0x05A3FF, "country": "Maldives"},
    {"start": 0x05C000, "end": 0x05CFFF, "country": "Mali"},
    {"start": 0x4D2000, "end": 0x4D23FF, "country": "Malta"},
    {"start": 0x900000, "end": 0x9003FF, "country": "Marshall Islands"},
    {"start": 0x05E000, "end": 0x05E3FF, "country": "Mauritania"},
    {"start": 0x060000, "end": 0x0603FF, "country": "Mauritius"},
    {"start": 0x0D0000, "end": 0x0D7FFF, "country": "Mexico"},
    {"start": 0x681000, "end": 0x6813FF,
     "country": "FedStates of Micronesia"},
    {"start": 0x4D4000, "end": 0x4D43FF, "country": "Monaco"},
    {"start": 0x682000, "end": 0x6823FF, "country": "Mongolia"},
    {"start": 0x516000, "end": 0x5163FF, "country": "Montenegro"},
    {"start": 0x020000, "end": 0x027FFF, "country": "Morocco"},
    {"start": 0x006000, "end": 0x006FFF, "country": "Mozambique"},
    {"start": 0x704000, "end": 0x704FFF, "country": "Myanmar"},
    {"start": 0x201000, "end": 0x2013FF, "country": "Namibia"},
    {"start": 0xC8A000, "end": 0xC8A3FF, "country": "Nauru"},
    {"start": 0x70A000, "end": 0x70AFFF, "country": "Nepal"},
    {"start": 0x480000, "end": 0x487FFF, "country": "Netherlands"},
    # { "start": 0xC80000, "end": 0xC87FFF, "country": "New Zealand" },
    {"start": 0x0C0000, "end": 0x0C0FFF, "country": "Nicaragua"},
    {"start": 0x062000, "end": 0x062FFF, "country": "Niger"},
    {"start": 0x064000, "end": 0x064FFF, "country": "Nigeria"},
    {"start": 0x478000, "end": 0x47FFFF, "country": "Norway"},
    {"start": 0x70C000, "end": 0x70C3FF, "country": "Oman"},
    {"start": 0x760000, "end": 0x767FFF, "country": "Pakistan"},
    {"start": 0x684000, "end": 0x6843FF, "country": "Palau"},
    {"start": 0x0C2000, "end": 0x0C2FFF, "country": "Panama"},
    {"start": 0x898000, "end": 0x898FFF, "country": "Papua New Guinea"},
    {"start": 0xE88000, "end": 0xE88FFF, "country": "Paraguay"},
    {"start": 0xE8C000, "end": 0xE8CFFF, "country": "Peru"},
    {"start": 0x758000, "end": 0x75FFFF, "country": "Philippines"},
    {"start": 0x488000, "end": 0x48FFFF, "country": "Poland"},
    {"start": 0x490000, "end": 0x497FFF, "country": "Portugal"},
    {"start": 0x06A000, "end": 0x06A3FF, "country": "Qatar"},
    {"start": 0x718000, "end": 0x71FFFF, "country": "Republic of Korea"},
    {"start": 0x504C00, "end": 0x504FFF, "country": "Republic of Moldova"},
    {"start": 0x4A0000, "end": 0x4A7FFF, "country": "Romania"},
    {"start": 0x100000, "end": 0x1FFFFF, "country": "Russian Federation"},
    {"start": 0x06E000, "end": 0x06EFFF, "country": "Rwanda"},
    {"start": 0xC8C000, "end": 0xC8C3FF, "country": "Saint Lucia"},
    {"start": 0x0BC000, "end": 0x0BC3FF,
     "country": "Saint Vincent and the Grenadines"},
    {"start": 0x902000, "end": 0x9023FF, "country": "Samoa"},
    {"start": 0x500000, "end": 0x5003FF, "country": "San Marino"},
    {"start": 0x09E000, "end": 0x09E3FF,
     "country": "Sao Tome and Principe"},
    {"start": 0x710000, "end": 0x717FFF, "country": "Saudi Arabia"},
    {"start": 0x070000, "end": 0x070FFF, "country": "Senegal"},
    {"start": 0x4C0000, "end": 0x4C7FFF, "country": "Serbia"},
    {"start": 0x074000, "end": 0x0743FF, "country": "Seychelles"},
    {"start": 0x076000, "end": 0x0763FF, "country": "Sierra Leone"},
    {"start": 0x768000, "end": 0x76FFFF, "country": "Singapore"},
    {"start": 0x505C00, "end": 0x505FFF, "country": "Slovakia"},
    {"start": 0x506C00, "end": 0x506FFF, "country": "Slovenia"},
    {"start": 0x897000, "end": 0x8973FF, "country": "Solomon Islands"},
    {"start": 0x078000, "end": 0x078FFF, "country": "Somalia"},
    {"start": 0x008000, "end": 0x00FFFF, "country": "South Africa"},
    {"start": 0x340000, "end": 0x37FFFF, "country": "Spain"},
    {"start": 0x770000, "end": 0x777FFF, "country": "Sri Lanka"},
    {"start": 0x07C000, "end": 0x07CFFF, "country": "Sudan"},
    {"start": 0x0C8000, "end": 0x0C8FFF, "country": "Suriname"},
    {"start": 0x07A000, "end": 0x07A3FF, "country": "Swaziland"},
    {"start": 0x4A8000, "end": 0x4AFFFF, "country": "Sweden"},
    {"start": 0x4B0000, "end": 0x4B7FFF, "country": "Switzerland"},
    {"start": 0x778000, "end": 0x77FFFF, "country": "Syrian Arab Republic"},
    {"start": 0x515000, "end": 0x5153FF, "country": "Tajikistan"},
    {"start": 0x880000, "end": 0x887FFF, "country": "Thailand"},
    {"start": 0x512000, "end": 0x5123FF,
     "country": "Republic of North Macedonia"},
    {"start": 0x088000, "end": 0x088FFF, "country": "Togo"},
    {"start": 0xC8D000, "end": 0xC8D3FF, "country": "Tonga"},
    {"start": 0x0C6000, "end": 0x0C6FFF, "country": "Trinidad and Tobago"},
    {"start": 0x028000, "end": 0x02FFFF, "country": "Tunisia"},
    {"start": 0x4B8000, "end": 0x4BFFFF, "country": "Turkey"},
    {"start": 0x601800, "end": 0x601BFF, "country": "Turkmenistan"},
    {"start": 0x068000, "end": 0x068FFF, "country": "Uganda"},
    {"start": 0x508000, "end": 0x50FFFF, "country": "Ukraine"},
    {"start": 0x896000, "end": 0x896FFF, "country": "United Arab Emirates"},
    # { "start": 0x400000, "end": 0x43FFFF, "country": "United Kingdom" },
    {"start": 0x080000, "end": 0x080FFF,
     "country": "United Republic of Tanzania"},
    # { "start": 0xA00000, "end": 0xAFFFFF, "country": "United States" },
    {"start": 0xE90000, "end": 0xE90FFF, "country": "Uruguay"},
    {"start": 0x507C00, "end": 0x507FFF, "country": "Uzbekistan"},
    {"start": 0xC90000, "end": 0xC903FF, "country": "Vanuatu"},
    {"start": 0x0D8000, "end": 0x0DFFFF, "country": "Venezuela"},
    {"start": 0x888000, "end": 0x88FFFF, "country": "Viet Nam"},
    {"start": 0x890000, "end": 0x890FFF, "country": "Yemen"},
    {"start": 0x08A000, "end": 0x08AFFF, "country": "Zambia"},
    {"start": 0x004000, "end": 0x0043FF, "country": "Zimbabwe"},
    {"start": 0xF00000, "end": 0xF07FFF, "country": "ICAO (temporary)"},
    {"start": 0x899000, "end": 0x8993FF,
     "country": "Taiwan(unofficial) or ICAO (special use)"},
    {"start": 0xF09000, "end": 0xF093FF, "country": "ICAO (special use)"},
    {"start": 0x200000, "end": 0x27FFFF,
     "country": "Rsrvd (ICAO AFI Region)"},
    {"start": 0x280000, "end": 0x28FFFF,
     "country": "Rsrvd (ICAO SAM Region)"},
    {"start": 0x500000, "end": 0x5FFFFF,
     "country": "Rsrvd (ICAO EUR/NAT Region)"},
    {"start": 0x600000, "end": 0x67FFFF,
     "country": "Rsrvd (ICAO MID Region)"},
    {"start": 0x680000, "end": 0x6FFFFF,
     "country": "Rsrvd (ICAO Asia Region)"},
    {"start": 0x900000, "end": 0x9FFFFF,
     "country": "Rsrvd (ICAO NAM/PAC Region)"},
    {"start": 0xB00000, "end": 0xBFFFFF,
     "country": "Rsrvd (ICAO future use)"},
    {"start": 0xEC0000, "end": 0xEFFFFF,
     "country": "Rsrvd (ICAO CAR Region)"},
    {"start": 0xD00000, "end": 0xDFFFFF,
     "country": "Rsrvd (ICAO future use)"},
    {"start": 0xF08000, "end": 0xFFFFFF,
     "country": "Rsrvd (ICAO future use)"},
]
