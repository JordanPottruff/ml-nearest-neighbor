
from src.algorithms.knn import KNN


class EditedKNN(KNN):

    def __init__(self, training_data, k):
        super().__init__(training_data, k)
        self.edit_training_data()

    def edit_training_data(self):
        # No return value -- method changes self.training_data variable.
        'empty'