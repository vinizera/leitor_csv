def csvGen(data):
    return 0


def dictGen(data_row, data_list):
    data_dict = dict()
    data_dict['id_usuario'] = data_row[0]
    data_dict['data_inicio'] = data_row[1]
    data_dict['hora_inicio'] = data_row[2]
    data_dict['data_fim'] = data_row[3]
    data_dict['hora_fim'] = data_row[4]
    data_list.append(data_dict)

