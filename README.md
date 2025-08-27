# никому не нужный waybar-модуль для отображения расписания алтгту

## пререквизитс:
```python3```

```waybar```

```cron```

## куикстарт:

1. https://www.altstu.ru/m/s/, найти нужную группу и скопировать юрл
2. настроить окружение
```bash
cd ~/.config/waybar
git clone https://github.com/vostralis/waybar-schedule-module
cd waybar-schedule-module
python3 -m venv venv
pip install -r requirements.txt
chmod +x ./run.sh
echo 'URL = "ссылка на группу"' > .env
```

3. вручную первый раз скрапнуть расписание
```bash
./run.sh -f
```
4. настроить фетч расписания
```bash
crontab -e
```
и вставить
```bash
@reboot ~/.config/waybar/waybar-schedule-module/run.sh -f
```

5. добавить модуль в ```~/.config/waybar/config.jsonc```:
```json
"custom/schedule": {
    "format": "<big>{}/big>",
    "tooltip": true,
    "return-type": "json",
    "interval": 43200,
    "exec": "$HOME/.config/waybar/waybar-schedule-module/run.sh -d"
}
```