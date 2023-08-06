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

