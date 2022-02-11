from numpy import average


def calculate_execution_times(data):
    min_time = data['Time'].min()
    max_time = data['Time'].max()
    average_time = data['Time'].mean().round(2)
    total_time = data['Time'].sum().round(2)

    return {'min_time': min_time, 'max_time': max_time, 'average_time': average_time, 'total_time': total_time}
