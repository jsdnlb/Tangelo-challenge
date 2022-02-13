MSG_TYPE_ERROR = 'Invalid parameters, validate the information entered.'
MSG_KEY_ERROR = 'Invalid parameters, must send a DataFrame'
 

def calculate_execution_times(data):


    try:
        print('\nCalculating table execution times... 🖥\n')

        max_time = data['Time'].max()
        min_time = data['Time'].min()
        average_time = data['Time'].mean().round(2)
        total_time = data['Time'].sum().round(2)

        print('Maximum time: ', str(max_time) + ' ms')
        print('Minimum time: ', str(min_time) + ' ms')
        print('Average time: ', str(average_time) + ' ms')
        print('Total time: ', str(total_time) + ' ms\n')

        return (max_time, min_time, average_time, total_time)

    except TypeError:
        return MSG_TYPE_ERROR
    except KeyError:
        return MSG_KEY_ERROR
