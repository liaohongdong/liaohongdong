import random
from datetime import datetime
import re

# 生成随机时间（周一至周五）
hour = random.randint(0,  23)
minute = random.randint(0,  59)
weekday = random.randint(1,  7)  # 1-5 对应周一至周五

# 生成 cron 表达式 
if weekday <= 5:
  cron_expr = f"{minute} {hour} * * *"
else:
  cron_expr = f"{minute} {hour} 1 * *"
print(f"New cron: {cron_expr}")

# 写入工作流文件（需替换为实际路径）
with open(".github/workflows/ci.yml",  "r+") as f:
    content = f.read() 
    new_content = re.sub(r'(- cron:\s*").*?(")', r'- cron: "' + cron_expr + r'"', content)
    f.seek(0) 
    f.write(new_content) 
    f.truncate() 
