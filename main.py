# ===================================
# DataMed
# ===================================
# Developed by. Ferdio Giffary
# JCDS - BSDAM29


# /************************************/

# DataMed -- Patient Data
# for optimalization & cleaner data, we restrict some of data to:
# 10 Medical Condition (med_con) into 5 Department (2 med_con for each department) and 5 doctors (1 for each department) as follows:
# Physio            = Injuries, Osteoporosis    = Dr. Bayu
# Endocrinologists  = Diabetes, Obesity         = Dr. Steven
# Neurologist       = Parkinson, Alzheimer      = Dr. Kristina
# Cardiologist      = Hypertention, Stroke      = Dr. Bobby
# General           = Asthma, Pneumonia         = Dr. Elbert

# This is EXAMPLE DATA provided solely for educational purposes.
# Note: 

from datetime import datetime, date
# Define valid mapping based on  conditions above ^
# dict of dict --> nested mapping
department_avail = {
    "Physio":           {"conditions": ["Injuries", "Osteoporosis"],"doctor": "Dr. Bayu"},
    "Endocrinologists": {"conditions": ["Diabetes", "Obesity"],     "doctor": "Dr. Steven"},
    "Neurologist":      {"conditions": ["Parkinson", "Alzheimer"],  "doctor": "Dr. Kristina"},
    "Cardiologist":     {"conditions": ["Hypertension", "Stroke"],  "doctor": "Dr. Bobby"},
    "General":          {"conditions": ["Asthma", "Pneumonia"],     "doctor": "Dr. Elbert"}}

# /===== Data Model =====/
# data mostly from https://www.kaggle.com/datasets/prasad22/healthcare-dataset?resource=download&select=healthcare_dataset.csv
# dictionary of list
patient = { 
    "patient_id"        : ["1998021001","1969022002","1999011003","2002110004","1988101005",],
    "Identity ID (KTP)" : [3674020379555407,3674264820182635,3456102836458876,1234567891011120,8012246780900001],
    "last_name"         : ["giffary","jackson","terry","smith","watts"],
    "first_name"        : ["ferdio","bobby","leslie","danny","andrew"],
    "date_of_birth"     : ["1998-03-07","1969-07-04","1999-12-12","2002-01-28","1988-05-15"],
    "age"               : [25,55,24,23,37],
    "gender"            : ["male","male","male","female","female"],
    "blood_type"        : ["b+","b-","a+","a-","o+"],
    "inpatient_status"  : [],
    "inpatient_count"   : []
}
#list of dict
inpatients = [
    {   "inpatient_id"  : "INP001",
        "patient_id"    : "1998021001",
        "date_adm"      : "2025-01-04",
        "date_disch"    : "2025-01-05",
        "room_number"   : "1",
        "med_con"       : "injuries",
        "adm_type"      : "elective",
        "department"    : "physio",
        "doctor"        : "bayu",
        "insurance"     : "jiwasraya",
        "bill_id"       : "101",
        "bill_amount"   : "1500000"
        },
    {   "inpatient_id"  : "INP002",
        "patient_id"    : "1969022002",
        "date_adm"      : "2025-02-02",
        "date_disch"    : "2025-02-04",
        "room_number"   : "1",
        "med_con"       : "parkinson",
        "adm_type"      : "urgent",
        "department"    : "neurologist",
        "doctor"        : "kristina",
        "insurance"     : "blue cross",
        "bill_id"       : "102",
        "bill_amount"   : "40000000"
        },
    {   "inpatient_id"  : "INP003",
        "patient_id"    : "1999011003",
        "date_adm"      : "2025-07-22",
        "date_disch"    : "2025-07-28",
        "room_number"   : "2",
        "med_con"       : "alzheimer",
        "adm_type"      : "emergency",
        "department"    : "neurologist",
        "doctor"        : "kristina",
        "insurance"     : "medicare",
        "bill_id"       : "103",
        "bill_amount"   : "16500000"
        },
    {   "inpatient_id"  : "INP004",
        "patient_id"    : "2002110004",
        "date_adm"      : "2025-08-01",
        "date_disch"    : "2025-08-08",
        "room_number"   : "3",
        "med_con"       : "pneumonia",
        "adm_type"      : "emergency",
        "department"    : "general",
        "doctor"        : "elbert",
        "insurance"     : "aetna",
        "bill_id"       : "104",
        "bill_amount"   : "20000000"
        },
    {   "inpatient_id"  : "INP005",
        "patient_id"    : "1988101005",
        "date_adm"      : "025-08-10",
        "date_disch"    : None,
        "room_number"   : "4",
        "med_con"       : "injuries",
        "adm_type"      : "elective",
        "department"    : "physio",
        "doctor"        : "bayu",
        "insurance"     : "medicare",
        "bill_id"       : "105",
        "bill_amount"   : "45000000"
        },
    {   "inpatient_id"  : "INP006",
        "patient_id"    : "1998021001",
        "date_adm"      : "2025-09-01",
        "date_disch"    : None,
        "room_number"   : "5",
        "med_con"       : "pneumonia",
        "adm_type"      : "elective",
        "department"    : "general",
        "doctor"        : "elbert",
        "insurance"     : "jiwasraya",
        "bill_id"       : "106",
        "bill_amount"   : "200000"},
]
# statement for checking-out patient to make sure inpatient status & count not empty

