import csv
import numpy as np
from niaaml.data.data_reader import DataReader
from niaaml.utility import get_label_encoder

__all__ = ['CSVDataReader']

class CSVDataReader(DataReader):
    def _set_parameters(self, src, **kwargs):
		r"""Set the parameters of the algorithm.

		Arguments:
			 src (string): Path to a CSV dataset file.

		See Also:
			 * :func:`niaaml.data.DataReader.setParameters`
		"""
        DataReader._set_parameters(self, **kwargs)
        self.__src = src
        self._read_data()

    def _read_data(self, **kwargs):
        r"""Read data from expected source.
        """
        x = []
        y = []
        with open(self.__src) as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)
            for row in reader:
                x.append(row[1:])
                y.append(row[0])

            self._x = np.array(x).astype(np.float)

            self._label_encoder = get_label_encoder(y)
            self._y = np.array(self._label_encoder.transform(y)).astype(np.uintc)