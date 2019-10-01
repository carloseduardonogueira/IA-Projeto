class Prepare_Data:

    @staticmethod
    #prepara os dados que entrarão no dicionário
    def dictionary_data(data):
        d = {}
        for line in data:
            key, value, distance = line.split(',')
            key = key.replace(',', '')
            value = value.replace(',', '')
            distance = int(distance.replace(';', '').replace('\n', ''))
            #se a chave não estiver em cidades, ele recebe um valor, caso contrário é adicionado um novo valor
            if key not in d:
                d[key] = {value: distance}
            else:
                d[key][value] = distance
        return d
