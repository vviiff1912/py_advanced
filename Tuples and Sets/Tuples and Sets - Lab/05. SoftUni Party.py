number_of_guests = int(input())
guests_with_reservation = set()

for _ in range(number_of_guests):
    guests_with_reservation.add(input())

while True:
    guest = input()
    if guest == 'END':
        break
    guests_with_reservation.remove(guest)

print(len(guests_with_reservation))
[print(el) for el in sorted(guests_with_reservation) if el[0].isdigit()]
[print(el) for el in sorted(guests_with_reservation) if not el[0].isdigit()]




