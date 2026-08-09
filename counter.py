from pathlib import Path
import subprocess

REPO = Path.home() / "github-counter"
COUNTER_FILE = REPO / "counter.txt"

# Read current counter
with open(COUNTER_FILE, "r") as f:
    counter = int(f.read().strip())

# Increment counter
counter += 1

# Write new counter
with open(COUNTER_FILE, "w") as f:
    f.write(str(counter) + "\n")

# Commit and push
subprocess.run(["git", "add", "counter.txt"], cwd=REPO, check=True)

subprocess.run(
    ["git", "commit", "-m", f"Update counter to {counter}"],
    cwd=REPO,
    check=True
)

subprocess.run(
    ["git", "push"],
    cwd=REPO,
    check=True
)

print(f"Counter updated to {counter}")
