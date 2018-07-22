from ...main import api
from ...core.pricing import get_price_rules
from ...core.order_pricer import price_order
from flask import request
from flask_restplus import Resource

ns = api.namespace('pricing', description='Pricing')


@ns.route('/rules')
class PricingRules(Resource):

    @ns.doc(description='Pricing Rules')
    def get(self):
        rules = get_price_rules()

        return rules


order = ns.schema_model('Order', {
    'type': 'object',
    'properties': {
        'order': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer'
                },
                'customer': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string'},
                        'customer_id': {'type': 'integer'}
                    },
                },
                'items': {
                    'type': 'array',
                    'items': {
                        'type': 'object',
                        'properties': {
                            'product_id': {
                                'type': 'integer'
                            },
                            'quantity': {
                                'type': 'integer'
                            }
                        }
                    }
                }
            }
        }
    }
})


@ns.route('/quote')
class Quote(Resource):
    @ns.expect(order, validate=True)
    @ns.doc(description='Quote a given order')
    def post(self):
        rules = get_price_rules()
        order = request.json
        return price_order(order, rules)
