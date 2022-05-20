period = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7
for i in range(1, period + 1):
    number_patients = int(input())
    if i % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    if number_patients <= doctors:
        treated_patients += number_patients
    if number_patients > doctors:
        treated_patients += doctors
        untreated_patients += number_patients - doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")