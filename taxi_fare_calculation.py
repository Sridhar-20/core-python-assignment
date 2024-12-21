def calculate_fare(distance):
    base_fare = 50
    distance_fare = 10 * distance
    return base_fare + distance_fare

def calculate_total_fare(trips):
    total_fare = 0
    for i, distance in enumerate(trips, start=1):
        trip_fare = calculate_fare(distance)
        total_fare += trip_fare
        print(f"Trip {i}: ${trip_fare}")
    print(f"Total Fare: ${total_fare}")

trips = [5, 10, 3]
calculate_total_fare(trips)
