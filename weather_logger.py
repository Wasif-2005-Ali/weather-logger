# weather_logger.py
temps = []
while True:
    val = input("Enter temperature ('done' to stop): ")
    if val.strip().lower() == "done":
        break
    temps.append(float(val))

print("Entered temperatures:", temps)