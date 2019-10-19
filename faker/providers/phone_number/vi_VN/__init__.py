# coding=utf-8

from .. import Provider as PhoneNumberProvider


# https://quantrimang.com/danh-sach-dau-so-cac-mang-di-dong-o-viet-nam-133203

class Provider(PhoneNumberProvider):
    """Phone number generator for Vietnamese locale"""
    formats = (
        # Viettel
        r"086%%%%%%%",
        r"096%%%%%%%",
        r"097%%%%%%%",
        r"098%%%%%%%",
        r"032%%%%%%%",
        r"033%%%%%%%",
        r"034%%%%%%%",
        r"035%%%%%%%",
        r"036%%%%%%%",
        r"037%%%%%%%",
        r"038%%%%%%%",
        r"039%%%%%%%",
        # Mobifone
        r"089%%%%%%%",
        r"090%%%%%%%",
        r"093%%%%%%%",
        r"070%%%%%%%",
        r"079%%%%%%%",
        r"077%%%%%%%",
        r"076%%%%%%%",
        r"078%%%%%%%",
        # Vinaphone
        r"088%%%%%%%",
        r"091%%%%%%%",
        r"094%%%%%%%",
        r"083%%%%%%%",
        r"084%%%%%%%",
        r"085%%%%%%%",
        r"081%%%%%%%",
        r"082%%%%%%%",
        # Vietnamobile
        r"092%%%%%%%",
        r"056%%%%%%%",
        r"058%%%%%%%",
        # Gmobile
        r"099%%%%%%%",
        r"059%%%%%%%",
    )
