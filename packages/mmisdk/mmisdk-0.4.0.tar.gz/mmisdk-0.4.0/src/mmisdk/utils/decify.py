from typing import Optional
from mmisdk.common.hex_string import HexString
from mmisdk.common.dec_string import DecString


def decify(hex_string: Optional[HexString]) -> Optional[DecString]:
    """
    Converts a hexadecimal string to its decimal representation. Support None input.
    """
    return str(int(hex_string, 16)) if hex_string is not None else None
