import datetime

def exception_handler(func):
    def inner_function(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"{func.__name__} returned an error: {e}")
    return inner_function

@exception_handler
def validate_date(date):
    if isinstance(date, datetime.date):
        return True
    elif isinstance(date, str):
        return date.lower() in ['today', 'tomorrow', 'yesterday']
    return False

@exception_handler
def datetime_to_string(date_obj):
    return date_obj.strftime("%m/%d/%Y")

@exception_handler
def date_handler(date_obj):
    if isinstance(date_obj, datetime.date):
        return datetime_to_string(date_obj)
    else:
        return date_obj

@exception_handler
def link_handler(link):
    if len(link) == 0:
        return "None"
    return link