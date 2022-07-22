﻿import pandas as pd
import json

class lists():
    def __init__(self):
        self.file_path = 'lists.csv'
        self.database = pd.read_csv(self.file_path)

    def search(self, content, keyword):
        result = self.database[(self.database[keyword] == content)]
        result = json.dumps(result.values.tolist())
        return result

    def get_full_list(self):
        result = json.dumps(self.database.values.tolist())
        return result

    def get_listnames(self):
        result = self.database['list_name'].unique().tolist()
        return result

    def get_recipe_detail(self, recipe_name):
        result = self.database[self.database["recipe_name"] == recipe_name].loc[:,["list_name", "description", "photo_path"]].values[0]
        return result