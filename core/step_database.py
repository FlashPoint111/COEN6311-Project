﻿import pandas as pd
import json

class steps():
    def __init__(self):
        self.file_path = 'steps.csv'
        self.database = pd.read_csv(self.file_path)

    def get_recipe_detail(self, recipe_name, mode):
        recipe = self.database[self.database["recipe_name"] == recipe_name].loc[:,["step", "ingredient", "quantity", "unit", "description"]]
        recipe = recipe.sort_values(by='step').values.tolist()
        result = []
        for step in recipe:
            row = []
            row.append(step[0])
            if mode == 'html':
                row.append(zip(step[1].split(','), step[2].split(','), step[3].split(',')))
            if mode == 'js':
                row.append([step[1].split(','), step[2].split(','), step[3].split(',')])
            row.append(step[4])
            result.append(row)
        return result

    def add_step(self, recipe_name, step, ingredient, quantity, unit, description):
        ingredient = ",".join(ingredient)
        quantity = ",".join(quantity)
        unit = ",".join(unit)
        record = {'recipe_name':recipe_name, 'step':step, 'ingredient':ingredient, 'quantity':quantity, 'unit':unit, 'description':description}
        self.database = self.database.append(record, ignore_index=True)
        self.database.to_csv(self.file_path, index=False)

    def delete_step(self,recipe_name):
        for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"step"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"step"][i])
        for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"ingredient"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"ingredient"][i])
        for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"quantity"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"quantity"][i])
        for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"unit"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"unit"][i])
        for i in range(len(self.database.loc[self.database.recipe_name == recipe_name,"description"])):
           self.database.drop(self.database.loc[self.database.recipe_name == recipe_name,"description"][i])
        

