import os
import sys
import all_order
import inventory_health
import custom
import performance_by_placement

current_path=os.getcwd()
file=open(current_path+r"\config.txt")
data=file.read()
tmp=data.split("\n")

userData=tmp[0]
executable_path=tmp[1]


if len(sys.argv) > 2:
    app=sys.argv[0]
    method=sys.argv[1]
    if app == "all_order" :
        all_order=AllOrder(userData,executable_path)
        if method == "report":        
            all_order.report()
        elif method == "send":
            all_order.send()
        elif method == "download":
            all_order.download()

    elif app == "custom":
        custom=custom.Custom(userData,executable_path)
        if method == "report":
            custom.report()
        elif method == "send":
            custom.send()
      
    elif app == "inventory":
        pass
    elif app == "performance_by_sku":
        pass
    elif app == "performance_by_placement":
        per = performance_by_placement.PerformanceByPlacement(userData,executable_path)
        if method == "report":
            per.report()
        elif method == "send":
            per.send()
    elif app == "":
        pass
        
            
            
            
            
