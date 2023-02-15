import math
import csv

with open("Data.csv") as file:
    reader = csv.reader(file, delimiter=",")
    for row in reader:
        Itemidx = row.index("item")
        OHidx = row.index("OH")
        OOidx = row.index("OO")
        UOMidx = row.index("UOM")
        Paridx = row.index("Min")
        break
    for row in reader:
        #On hand is set equal to current on hand value + products on order
        OH = int(row[OHidx]) + int(row[OOidx])
        UOM = int(row[UOMidx])
        Par = int(row[Paridx])

        OrderAMT = math.ceil((Par-OH)/UOM)
        Excess = ((OrderAMT*UOM) + OH)-(Par)

        #Conditional to adjust the order amount if the excess created would be extreme (Typically if UOM is greater than par)
        #if Excess > Par * 0.5: OrderAMT -= 1; Excess = ((OrderAMT*UOM) + OH)-(Par)

        print(f"Item: {row[Itemidx]}, Order amount (individual): {OrderAMT*UOM}, Amount above par after order: {Excess}")