#my_dictionary = {
#    "key1": "[List]",
#    "key2": "Value",
#} // nesting a list from a dictionary

#print(my_dictionary)

#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Stuttgart", "Berlin"],
#}
#print(travel_log["France"][1])

#nested_list = ["A", "B", ["C", "D"]]
#print(nested_list[2][1])  // nesting a list from a list

#my_dictionary = {
#    key1: Value,
#    key2: {Key: Value, Key: Value},
#}  // nesting a dictionary from a dictionary

travel_log = {
  "France": {
    "cities_visited": ["Paris", "Lille", "Dijon"],
    "total_visits": 12
   },
  "Germany": {
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
   },
}

print(travel_log["Germany"]["cities_visited"][2])





