from datetime import datetime
from zoneinfo import ZoneInfo



def convert_class_time(ist_datetime_str, target_timezone_str):
    try:
        ist_datetime = datetime.fromisoformat(ist_datetime_str)
        target_tz = ZoneInfo(target_timezone_str)
        return ist_datetime.astimezone(target_tz).isoformat()
    except Exception as e:
        return ist_datetime_str