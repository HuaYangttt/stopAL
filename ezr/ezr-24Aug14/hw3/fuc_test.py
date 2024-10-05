import sys,random,os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
sys.path.append(parent_dir) # add parent_dir to sys.path

from ezr import the, DATA, csv, dot
from part1 import guess

class TestGuessFunctionality:

    def setup_method(self):
        # Initialize a test dataset
        test_data = csv('/workspaces/ezr/data/optimize/misc/auto93.csv')
        test_data = list(test_data)[0:4]
        # [['Clndrs', 'Volume', 'HpX', 'Model', 'origin', 'Lbs-', 'Acc+', 'Mpg+'], 
        # [8, 304, 193, 70, 1, 4732, 18.5, 10], 
        # [8, 360, 215, 70, 1, 4615, 14, 10], 
        # [8, 307, 200, 70, 1, 4376, 15, 10]]

        self.data = DATA().adds(test_data)


    def test_chebyshevs_returns_sorted_top_item(self):
        # Get the sorted Chebyshev distance rows
        sorted_rows = self.data.chebyshevs().rows

        # check if chebyshevs().rows[0] return the top item in that sort
        expected_top_item = sorted(self.data.rows, key=lambda row: self.data.chebyshev(row))[0]
        assert sorted_rows[0] == expected_top_item, "chebyshevs().rows[0] does not return the top sorted item"

    def test_smart_and_dumb_list_length(self):
        N = 3
        # check the length of dumb list
        dumb_list = guess(N, self.data)
        assert len(dumb_list.rows) == N, "dumb list length is incorrect"
        
        # check the length of smart list
        smart_list = [self.data.shuffle().activeLearning()[0] for _ in range(N)]
        assert len(smart_list) == N, "smart list length is incorrect"

    def test_experimental_treatment_runs_20_times(self):
        N = 3
        # check the number of experimental treatment
        smart_list = [self.data.shuffle().activeLearning()[0] for _ in range(20)]
        assert len(smart_list) == 20, "The experimental treatment did not run 20 times"

    def test_shuffle_jiggles_data_order(self):
        # Save the original data order
        original_order = self.data.rows[:]
        # Execute the shuffle operation
        self.data.shuffle()
        # Ensure that the order has changed
        assert self.data.rows != original_order, "shuffle() did not change the data order"
        # Ensure the data length remains the same after shuffling
        assert len(self.data.rows) == len(original_order), "shuffle() changed the data length"
