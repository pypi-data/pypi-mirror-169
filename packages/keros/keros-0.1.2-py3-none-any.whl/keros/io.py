import glob
from dataset import dataset

class Io:

    def read(path, batch_size=10):
        """
        Info:
            Lê um conjunto de imagens de um diretório.
        Params:
            path (string): Caminho do diretório.
            batch_size (int): Tamanho do lote de imagens.
        return:
            Objeto dataset.
        """
        batchs = {}
        files = glob.glob(path)

        if len(files) < batch_size:
            raise Exception("O tamanho do lote é maior que o número de imagens no diretório.")

        count = 0
        for batch in range(0, len(files), batch_size):
            batchs[str(count)] = files[batch:batch+batch_size]

            count += 1

        return dataset(batchs)

        

        


