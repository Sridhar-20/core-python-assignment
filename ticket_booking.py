def get_available_seats(total_seats, booked_seats):
    return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

def book_seat(total_seats, booked_seats, seat_number):
    if seat_number < 1 or seat_number > total_seats:
        return "Invalid seat number."
    if seat_number in booked_seats:
        return f"Seat {seat_number} is already booked."
    booked_seats.append(seat_number)
    return f"Seat {seat_number} has been successfully booked."

def cancel_seat(booked_seats, seat_number):
    if seat_number not in booked_seats:
        return f"Seat {seat_number} is not booked."
    booked_seats.remove(seat_number)
    return f"Seat {seat_number} has been successfully canceled."

total_seats = 10
booked_seats = [2, 5, 7]
book_seat_number = 3
cancel_seat_number = 5

booking_message = book_seat(total_seats, booked_seats, book_seat_number)

cancellation_message = cancel_seat(booked_seats, cancel_seat_number)

available_seats = get_available_seats(total_seats, booked_seats)

print(f"Available seats: {available_seats}")
