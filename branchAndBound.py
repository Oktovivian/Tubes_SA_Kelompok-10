from heapq import heappop, heappush


class Event:
    def _init_(self, name, capacity, price, start_time, end_time):
        self.name = name
        self.capacity = capacity
        self.price = price
        self.start_time = start_time
        self.end_time = end_time
        self.profit = self.price / (self.end_time - self.start_time)

    def _lt_(self, other):
        # Order by profit per duration (descending)
        return self.profit > other.profit


def get_maximum_profit(events, max_capacity, max_time):
    # Sort events by profit/duration (descending)
    events.sort()

    max_profit = 0
    best_combination = None
    pq = []

    # Initialize the priority queue with the first event
    event = events[0]
    heappush(pq, (event.profit, [event]))

    while pq:
        profit, combination = heappop(pq)

        # Check if the current combination is the best so far
        if profit > max_profit:
            max_profit = profit
            best_combination = combination

        last_event = combination[-1]

        # Try adding the next event to the current combination
        for i in range(events.index(last_event) + 1, len(events)):
            next_event = events[i]

            # Check if the next event can fit in terms of capacity and time
            if (
                last_event.end_time <= next_event.start_time
                and next_event.end_time <= max_time
                and sum(e.capacity for e in combination) + next_event.capacity
                <= max_capacity
            ):
                new_combination = combination + [next_event]
                new_profit = profit + next_event.profit
                heappush(pq, (new_profit, new_combination))

    return best_combination, max_profit


# Create event objects
events = [
    Event("Andi", 4000, 8000000, 15, 16),
    Event("Bambang", 3000, 26000000, 15, 17),
    Event("Cacuk", 3800, 27000000, 15, 18),
    Event("Dimas", 3200, 12000000, 16, 17),
    Event("Eko", 3600, 20000000, 16, 18),
    Event("Farid", 3400, 11000000, 17, 18),
    # Event("Andi", 4000, 7000000, 15, 16),
    # Event("Bambang", 3000, 18000000, 15, 17),
    # Event("Cacuk", 3800, 33000000, 15, 18),
    # Event("Dimas", 3200, 10000000, 16, 17),
    # Event("Eko", 3600, 16000000, 16, 18),
    # Event("Farid", 3400, 6000000, 17, 18),
]

# Set maximum capacity and time
max_capacity = 10000
max_time = 18

# Get the maximum profit combination
best_combination, max_profit = get_maximum_profit(events, max_capacity, max_time)

total = 0

# Print the result
if best_combination:
    print("Best combination:")
    for event in best_combination:
        print(
            f"- {event.name}: {event.capacity} people, Rp {event.price}, {event.start_time} - {event.end_time}"
        )
        total += event.price
    print(f"Maximum profit: Rp {total}")
else:
    print("No valid combination found.")
