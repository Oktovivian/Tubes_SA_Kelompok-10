def calculate_profit(bookings):
    bookings.sort(
        key=lambda x: x[2] / (x[3][1] - x[3][0]), reverse=True
    )  # Mengurutkan pesanan berdasarkan profit/durasi tertinggi
    schedule = [0] * 60  # Membuat jadwal 60 menit (15:00 - 18:00)
    total_profit = 0
    total_capacity = 0
    selected_bookings = []

    for booking in bookings:
        name = booking[0]
        capacity = booking[1]
        price = booking[2]
        start_time = booking[3][0]
        end_time = booking[3][1]

        # Mengecek apakah jadwal booking masih tersedia
        if max(schedule[start_time:end_time]) == 0:
            schedule[start_time:end_time] = [1] * (end_time - start_time)

            # Mengecek apakah kapasitas makanan mencukupi
            if total_capacity + capacity <= 10000:
                total_profit += price
                total_capacity += capacity
                selected_bookings.append((name, price))

    return total_profit, selected_bookings


# Data penyewa
bookings = [
    # ["Andi", 4000, 8000000, (15, 16)],
    # ["Bambang", 3000, 26000000, (15, 17)],
    # ["Cacuk", 3800, 27000000, (15, 18)],
    # ["Dimas", 3200, 12000000, (16, 17)],
    # ["Eko", 3600, 20000000, (16, 18)],
    # ["Farid", 3400, 11000000, (17, 18)],
    ["Andi", 4000, 7000000, (15, 16)],
    ["Bambang", 3000, 18000000, (15, 17)],
    ["Cacuk", 3800, 33000000, (15, 18)],
    ["Dimas", 3200, 10000000, (16, 17)],
    ["Eko", 3600, 16000000, (16, 18)],
    ["Farid", 3400, 6000000, (17, 18)],
]

max_profit, selected_bookings = calculate_profit(bookings)
print("Keuntungan maksimal yang dapat diperoleh: Rp", max_profit)
print("Pemesan yang dipilih:")
for booking in selected_bookings:
    print("Nama:", booking[0])
    print("Keuntungan:", booking[1])
    print("-------------")