if len(patient["inpatient_status"]) == 0:
    for i in range(len(patient["patient_id"])):
        patient["inpatient_status"].append("No")

if len(patient["inpatient_count"]) == 0:
    for i in range(len(patient["patient_id"])):
        patient["inpatient_count"].append(0)

# global var for bill_id (right now starting at 106)
bill_counter = 107

# Function Menu 1 No 1 --> show_patient
# =======================================
def show_patient():
    print("\n============ Patient List ============")
    print("--------------------------------------")
    print(f"{'Patient ID':<12}|{'First Name':<12}|{'Last Name':<12}|")
    print("--------------------------------------")
    index = len(patient["patient_id"])
    for i in range(index):
        print(f"{patient['patient_id'][i].upper():<12}|{patient['first_name'][i].upper():<12}|{patient['last_name'][i].upper():<12}|")
    print("--------------------------------------")

    while True:
        show_detail = input("\n1. Show patient detail\n2. Back to main menu\nChoose menu: ")
        if show_detail == "1":
            detail_id = input("Enter patient ID: ").strip()
            if detail_id in patient["patient_id"]:
                show_details(detail_id)
            else:
                print("Patient ID not found.")
        elif show_detail == "2":
            print("\nBack to main menu")
            break
        else:
            print("\nUnrecognized input, try again!")


# Function Menu 1 No 2 --> show_details
# =======================================
def show_details(detail_id):
    detail_index = patient["patient_id"].index(detail_id)
    print("\n============ Patient Detail ============")
    print("--------------------------------------")
    print(f"Patient ID          : {patient['patient_id'][detail_index].upper()}")
    print(f"First Name          : {patient['first_name'][detail_index].upper()}")
    print(f"Last Name           : {patient['last_name'][detail_index].upper()}")
    print(f"Age                 : {patient['age'][detail_index]} YEARS OLD")
    print(f"Gender              : {patient['gender'][detail_index].upper()}")
    print(f"Blood Type          : {patient['blood_type'][detail_index].upper()}")
    print("--------------------------------------")

    choice = input("\nView inpatient details for this patient? (y/n): ").strip().lower()
    if choice == "y":
        show_inpatient_details(detail_id)
        print("\nReturn to previous menu")
    elif choice =="n":
        print("\nReturn to previouys menu")
    else:
        print("\nUnrecognized input, return to previouys menu")

