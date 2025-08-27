import os
import json
from datetime import datetime, timedelta

def main() -> None:
    today = datetime.now()
    tomorrow = today + timedelta(days=1)

    today_str = today.strftime("%d.%m.%y")
    tomorrow_str = tomorrow.strftime("%d.%m.%y")

    schedule_path = os.path.expanduser("~/.config/waybar/waybar-schedule-module/schedule.json")

    with open(schedule_path, "r", encoding="utf-8") as f:
        schedule = json.load(f)

    data = ""

    if today_str in schedule:
        data += f"Сегодня (<u>{today_str}</u>):\n{schedule[today_str]}"
    else:
        data += f"На сегодня ({today_str}) расписание не известно."

    if tomorrow_str in schedule:
        data += f"\n\nЗавтра (<u>{tomorrow_str}</u>):\n{schedule[tomorrow_str]}"
    else:
        data += f"\n\nНа завтра ({tomorrow_str}) расписание не известно."

    output = {
        "text": "<",
        "tooltip": data,
    }

    print(json.dumps(output, ensure_ascii=False))


if __name__ == "__main__":
    main()