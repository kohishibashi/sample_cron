from datetime import datetime
import pathlib

dt_now = datetime.now()
now_time_str = dt_now.strftime('%Y%m%d%H%M%S')

log_path = pathlib.Path("/Users/dev/sample_cron/log")
file_path = log_path.joinpath(f'{now_time_str}.txt')
print(f'【cron】 {now_time_str}')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(now_time_str)
