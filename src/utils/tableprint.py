from prettytable import PrettyTable

def list_event_table(events):
    table = PrettyTable()    
    table.field_names = ["EVENT_NAME", "EVENT_DATE", "LOCATION", "RATING", "PRICE", "CATEGORY", "TICKET_QUANTITY"]
    for event in events:
        table.add_row([event[2], event[3], event[4], event[5], event[6], event[7], event[8]])
    table.align = "l"
    table.max_width["RATING"] = 10
    table.max_width["CATEGORY"] = 16
    print(table)  
    
def booked_event_table(booked_events):
    table = PrettyTable()
    table.field_names = ["EVENT_NAME", "EVENT_DATE", "TICKET_QUANTITY"]
    for booking in booked_events:
        table.add_row([booking[3], booking[4], booking[5]])
    table.align = "l"
    table.max_width["EVENT_NAME"] = 10
    table.max_width["TICKET_QUANTITY"] = 16
    print(table)