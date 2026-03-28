# 📊 cyber-project-06-siem-simulation
SIEM simulation with log correlation and attack detection


## Context

SIEM systems collect and analyze logs to detect security incidents.

This project simulates log correlation to identify a potential compromise.

---

## Objective

* Correlate multiple events
* Detect attack patterns
* Simulate SIEM logic

---

## 🔍 Events

```id="3mrldq"
LOGIN FAILED - admin - 45.33.32.1
LOGIN FAILED - admin - 45.33.32.1
LOGIN SUCCESS - admin - 45.33.32.1
FILE ACCESS - sensitive_data.txt
```

---

## Analysis

### Step 1: Failed Logins

* Multiple failed attempts detected

### Step 2: Successful Login

* Indicates brute force success

### Step 3: Sensitive File Access

* Potential data compromise

---

## Conclusion

This sequence indicates a **confirmed account compromise**.

---

## Recommendations

* Block the IP address
* Reset credentials
* Monitor file access activity

---

## Key Takeaways

* Event correlation
* SIEM logic
* Threat detection workflow

---

## 👨‍💻 Author

Part of my cybersecurity learning journey.
