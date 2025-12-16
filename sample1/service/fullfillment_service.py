
from model.order import Order
from typing import Dict
from utils.loader_util import LoaderUtil

class FullfillmentService:
    def __init__(self):
        loader_util = LoaderUtil()
        self.inventory = loader_util.load_inventory()
    
    def fullfill_order(self,order:Order) -> Dict[str,str]:
        for inventory in self.inventory:
            if inventory.product == order.product:
                if inventory.quantity >= order.qty:
                    inventory.quantity -= order.qty
                    return {"order_id":order.order_id,"assigned_to":inventory.warehouse}
                
        return {"order_id":order.order_id,"assigned_to":"unassigned"}