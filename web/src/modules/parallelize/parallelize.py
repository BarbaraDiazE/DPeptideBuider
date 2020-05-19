from python_utilities.scripting import setup_logging
from python_utilities.parallel import Parallelizer, make_data_iterator

"""
Aaron implementation
"""


def parallelize_func(func, data_list, **kwargs):

    print(kwargs)

    # data_iterator = make_data_iterator(data_list)
    data_iterator = data_list
    print("data_iterator", data_iterator)
    output_data = []

    parallelizer = Parallelizer(parallel_mode="processes")
    run_kwargs = {
        # "out_file": "atom.txt",
        "out_str": "%s\n",
        "out_format": lambda x: output_data.append(x),
        "logging_str": "%s",
        "logging_format": lambda x: x,
        "kwargs": kwargs,
    }
    parallelizer.run(func, data_iterator, **run_kwargs)
    return output_data

