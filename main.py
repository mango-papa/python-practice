import merge_sort
import quick_sort
import min_num_changes
import fibonacci
import bicycle
import pandas_training

def main():
    l = [1, 3, 2, 5, -1, 0, 4, 1]
    # print(merge_sort.sort(l))
    # print(quick_sort.sort(l))

    # print(fibonacci.get(100))
    # print(fibonacci.get(99))
    # print(fibonacci.get(10))

    # print(min_num_changes.find_change2(7, [1,3,4, 5, 10]))
    # print(min_num_changes.find_change(31, [1, 5, 10, 15, 16]))
    # print(min_num_changes.find_change(10, [1, 2]))
    # print(min_num_changes.find_change(12, [1, 5]))
    # print(min_num_changes.find_change(12, [2, 5]))

    # print(min_num_changes.find_change2(12, [1, 5]))
    # print(min_num_changes.find_change2(31, [1, 5, 11, 15, 16]))
    my_bicycle = bicycle.Bicycle(20, 'blue')
    # my_bicycle.wheel_size = 26
    # my_bicycle.color = 'red'

    # my_bicycle.move(30)
    # my_bicycle.turn('left')
    # my_bicycle.stop()
    #
    # folding_bicycle = bicycle.FoldingBicycle(27, 'red', 'unfolding')
    # folding_bicycle.move(20)
    # folding_bicycle.fold()
    # folding_bicycle.unfold()
    pandas_training.p()

if __name__ == "__main__":
    main()
