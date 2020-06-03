from flask_restful import Resource

class Periods(Resource):
    def get(self):
        sample_response = [
            {
                "start_date": "2020/01/01",
                "duration":  "5",
                "created_date": "yyyy/mm/dd"
            },
            {
                "start_date": "2020/02/01",
                "duration":  "5",
                "created_date": "yyyy/mm/dd"
            },
        ]
        return {'message': 'latest periods found', 'data': sample_response}, 200