# Function Menu 1 No 3 --> show_inpatient_details
# =======================================
def show_inpatient_details(patient_id):
    print("\n========= Inpatient Records =========")
    found = False
    for record in inpatients:  
        if record["patient_id"] == patient_id:
            found = True
            print("--------------------------------------")
            print(f"Inpatient ID   : {record['inpatient_id']}")
            print(f"Room number    : {record['room_number']}")
            print(f"Medical cond.  : {record['med_con'].upper()}")
            print(f"Admission type : {record['adm_type'].upper()}")
            print(f"Date admitted  : {record['date_adm']}")
            print(f"Date discharge : {record['date_disch']}")
            print(f"Department     : {record['department'].upper()}")
            print(f"Doctor         : {record['doctor'].upper()}")
            print(f"Insurance      : {record['insurance'].upper()}")
            print(f"Bill ID        : {record['bill_id']}")
            print(f"Bill amount    : Rp.{record['bill_amount']},-")
            print("--------------------------------------")
    if not found:
        print("No inpatient records found for this patient.")
    

# Function Menu 2 No 1 --> find_patient
# =======================================
def find_patient():
    print("\n============ Find Patient ==============")
    print("--------------------------------------")
    while True:
        search = input("1. Find by patient ID\n2. Find by patient name\n3. Return to main Menu\nChoose menu: ")
        
        if search == "1":
            search_id = input("\nInput patient ID: ").lower()
            found = False
            for index in range(len(patient["patient_id"])):
                if search_id in patient["patient_id"][index].lower():
                    if not found:
                        print("\nPatient(s) Found by ID!\n")
                    show_details(patient["patient_id"][index])
                    found = True
            if not found:
                print("\nNo Patient ID found\n")
        
        elif search == "2":
            search_name = input("\nInput patient first or last name: ").lower()
            found = False
            for index in range(len(patient["patient_id"])):
                if (search_name in patient["first_name"][index].lower() or 
                    search_name in patient["last_name"][index].lower()): #partial
                    if not found:
                        print("\nPatient(s) Found by name!\n")
                    show_details(patient["patient_id"][index])
                    found = True
            if not found:
                print("\nNo patient name found\n")
        
        elif search == "3":
            print("\nBack to main menu")
            break
        
        else:
            print("\nUnrecognized input, try again!")

