from utils.loader_util import LoaderUtil
from service.fullfillment_service import FullfillmentService

if __name__ == "__main__":
    loader_util = LoaderUtil()
    fullfillment_service = FullfillmentService()
    orders = loader_util.load_orders()
    inventory = loader_util.load_inventory()
    output = []
    for order in orders:
        output.append(fullfillment_service.fullfill_order(order))
    print(output)