from dataclasses import dataclass
from typing import Optional

from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class Conf:
    # here is should be same content as in __init__.py
    bot_token: str
    log_file: str
    debug: bool
    db_uri: str
    stdout_log: Optional[bool] = False
    sql_log: Optional[bool] = False
    tele_proxy: Optional[str] = None
    root_dir: Optional[str] = None
