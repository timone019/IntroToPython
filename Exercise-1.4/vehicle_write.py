import pickle

vehicle = {
    'brand': 'BMW',
    'model': '530i',
    'year' : 2015,
    'color': 'Black Sapphire'
}

# Calling the pickle.dump() method
# while passing 'vehicle' as the dictionary,
# and 'my_file' as the file object.
my_file = open('vehicledetail.bin', 'wb')
pickle.dump(vehicle, my_file)
my_file.close()