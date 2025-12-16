import csv
import json
from model.inventory import Inventory
from model.order import Order

class LoaderUtil:
    def __init__(self):
        self.inventory_file = "python/sample1/inventory.csv"
        self.orders_file = "python/sample1/orders.json"
    
    def load_orders(self):
        with open(self.orders_file,"r") as f:
            orders = json.load(f)
            return [Order(**order) for order in orders]
    
    def load_inventory(self):
        with open(self.inventory_file,"r") as f:
            inventory = csv.DictReader(f)
            return [Inventory(**row) for row in inventory]