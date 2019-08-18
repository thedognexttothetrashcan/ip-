from flask_restful import Resource


class GoodsResource(Resource):

    def get(self):

        return {"msg": "不是谁都能吃爆米花的"}