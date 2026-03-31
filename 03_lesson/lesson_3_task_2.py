from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "IPhone 13", "+79523456789"),
    Smartphone("Apple", "IPhone 14", "+79319876543"),
    Smartphone("Apple", "IPhone 15", "+79215678901"),
    Smartphone("Apple", "IPhone 16", "+79111234560"),
    Smartphone("Apple", "IPhone 17", "+79857890123")
]

for smartphone in catalog:
    print(
      f"{smartphone.phone_name} - {smartphone.phone_model}. "
      f"{smartphone.phone_number}"
    )
