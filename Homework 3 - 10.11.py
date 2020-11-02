#Pranav Tetali
#ID 1541822
#Homework 3 10.11

class FoodItem:

    # TODO: Define constructor with parameters to initialize instance
    # attributes (name, fat, carbs, protein)
    # provided in the question
    def __init__(self, name=None, fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein

    def get_calories(self, num_servings):
        # Calorie formula i used
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))

if __name__ == "__main__":
    #fooditem #1
    food_item1 = FoodItem()
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    #fooditem #2
    food_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    num_servings = float(input())
    
    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food_item1.get_calories(num_servings)))
    print()
    
    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,food_item2.get_calories(num_servings)))
