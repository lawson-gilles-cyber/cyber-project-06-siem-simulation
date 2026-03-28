logs = [
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN FAILED - admin - 45.33.32.1",
    "LOGIN SUCCESS - admin - 45.33.32.1",
    "FILE ACCESS - sensitive_data.txt"
]

failed_logins = 0
successful_login = False
file_access = False

for log in logs:
    if "LOGIN FAILED" in log:
        failed_logins += 1

    if "LOGIN SUCCESS" in log:
        successful_login = True

    if "FILE ACCESS" in log:
        file_access = True

print("=== SIEM Analysis Report ===\n")

if failed_logins >= 2 and successful_login and file_access:
    print("[ALERT] Possible account compromise detected\n")
else:
    print("No critical threat detected\n")
