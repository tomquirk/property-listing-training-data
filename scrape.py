from realestate_com_au import RealestateComAu
import json

api = RealestateComAu()
import jsonpickle

# Get property listings
start_page = int(open("progress.txt", "r").read())
progress_file = open("progress.txt", "w")

while True:
    print('start_page: ' + str(start_page))
    listings = api.search(limit=1000, start_page=start_page)
    for listing in listings:
        d = jsonpickle.encode(listing)
        f = open("data/" + listing.id + ".json", "w")
        f.write(d)
    start_page += 1
    progress_file.write(str(start_page))
    
