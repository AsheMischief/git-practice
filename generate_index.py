import os
import glob

# Find all dashboard files, most recent first
dashboard_files = sorted(glob.glob("dashboard_*.html"), reverse=True)

links = "\n".join(
    f'<li><a href="{filename}">{filename}</a></li>' for filename in dashboard_files
)

html = f"""<!DOCTYPE html>
<html>
<head>
  <title>UAT Dashboard History</title>
</head>
<body>
  <h1>UAT Dashboard Runs</h1>
  <p>{len(dashboard_files)} dashboard(s) generated so far.</p>
  <ul>
    {links}
  </ul>
</body>
</html>
"""

with open("index.html", "w") as f:
    f.write(html)

print(f"Index page updated with {len(dashboard_files)} dashboards")