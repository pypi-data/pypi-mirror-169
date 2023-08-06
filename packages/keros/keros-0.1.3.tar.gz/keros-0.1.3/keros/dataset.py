from skimage.io import imread
import numpy as np

class dataset:

    def __init__(self, batches):
        self._files = []
        self._batches = batches
        self._n_batches = len(batches)
        self._read_files()

    def read_batch(self, batch):
        """
        Info:
            Lê um lote de imagens do dataset.
        Params:
            batch (int): Id do lote.
        Return:
            Lista de imagens.
        """
        images = []
        for file in self._batches[str(batch)]:
            images.append(imread(file))
        
        return np.asarray(images)


    def _read_files(self):
        """
        Info:
            Lê todos os diretórios dos arquivos do dataset.
        Return:
            Lista com diretórios.
        """
        for batch in self._batches:
            for file in self._batches[batch]:
                self._files.append(file)

        self._files = np.asarray(self._files)

    @property
    def files(self):
        return self._files

    @property
    def n_batches(self):
        return self._n_batches



