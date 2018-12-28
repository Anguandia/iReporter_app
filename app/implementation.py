from .models import RedFlag
import datetime

red_flags = {}


class Implementation:
    def creat(self, data):
        red_flag = RedFlag((len(red_flags)+1), data['location'],
                           data['createdBy'], data['comment'])
        for field in data:
            if field not in ['location', 'createdBy', 'comment']:
                red_flag.__setattr__(field, data[field])
        red_flags[str(red_flag.id)] = red_flag.__dict__
        return [
            201, 'data', [{'id': red_flag.id, 'message': 'Created red flag'}]
            ]

    def get_flags(self):
        if not red_flags.keys():
            res = [404, 'error', 'no red flags']
        else:
            res = [200, 'data', [red_flags[key] for key in red_flags.keys()]]
        return res

    def get_flag(self, red_flag_id):
        try:
            red_flag = red_flags[str(red_flag_id)]
            res = [200, 'data', [red_flag]]
        except Exception as e:
            print(e)
            res = [404, 'error', 'red flag not found']
        return res