# Function Menu 3 No 1 --> add_patient
# =======================================
def add_patient():
    print("\n============ Add New Patient =============")
    
    # Mini function for calculate age (date right now - date of birth)
    def calculate_age(tgl_str):
        tgl = datetime.strptime(tgl_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        age = today.year - tgl.year - ((today.month, today.day) < (tgl.month, tgl.day))
        return age

    # Validate No KTP
    while True:
        ktp = input("KTP (16 digits, and cannot start with 0): ").strip()
        if not ktp.isdigit() or len(ktp)!= 16 or ktp[0]== "0":
            print("KTP must be exactly 16 digits and not start with 0, try again")
        else:
            break

    #Validate First Name
    while True:
        first_name = input("First name: ").strip()
        if not first_name.isalpha():
            print("First name must only contain letters, try again.")
        else:
            break

    #Validate Last Name
    while True:
        last_name = input("Last name: ").strip()
        if not last_name.isalpha():
            print("Last name must only contain letters. Try again.")
        else:
            break

    # Validate Birth Date
    while True:
        date_of_birth = input("Date of birth (YYYY-MM-DD): ").strip()
        try:
            date_of_birth = datetime.strptime(date_of_birth, "%Y-%m-%d")
            break
        except ValueError:
            print("Unrecognized date format. Use YYYY-MM-DD.")

    # Calculate Age
    age = calculate_age(date_of_birth)

    # Validate Gender
    while True:
        gender = input("Gender (male/female): ").strip().capitalize()
        if gender not in ["Male", "Female"]:
            print("Gender must be 'Male' or 'Female'. Try again.")
        else:
            break

    # Validate Blood Type
    valid_blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
    while True:
        blood_type = input("Blood type (A+, A-, B+, B-, AB+, AB-, O+, O-): ").strip().upper()
        if blood_type not in valid_blood_types:
            print("Invalid blood type. choose from:", ", ".join(valid_blood_types))
        else:
            break
    # Mini function for generate patient ID = 
    # 1st - 4th --> Year of birth
    # 5th       --> Gender (0 = Male, 1 = Female)
    # 6th       --> Blood Type (0 = O, 1 = A, 2 = B, 3 = AB)
    # 7th       --> Rhesus (0 = -, 1 = +)
    # 8th - 10th--> Generated
    
    def generate_patient_id(date_of_birth, gender, blood_type, serial):
        year = date_of_birth.split("-")[0]
        gender_digit = "0" if gender.lower() == "male" else "1"
        bt = blood_type.lower()
        if "ab" in bt:
            blood_digit = "3"
        elif bt.startswith("a"):
            blood_digit = "1"
        elif bt.startswith("b"):
            blood_digit = "2"
        elif bt.startswith("o"):
            blood_digit= "0"
        else:
            raise ValueError ("Unknown blood type")

        rhesus_digit = "1" if "+" in bt else "0"
        serial_digit = str(serial).zfill(3) #zfill --> fill serial number to a string to reach () length

        return year + gender_digit + blood_digit + rhesus_digit + serial_digit
    
    # Generate unique patient ID
    serial = len(patient["patient_id"])+ 1
    new_id = generate_patient_id(date_of_birth, gender, blood_type, serial)

    # Append the Data
    patient["patient_id"].append(new_id)
    patient["Identity ID (KTP)"].append(ktp)
    patient["first_name"].append(first_name)
    patient["last_name"].append(last_name)
    patient["date_of_birth"].append(date_of_birth)
    patient["age"].append(age)
    patient["gender"].append(gender)
    patient["blood_type"].append(blood_type)

    # Auto-assign inpatient info
    patient["inpatient_status"].append("No")
    patient["inpatient_count"].append(0)

    print("\nPatient added successfully!")
    print(f"Assigned patient ID : {new_id}")
    print(f"Inpatient status    : No")
    print(f"Inpatient count     : 0")

# Function Menu 4 No 1 --> update_patient
# =======================================
def update_patient():
    print("\n============ Update Patient =============")
    update_id = input("Enter patient ID to update: ").strip()

    if update_id not in patient["patient_id"]:
        print("Patient ID not found.")
        return
    
    index = patient["patient_id"].index(update_id)
    print(f"\nPatient found: {patient['first_name'][index]} {patient['last_name'][index]}")

    # Only allow some fields to be updated
    updatable_fields = ["first_name", "last_name", "date_of_birth", "Identity ID (KTP)", "blood_type"]
    
    print("\nWhich field do you want to update?")
    for i, key in enumerate(updatable_fields, start=1):
        print(f"{i}. {key.replace('_', ' ').capitalize()}")
    print(f"{len(updatable_fields)+1}. Cancel")

    choice = input("Choose option: ").strip()
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(updatable_fields)+1:
        print("Invalid choice.")
        return
    
    choice = int(choice)
    if choice == len(updatable_fields)+1:
        print("Update cancelled.")
        return
    
    field = updatable_fields[choice-1]

    # ask new value
    new_value = input(f"Enter new value for {field.replace('_', ' ').capitalize()}: ").strip()

    # apply validation rules
    if field in ["first_name", "last_name"]:
        if not new_value.isalpha():
            print(f"{field.replace('_', ' ').capitalize()} must only contain letters.")
            return
    elif field == "date_of_birth":
        try:
            datetime.strptime(new_value, "%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Use YYYY-MM-DD.")
            return
    elif field == "Identity ID (KTP)":
        if not new_value.isdigit() or len(new_value) != 16 or new_value[0] == "0":
            print("KTP must be exactly 16 digits and not start with 0.")
            return
    elif field == "blood_type":
        valid_blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
        if new_value.upper() not in valid_blood_types:
            print("Invalid blood type.")
            return
        new_value = new_value.upper()

    # apply update
    patient[field][index] = new_value
    print(f"{field.replace('_', ' ').capitalize()} updated successfully.")

# Function Menu 5 No 1 --> delete_patient
# =======================================
def delete_patient():
    print("\n============ Delete Patient =============")
    delete_id = input("Enter patient ID to delete: ").strip()

    if delete_id not in patient["patient_id"]:
        print("Patient ID not found. Return to main menu")
        return
        
    idx = patient["patient_id"].index(delete_id)
    confirm = input(f"Are you sure you want to delete patient {patient['first_name'][idx].upper()} {patient['last_name'][idx].upper()}? (y/n): ").strip().lower()
    if confirm != "y":
        print("Delete cancelled. Back to main menu")
        return

    # remove patient from every field
    for key in patient.keys():
        del patient[key][idx]

    print("Patient deleted successfully.")

# Function Menu 7 No 1 --> check_in
# =======================================
def check_in():
    print("\n============ Patient Check-In ============")
    pid = input("Enter patient ID for check-in: ").strip()

    # Make sure patient exists
    if pid not in patient["patient_id"]:
        print("Patient ID not found!")
        return
    
    active_inpatient = next((rec for rec in inpatients if rec["patient_id"] == pid and rec["date_disch"] is None), None)
    if active_inpatient:
        print(f"Patient {pid} is already admitted (Inpatient ID: {active_inpatient['inpatient_id']}, Room {active_inpatient['room_number']}).")
        return

    # Collect input
    room_avail = 12 #----> for example
    occupied_rooms = [rec["room_number"] for rec in inpatients if rec["date_disch"] is None]
    available_rooms = [str(r) for r in range(1, room_avail + 1) if str(r) not in occupied_rooms]

    if not available_rooms:
        print("No rooms available at the moment. check-in cannot proceed.")
        return

    print(f"\nAvailable rooms: {', '.join(available_rooms)}")

    while True:
        room_number = input("Choose room number: ").strip()
        if room_number in available_rooms:
            break
        else:
            print(f"Invalid choice. available rooms are: {', '.join(available_rooms)}")


    valid_adm_types = ["Emergency", "Elective", "Urgent"]
    while True:
        adm_type = input("Enter admission Type (Emergency/Elective/Urgent): ").strip().capitalize()
        if adm_type not in valid_adm_types:
            print("Invalid input. must be Emergency, Elective, or Urgent.")
        else:
            break

    print("\nAvailable departments:")
    for dep in department_avail.keys():
        print(f"- {dep}")

# Validate department
    while True:
        department = input("Enter department: ").strip().capitalize()
        if department in department_avail:
            break
        else:
            print("Invalid department, please choose again.")

# Validate medical condition based on department
    allowed_conditions = department_avail[department]["conditions"]
    print(f"\nAllowed conditions for {department}: {', '.join(allowed_conditions)}")

    while True:
        med_con = input("Enter medical condition: ").strip().capitalize()
        if med_con in allowed_conditions:
            break
        else:
            print(f"Invalid condition. Allowed for {department}: {', '.join(allowed_conditions)}")

# Show available doctors (even though only 1 per department)
    doctor_name = department_avail[department]["doctor"]
    available_doctors = [doctor_name.replace("Dr. ", "").lower()]  # → bayu, steven, etc.
    print(f"\nAvailable doctors in {department}: {', '.join([doc.capitalize() for doc in available_doctors])}")

    # Let user choose doctor
    while True:
        doctor_input = input("Choose doctor: ").strip().lower()
        if doctor_input in available_doctors:
            doctor = doctor_input
            break
        else:
            print(f"Invalid doctor. Available: {', '.join([doc.capitalize() for doc in available_doctors])}")

    insurance = input("Enter Insurance: ").strip().capitalize()

    # Mini function for generate bill_id
    def generate_billing_id():
        global bill_counter
        bill_id = f"BILL{bill_counter}"
        bill_counter += 1
        return bill_id

    bill_id = generate_billing_id()

    while True:
        bill_amount = input("Enter Bill Amount: ").strip()
        if not bill_amount.isdigit():
            print("Billing Amount must be a number. Try again.")
        elif int(bill_amount) < 100000:
            print("Billing Amount must be at least Rp. 100000. Try again.")
        else:
            bill_amount = str(int(bill_amount))
            break

    # Create new inpatient record
    new_inpatient_id = f"INP{len(inpatients)+1:03d}"
    today = datetime.today().strftime("%Y-%m-%d")

    new_inpatient = {
        "inpatient_id"  : new_inpatient_id,
        "patient_id"    : pid,
        "room_number"   : room_number,
        "med_con"       : med_con,
        "adm_type"      : adm_type,
        "date_adm"      : today,
        "date_disch"    : None,
        "department"    : department,
        "doctor"        : doctor,
        "insurance"     : insurance,
        "bill_id"       : bill_id,
        "bill_amount"   : bill_amount
    }

    inpatients.append(new_inpatient)

    # Confirmation
    print(f"\nPatient {pid} successfully checked in!")
    print(f"   Inpatient ID : {new_inpatient_id}")
    print(f"   Room Number  : {room_number}")
    print(f"   Doctor       : {doctor}")
    print(f"   Bill ID      : {bill_id} (Rp.{bill_amount},-)")

# Function Menu 8 No 1 --> check_out
# =======================================
def check_out(inpatient_id):
    for record in inpatients:
        if record["inpatient_id"] == inpatient_id:
            if record["date_disch"] is not None:
                print(f"Inpatient {inpatient_id} has already been discharged on {record['date_disch']}.")
                return
            
            record["date_disch"] = str(date.today())
            
            # Auto-update patient status
            pid = record["patient_id"]
            index = patient["patient_id"].index(pid)
            patient["inpatient_status"][index] = "No"
            
            print(f"\nInpatient {inpatient_id} successfully checked out.")
            print(f"   Patient {pid} status updated → No")
            return
    
    print(f"Inpatient ID {inpatient_id} not found.")

# Function Menu 6 No 1 --> view_logs
# =======================================
def view_logs():
    print("\n============ Inpatient Logs ============")
    if not inpatients:
        print("No inpatient records available.")
        return
    
    # Count active inpatients
    active_inpatients = [rec for rec in inpatients if rec["date_disch"] in [None, "", "N/A"]]
    print(f"Active Inpatients: {len(active_inpatients)}")

    if active_inpatients:
        print("\n--- Active Inpatient List ---")
        for rec in active_inpatients:
            print(f" Inpatient ID: {rec['inpatient_id']} | "
                  f"Patient ID: {rec['patient_id']} | "
                  f"Room: {rec['room_number']} | "
                  f"Admitted: {rec['date_adm']}")

    # Show history logs
    print("\n--- Admission / Discharge History ---")
    for rec in inpatients:
        print(f" Inpatient ID: {rec['inpatient_id']} | "
              f"Patient ID: {rec['patient_id']} | "
              f"Check-in: {rec['date_adm']} | "
              f"Check-out: {rec['date_disch'] if rec['date_disch'] else 'Still Admitted'}")

    print("--------------------------------------")

# MAIN MENU

while True:
    print("\nWelcome to DataMed!")
    print("\n============== Main Menu =============")
    print("--------------------------------------")
    print("1. Show Patient List\n2. Find Patient\n3. Add Patient\n4. Update Patient Data\n5. Delete Patient\n6. View Inpatient Log History\n7. Inpatient Check In\n8. Inpatient Check-Out\n9. Exit DataMed")
    print("--------------------------------------")
    input_menu = input("Choose Menu: ")
    if input_menu =="1":
        show_patient()
    elif input_menu =="2":
        find_patient()
    elif input_menu =="3":
        add_patient()
    elif input_menu =="4":
        update_patient()
    elif input_menu =="5":
        delete_patient()
    elif input_menu =="6":
        view_logs()
    elif input_menu == "7":
        check_in()
    elif input_menu == "8":
        inp_id = input("Enter Inpatient ID for check-out: ").strip()
        check_out(inp_id)
    elif input_menu =="9":
        print("Exit Program, Thank you for using DataMed!")
        break
    else:
        print("\nUnrecognized input, try again!")