import csv
from pathlib import Path

def validate(rows):
    seen = set()
    results = []
    for row in rows:
        errors = []
        employee_id = row["employee_id"].strip()
        if not employee_id:
            errors.append("Missing employee ID")
        if employee_id in seen:
            errors.append("Duplicate ID")
        seen.add(employee_id)
        if "@" not in row["email"]:
            errors.append("Invalid email")
        if not row["department"].strip():
            errors.append("Missing department")
        results.append({
            **row,
            "status":"Exception" if errors else "Ready",
            "reason":"; ".join(errors)
        })
    return results

if __name__ == "__main__":
    with open("data/employees.csv",newline="") as f:
        results = validate(csv.DictReader(f))
    Path("output").mkdir(exist_ok=True)
    with open("output/report.csv","w",newline="") as f:
        writer = csv.DictWriter(f,fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print("Validation report created.")
