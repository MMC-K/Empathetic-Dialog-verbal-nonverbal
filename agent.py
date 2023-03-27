import json

from empathetic_response import DM_Response

class Service:
    task = [
        {
            'name': "empathetic response",
            'description': 'generate empathetic response'
        }
    ]

    def __init__(self):
        self.model = ExampleModel()
    
    @classmethod
    def get_task_list(cls):
        return json.dumps(cls.task), 200
    
    def do(self, content):
        try:
            ret = self.model.response(content)
            if 'error' in ret.keys():
                return json.dumps(ret), 400
            return json.dumps(ret), 200
        except Exception as e:
            return json.dumps(
                {
                    'error': "{}".format(e)
                }
            ), 400


class ExampleModel(object):
    def __init__(self):
        self.model = DM_Response('best', './model/ke_t5_dm')
        self.user_uttr_history = {}

    def get_user_uttr_with_history(self, uid, text):
        if uid not in self.user_uttr_history:
            self.user_uttr_history[uid] = [text]
        else:
            self.user_uttr_history[uid].append(text)
            if len(self.user_uttr_history[uid]) > 3: self.user_uttr_history[uid].pop(0)

        return ' '.join(self.user_uttr_history[uid])
    
    def response(self, content):
        uid = content.get('uid', None)
        text = content.get('text', None)
        if uid is None or text is None:
            return {
                'error': "content must have uid or text."
            }
        elif text in ["reset", "/reset"]:
            if uid in self.user_uttr_history: self.user_uttr_history[uid].clear()
        else:
            response = self.model.get_response(self.get_user_uttr_with_history(uid, text))
            return {'text': response}


if __name__ == "__main__":
    dummy = ExampleModel()
    ret = dummy.response({
        'uid':'11111', 
        'text':"아 화나네"
        })
    print(ret)