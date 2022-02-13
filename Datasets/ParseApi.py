# Main.py
#
# Copyright 2022 Francesco Masala <mail@francescomasala.me>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import requests
import yaml
import json

def migrate_json_to_yaml(json_string):
    return yaml.dump(json.loads(json_string),sort_keys=False, allow_unicode=True)

def get_classes_from_api(school_id):
    url = "https://www.adozionilibriscolastici.it/v1/classi/" + school_id
    try:
        response = requests.request("GET", url)
        string = str(response.text)
        return migrate_json_to_yaml(string)
    except requests.exceptions.MissingSchema as e:
        print(f"\n[ERROR] | {school_id}: {e}")
        return False

def get_schools_from_api(city, grade):
    url = "https://www.adozionilibriscolastici.it/v1/scuole?locId=" + city + "&grado=" + grade 
    try:
        response = requests.request("GET", url)
        string = str(response.text)
        return migrate_json_to_yaml(string)
    except requests.exceptions.MissingSchema as e:
        print(f"\n[ERROR] | {city}: {e}")
        return False        

def get_books_from_api(school_id, class_id):
    url = "https://www.adozionilibriscolastici.it/v1/libri/" + class_id + "/" + school_id
    try:
        response = requests.request("GET", url)
        string = str(response.text)
        return migrate_json_to_yaml(string)
    except requests.exceptions.MissingSchema as e:
        print(f"\n[ERROR] | {class_id}: {e}")
        return False


def check_path(region, school_id):
    '''Checks if the temp path exists, if not, creates it'''
    if not os.path.exists(region):
        os.makedirs(region)
    if not os.path.exists(region + "/" + school_id):
        os.makedirs(region + "/" + school_id)


if __name__ == '__main__' :
    print(get_classes_from_api("TNTF01301D"))
    print("---------")
    print(get_books_from_api("TNTF01301D","121445"))
    print("---------")
    print(get_schools_from_api("Trento", "2"))
