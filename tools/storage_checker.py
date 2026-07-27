import shutil

print("=" * 30)
print(" STORAGE ANALYZER ")
print("=" * 30)

total, used, free = shutil.disk_usage("/")

total_gb = total // (1024 ** 3)
used_gb = used // (1024 ** 3)
free_gb = free // (1024 ** 3)

usage_percent = (used / total) * 100

print(f"\nTotal Space : {total_gb} GB")
print(f"Used Space  : {used_gb} GB")
print(f"Free Space  : {free_gb} GB")
print(f"Usage       : {usage_percent:.1f}%")

if usage_percent >= 90:
    print("\nWarning: Storage is almost full!")
elif usage_percent >= 75:
    print("\nNotice: Storage usage is high.")
else:
    print("\nStorage status is healthy.")
