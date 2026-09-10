import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("raw_data.csv")
print("---🔴RAW MESSY DATA---")
print(df)

# ==========================================
# 🟢 STEP 2: DUPLICATE ROWS KO CLEAN KARNA
# ==========================================

df = df.drop_duplicates()
print("\n--- 🟢 AFTER REMOVING DUPLICATES ---")
print(df)

# ==========================================
# 🟡 STEP 3: MISSING DATA (NaN) CLEAN KARNA
# ==========================================


df['Department'] = df['Department'].fillna('Unassigned')

df['Age'] = df['Age'].fillna(df['Age'].mean())

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())

print("\n--- 🟢 AFTER FILLING MISSING VALUES ---")
print(df)

# ==========================================
# 🔵 STEP 4: CLEANED DATA EXPORT KARNA
# ==========================================
df.to_csv("cleaned_data.csv", index=False)
print("\n✅ Cleaned data successfully exported to 'cleaned_data.csv'!")


# ==========================================
# 📊 STEP 5: VISUAL SUMMARY CHART GENERATE KARNA
# ==========================================

dept_salary = df.groupby('Department')['Salary'].mean()

plt.figure(figsize=(8, 5))
dept_salary.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Average Salary by Department', fontsize=14, fontweight='bold')
plt.xlabel('Department', fontsize=12)
plt.ylabel('Average Salary ($)', fontsize=12)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('department_salary_report.png')
print("📈 Visual summary chart saved as 'department_salary_report.png'!")