raw_data = "  AhMeT  yILMAZ ;  23 ;  1.78 ;  ahmetYILMAZ@GMAIL.Com   "

clean_data = raw_data.strip()
parts = clean_data.split(";")

name_raw = parts[0].strip()
name_clean = name_raw.lower().title()
name_fixed = name_clean.replace("  ", " ")

first_char = name_fixed[0:1]
rest_chars = name_fixed[1:]
name_final = first_char + rest_chars

age_raw = parts[1].strip()
age_int = int(age_raw)
age_after_10 = float(age_int + 10)

height_raw = parts[2].strip()
height_m = float(height_raw)
height_cm = height_m * 100

email_raw = parts[3].strip()
email_clean = email_raw.lower()

at_index = email_clean.find("@")
email_username = email_clean[0:at_index]
email_code = email_username[0:3]

print("Kullanıcı:", name_final)
print("Yaş (10 yıl sonra):", age_after_10)
print("Boy (cm):", height_cm)
print("Email kullanıcı kodu:", email_code)