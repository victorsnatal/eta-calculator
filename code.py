from datetime import datetime, timedelta

# Constants
average_speed_kmh = 60  # Average speed of the truck in km/h
daily_drive_hours = 12  # Number of driving hours per day
start_time = datetime.strptime("2023-08-24 13:00", "%Y-%m-%d %H:%M")  # Start time
total_distance_km = 3000  # Total distance in km
rest_start_time = datetime.strptime("21:00", "%H:%M")  # Rest start time
rest_end_time = datetime.strptime("05:00", "%H:%M")  # Rest end time

# Initialize variables
current_time = start_time
remaining_distance = total_distance_km
total_days = 0

# Calculate ETA considering rest stops
while remaining_distance > 0:
    if current_time.time() >= rest_start_time.time() or current_time.time() < rest_end_time.time():
        # Rest period, wait until rest end
        current_time = current_time.replace(hour=rest_end_time.hour, minute=rest_end_time.minute)
    else:
        # Driving period
        drive_hours_today = min(daily_drive_hours, remaining_distance / average_speed_kmh)
        current_time += timedelta(hours=drive_hours_today)
        remaining_distance -= drive_hours_today * average_speed_kmh
    
    total_days += 1

# Calculate ETA
eta_time = start_time + timedelta(days=total_days)

print("ETA:", eta_time.strftime("%Y-%m-%d %H:%M"))
