#!/usr/bin/python

import pandas as pd
import numpy

def outlierCleaner(predictions, ages, net_worths):

    numpy.set_printoptions(precision=4, suppress=True)
    col_names = ['pred', 'age', 'net worth']
    cleaned_data = numpy.concatenate((predictions, ages, net_worths), axis=1)
    cleaned_data = pd.DataFrame(cleaned_data, columns=col_names)
    cleaned_data['error'] = numpy.absolute(cleaned_data['pred'] - cleaned_data['net worth'])
    cleaned_data = cleaned_data.sort_values(by='error').reset_index()
    cleaned_data = cleaned_data[:81]
    cleaned_data = cleaned_data[['age', 'net worth', 'error']]
    cleaned_data = cleaned_data.as_matrix()

    # print cleaned_data

    return cleaned_data

