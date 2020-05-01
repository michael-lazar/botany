#!/usr/bin/env python2
from botany import *


if __name__ == '__main__':
    my_data = DataManager()
    # if plant save file exists
    if my_data.check_plant():
        my_plant = my_data.load_plant()
    # otherwise create new plant
    else:
        my_plant = Plant(my_data.savefile_path)
        my_data.data_write_json(my_plant)
    filename = CursedMenu.get_art_file(my_plant)
    print(ArtFile(filename, my_plant.color).export())
