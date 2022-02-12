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

def GetClassesFromApi(school_id):
    url = "https://www.adozionilibriscolastici.it/v1/classi/" + school_id
    try:
        response = requests.request("GET", url)
        return yaml.dump(response.text, allow_unicode=True)
    except requests.exceptions.MissingSchema as e:
        print(f"\n[ERROR] | {school_id}: {e}")
        return False


def check_school_path(school_id):
    '''Checks if the temp path exists, if not, creates it'''
    if not os.path.exists(school_id):
        os.makedirs(school_id)

def load_school_index_json():
    with open("index.yml", 'r') as file:
        data = yaml.safe_load(file)

        region =

if __name__ == '__main__' :
