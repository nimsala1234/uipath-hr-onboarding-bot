# HR Onboarding Automation Bot

Prototype with synthetic employee data and a working
Python reference implementation of the validation rules.

## Run reference implementation
python validate.py

## UiPath Studio implementation (not yet created)
1. Create a Windows Process named HROnboarding.
2. Convert data/employees.csv to employees.xlsx.
3. Install UiPath.Excel.Activities.
4. Use Excel File -> Read Range.
5. For Each Row in Data Table:
   - Validate required fields.
   - Track IDs with HashSet(Of String).
   - Detect duplicate IDs and malformed email addresses.
   - Assign Ready or Exception status.
6. Write results with Write DataTable to Excel.
7. Add Try Catch and Log Message activities.
8. Run and compare output with the reference report.
9. Commit the actual UiPath project including Main.xaml,
   project.json and supporting workflows.

Status: Python reference implementation only.
The native UiPath workflow must be implemented and tested in Studio.
Never use real employee records in the public repository.
