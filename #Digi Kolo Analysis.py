# Digi Kolo Analysis


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Data provided from the image
data = {
    "Date": ["Feb 21, 2025", "Feb 28, 2025", "Mar 7, 2025", "Mar 14, 2025"],
    "DigiLock": [436200132.80, 431326491.98, 440787872.08, 439661197.43],
    "DigiSave": [26553058.17, 28185489.75, 25027458.96, 25545027.91],
    "DigiTarget": [5468734.91, 5577327.91, 5288509.97, 5377757.21],
    "Total Savings": [468221925.88, 465089459.64, 472103837.03, 471945012.54],
    "Wallet Balance": [27834008.63, 35817824.44, 37950723.48, 38580793.18],
    "Total Balance": [49605934.51, 500907284.08, 510054560.51, 510525805.72],
    "DigiLock Interest": [17938459.32, 18879056.20, 19972531.43, 22780617.43],
    "DigiSave Interest": [9888737.68, 9984123.10, 10042021.10, 10161469.08],
    "DigiTarget Interest": [127526.02, 133285.55, 145720.44, 159443.11],
    "Total Interest": [27954849.29, 28964748.38, 30158424.94, 33011529.82],
    "Expected Liquidation": [19608417.77] * 4  # Same across all weeks
}

# Convert to DataFrame
df = pd.DataFrame(data)
df["Date"] = pd.to_datetime(df["Date"])

# Plot Savings Trends
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="DigiLock", data=df, label="DigiLock", marker="o")
sns.lineplot(x="Date", y="DigiSave", data=df, label="DigiSave", marker="o")
sns.lineplot(x="Date", y="DigiTarget", data=df, label="DigiTarget", marker="o")
sns.lineplot(x="Date", y="Total Savings", data=df, label="Total Savings", marker="o", linewidth=2)
plt.title("DigiKolo Savings Trends (Feb - Mar 2025)")
plt.xlabel("Date")
plt.ylabel("Amount (₦)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Plot Wallet Balance Growth
plt.figure(figsize=(12, 6))
sns.barplot(x="Date", y="Wallet Balance", data=df, palette="Blues_r")
plt.title("Wallet Balance Growth Over Time")
plt.xlabel("Date")
plt.ylabel("Wallet Balance (₦)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()

# Plot Accrued Interest Trends
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="DigiLock Interest", data=df, label="DigiLock Interest", marker="o")
sns.lineplot(x="Date", y="DigiSave Interest", data=df, label="DigiSave Interest", marker="o")
sns.lineplot(x="Date", y="DigiTarget Interest", data=df, label="DigiTarget Interest", marker="o")
sns.lineplot(x="Date", y="Total Interest", data=df, label="Total Interest", marker="o", linewidth=2)
plt.title("DigiKolo Accrued Interest Trends (Feb - Mar 2025)")
plt.xlabel("Date")
plt.ylabel("Interest Earned (₦)")
plt.xticks(rotation=45)
plt.legend()
plt.grid(True)
plt.show()

# Expected Liquidation Insights
plt.figure(figsize=(8, 4))
sns.barplot(x=df["Date"], y=df["Expected Liquidation"], palette="Reds_r")
plt.title("Expected Liquidation for the Week")
plt.xlabel("Date")
plt.ylabel("Amount (₦)")
plt.xticks(rotation=45)
plt.grid(axis="y")
plt.show()
