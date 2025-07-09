patients = [
    {
        'name': 'Alice', 
        'age': 30, 
        'weight': 60, 
        'dosages': [
            {'time': '08:00', 'dose': 10},
            {'time': '12:00', 'dose': 40},
        ]
    },
    {
        'name': 'Bob', 
        'age': 16, 
        'weight': 40, 
        'dosages': [
            {'time': '08:00', 'dose': 5},
            {'time': '12:00', 'dose': 15}
        ]
    }
]

def safe_range(age, weight):
    if age >= 18:
        return (0.1 * weight, 0.5 * weight)
    else:
        return (0.05 * weight, 0.3 * weight)
     
def  check_dose_status(dose, min_dose, max_dose):
    if dose <= 0:
        return "invalid"
    elif min_dose <= dose <= max_dose:
        return "safe"
    else:
        return "Unsafe"
    
for patient in patients:
    print(f"patient: {patient['name']} (Age: {patient['age']}, weight: {patient['weight']} kg)")
    min_dose, max_dose = safe_range(patient['age'], patient['weight'])
    valid_count = 0

    for record in patient['dosages']:
        dose = record['dose']
        status = check_dose_status(dose, min_dose, max_dose)
        print(f" Time:{record['time']}, dose:{dose} mg, {status}")
        if status != "Invalid":  
            valid_count +=1
        print(f"Total valid doses: {valid_count}")