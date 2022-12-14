from ozon_api import Ozon
from config import client_id, api_key


def get_ids(func):
    """ Получает id доступных акций """
    action_ids = []
    for ids_ in func:
        action_ids.append(ids_['id'])
    return action_ids


if __name__ == "__main__":
    ozon = Ozon(client_id, api_key)
    actions = ozon.get_actions_()
    actions_ids = get_ids(actions)

    action_products = []

    for ids in actions_ids:
        fake_action_products = {'action_id': ids, 'products': []}
        for candidates in ozon.get_candidates(ids)['result']['products']:
            c = candidates
            fake_action_products['products'].append(
                {'product_id': candidates['id'], 'action_price': candidates['max_action_price']}
            )
            action_products.append(fake_action_products)

            for a in action_products:

                print(ozon.activate_action(a))