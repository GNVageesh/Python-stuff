import time
import sys
from plyer import notification

# while True:
try:
    notification.notify(
        title="Hello vageesh",
        app_name="Dot Bot",
        message="I am bot",
        # app_icon
        ticker=".bot",
        toast=True,
        timeout=2
    )
    time.sleep(2)
except KeyboardInterrupt:
    print("Thanks for using . bot")
    sys.exit()
