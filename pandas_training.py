import numpy as np
import pandas as pd


def p():
    # data = np.array([['', 'col1', 'col2'],
    #                  ['row1', 1, 2, ],
    #                  ['row2', 3, 4]
    #                  ])
    # print(pd.DataFrame(data=data[1:, 1:],
    #                    index=data[1:, 0],
    #                    columns=data[0, 1:]))
    # my_2darray = np.array([[1, 2, 3, ], [4, 5, 6]])
    # print(my_2darray)
    # print(pd.DataFrame(my_2darray))
    #
    # my_dict = {1: ['1', '3'], 2: ['2', '3'], 3: ['2', '4']}
    # print(my_dict)
    # print(pd.DataFrame(my_dict))
    #
    # my_df = pd.DataFrame(data=[4, 5, 6, 7], index=range(0, 4), columns=['A'])
    # print(my_df)
    # print(pd.DataFrame(my_df))
    #
    # my_series = pd.Series(
    #     {"Belgium": "Brussels",π "India": "New Delhi", "United Kingdom": "London", "United States": "Washington"})
    # print(my_series)
    df = pd.DataFrame(data=np.array([[1, 2, 3], [1, 5, 6], [7, 8, 9], [10, 11, 12], [113, 14, 15]]),
                      index=[2.5, 12.6, 4.8, 4.8, 2.5], columns=[48, 49, 50])
    df['result'] = ['ABC+-DEF', 'AAA', 'aaaAbBcCdd', 'AA', 'ABC+-']

    # replace string in index 'result'
    # map can be applied to pd.Series (i.e. df['result'])
    # df['result'] = df['result'].map(lambda x: x.lstrip('A').x.rstrip('F'))

    df['ticket'] = ['Like a dragon', '24hours Cindella', 'Majima Goroh', 'Kiryu', 'like a idiot']

    c = pd.read_csv('test.csv', parse_dates=True)
    print(c)


    df = pd.DataFrame(data=np.array([[1,2,3], [4,5,6], [7,8,9]]), columns=['A', 'B', 'C'])
    for index, row in df.iterrows():
        print(row['A'], row['B'])

    s = pd.Series([1,3,5, np.nan, 6,8])

    pd.pivot_table