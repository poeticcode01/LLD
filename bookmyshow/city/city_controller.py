class CityController:

    def __init__(self):
        self.cities_list = self.build_cities()

    def get_list_of_cities(self):
        return self.cities_list
    
    def add_cities(self,name: str):
        self.cities_list.append(name)

    def build_cities(self):
        city_list = ["Bangalore","Hyderabad","Mumbai"]
        for city in city_list:
            self.add_cities(city)

    def remove_city(self,city):
        del self.cities_list[city]

if __name__ == "__main__":
    tst = ["Bangalore","Hyderabad","Mumbai"]
    print(tst)
    tst.remove("Hyderabad")
    print(tst)

        
