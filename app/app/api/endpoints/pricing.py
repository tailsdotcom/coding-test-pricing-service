from ...main import api
from ...core.pricing import get_price_rules
from flask_restplus import Resource


ns = api.namespace('pricing', description='Pricing')


@ns.route('/rules')
class PricingRules(Resource):

    @ns.doc(description='Pricing Rules')
    def get(self):
        rules = get_price_rules()

        return rules

