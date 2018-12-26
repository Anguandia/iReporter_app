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

    def edit(self, red_flag_id, data, field):
        try:
            red_flag = red_flags[str(red_flag_id)]
            if red_flag['status'] in ['rejected', 'resolved']:
                result = [
                    403, 'error', f'red flag already {red_flag["status"]}'
                    ]
            else:
                red_flag[field] = data[field]
                result = [200, 'data', [{'id': red_flag_id, 'message':
                          f'{field} updated to \'{data[field]}\''}]]
        except Exception:
            result = self.get_flag(red_flag_id)
        return result
