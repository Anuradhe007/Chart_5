def bar_chart_1(data_file_path, chart_title):
    file = open(data_file_path, 'r')
    room_1 = 0
    room_2 = 0
    room_3 = 0
    room_4 = 0
    executive = 0

    for line in file.readlines():
        room = line.split(',')[1].strip()
        no_of_resale = line.split(',')[2].strip('\n')

        if room == '1-room':
            room_1 = room_1 + int(no_of_resale)
        if room == '2-room':
            room_2 = room_2 + int(no_of_resale)
        if room == '3-room':
            room_3 = room_3 + int(no_of_resale)
        if room == '4-room':
            room_4 = room_4 + int(no_of_resale)
        if room == 'Executive':
            executive = executive + int(no_of_resale)

def line_chart_1(data_file_path, chart_title):
    price_dict = dict()
    file = open(data_file_path, 'r')
    next(file)
    for line in file.readlines():
        year = int(line.split(',')[8].strip())
        price = int(line.split(',')[10].strip())
        if year in price_dict:
            price_dict[year] += price
        else:
            price_dict[year] = price