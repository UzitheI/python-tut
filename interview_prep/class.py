class Car:
    
    def __init__(self,name, model, made_year ):
        self.name=name
        self.model=model
        self.made_year=made_year
        
    
    def print_car_stats(self):
        return f"The name of the car is {self.name}. It's model is {self.model} and the year it was made in was {self.made_year}"


class Volkswagen(Car):
    
    volkswagen_initial='VOL'
    
    def add_initial(self):
        return f"The volkswagen car is {self.volkswagen_initial}-{self.name} "


volkswagen_model=Volkswagen('Volksw','V7',1920)
    



def main():
    volkswagen_model=Volkswagen('Volksw','V7',1920)
    print(volkswagen_model.add_initial())
    print('Enter the number of entries of cars that you want to make:')
    number_of_cars=int(input())
    
    
    
    for i in range(number_of_cars):
        print('Enter the name of the car:')
        cars_name=input()
        
        print('Enter the model of the car:')
        car_model=input()
        
        print('Enter the year that it was made:')
        year_made=int(input())
        
        car=Car(cars_name,car_model,year_made)
        
        
        print(car.print_car_stats())


if __name__== '__main__':
    main()
    
    