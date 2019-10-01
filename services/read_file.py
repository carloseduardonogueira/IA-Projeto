class Read:

    @staticmethod
    def readFile(input):
        #lendo um arquivo txt
        file = open(input, 'r') #abre o arquivo e lê
        #lê cada linha do arquivo 
        file_stuff = file.readlines()
        file.close()
        return file_stuff