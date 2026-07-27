import shutil

print("=" * 30)
print(" STORAGE ANALYZER ")
print("=" * 30)

total, used, free = shutil.disk_usage("/")

print(f"\nTotal Space: {total // (1024**3)} GB")
print(f"Used Space : {used // (1024**3)} GB")
print(f"Free Space : {free // (1024**3)} GB")
