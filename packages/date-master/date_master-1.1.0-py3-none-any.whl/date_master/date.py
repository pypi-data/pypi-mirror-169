import datetime 
from datetime import date, timedelta

from .validation import *
from .changeorder import change_order
from .changeformat import changeformat, changeformat_without_order


def beautiful_date(params):
    try:
        result = None
        date, order, format, split_by = None, None, None, None

        if params != '':
            result = check_params_keys(params)
            if result == True:
                pass
            else:
                return result
        else:
            result = 'Missing date_master parameter'
            return result

        if 'date' in params:

            if params['date'] == ['today']:
                current_date = str(datetime.date.today()).split("-")
                params['date'] = list(map(int, current_date[::-1]))

            if len(params['date']) == 2:
                result = next_day_prev_day_validation(params['date'])

                if result == True:
                    if params['date'][0] == 'today':
                        days_before = (datetime.date.today() + timedelta(days=params['date'][1])).isoformat()
                        current_date = str(days_before).split("-")
                        current_date = list(map(int, current_date[::-1]))
                        params['date'] = current_date
                    else:
                        date_value = params['date'][0]
                        string_date_value = ""
                        for item in date_value:
                            string_date_value=string_date_value+str(item)+','
                        string_date_value = string_date_value.rstrip(',')

                        datetime_datatype_date = datetime.datetime.strptime(string_date_value, '%d,%m,%Y')
                        update_new_date = (datetime_datatype_date + timedelta(days=params['date'][1])).strftime('%d,%m,%Y')
                        update_new_date = update_new_date.split(',')
                        params['date']=list(map(int, update_new_date))
                else:
                    result = 'Invalid Date'
                    return result

            date = params['date']
            result = date_validation(date)
            if result == True:
                pass
            else:
                return result
        else:
            result = 'Date required'
            return result

        if 'order' in params:
            order = params['order']
            result = order_validation(order)
            if result == True:
                order = [x.upper() for x in order]
                pass
            else:
                return result

        if 'format' in params:
            format = params['format']
            result = format_validation(format)
            if result == True:
                pass
            else:
                return result

        if 'split_by' in params:
            split_by = params['split_by']
            result = split_validation(split_by)
            if result == True:
                pass
            else:
                return result


        # ('d', 'o', 'f', 's')
        if date and order and format and split_by:
            result = change_order(date, order)
            result = changeformat(result, order, format)
            result = str(result).replace(',',split_by[0])
            # print('-----------1------------')
        
        # ('d', 'o', 'f')
        elif date and order and format:
            result = change_order(date, order)
            result = changeformat(result, order, format)
            # print('-----------2------------')
        
        # ('d', 'o', 's')
        elif date and order and split_by:
            result = change_order(date, order)
            result = str(result).replace(',',split_by[0])
            # print('-----------3------------')

        # ('d', 'f', 's')
        elif date and format and split_by:
            result = changeformat_without_order(date, format)
            result = str(result).replace(',',split_by[0])
            # print('-----------4------------')

        # ('d', 'o')
        elif date and order:
            result = change_order(date, order)
            # print('-----------5------------')

        # ('d', 'f')
        elif date and format:
            result = changeformat_without_order(date, format)
            # print('-----------6------------')


        # ('d', 's')
        elif date and split_by:
            result = str(date).replace(',',split_by[0])
            # print('-----------7------------')

        # ('d',)
        elif date:
            result = date
            # print('------------8-----------')
        else:
            result = 'Invalid format'

        return result
    except Exception as e:
        message = str(e)
        return message

