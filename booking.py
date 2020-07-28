booking = list()
current_time = 0


def book(r):
    global booking, current_time
    time, hotel_name, client_id, room_count = r.split()[1:]
    time = int(time)
    room_count = int(room_count)
    current_time = time # current_time - время последнего запроса BOOK
    booking.append({'time': time, 'hotel_name': hotel_name, 'client_id': client_id, 'room_count': room_count})
    return len(booking)


def clients(r):
    global booking
    hotel = r.split()[1]
    unique_clients = list()
    for i in booking:
        if (i['hotel_name'] == hotel and i['client_id']) and (current_time - 86400 < i['time'] <= current_time):
            unique_clients.append(i['client_id'])
    return len(unique_clients)


def rooms(r):
    global booking
    hotel = r.split()[1]
    count = 0
    for i in booking:
        if i['hotel_name'] == hotel and (current_time - 86400 < i['time'] <= current_time):
            count += int(i['room_count'])
    return count


def make_request():
    r = input()
    key_word = r.split()[0]
    if key_word.upper() == 'BOOK':
        return book(r)
    elif key_word.upper() == 'CLIENTS':
        return clients(r)
    elif key_word.upper() == 'ROOMS':
        return rooms(r)
    return 0


def main():
    q = int(input('Input amount of requests: '))
    for i in range(q):
        print(f"Requests {i+1} returns: {make_request()}")


main()
