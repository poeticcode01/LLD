from typing import Dict, List
from city.city_controller import CityController
from cinemahall.cinemahall_contoller import CinemaHallController
from cinemahall.cinemahall import CinemaHall
from movie.movie_controller import MovieController
from screen.screen import Screen
from show.show import Show
from seat.seat import Seat,BookedSeat
from collections import defaultdict

class BookMyShow:
    def __init__(self):
        self.city_contoller = CityController()
        self.cinema_hall_controller = CinemaHallController()
        self.movie_controller = MovieController()

    def get_city_list(self):
        return CityController.get_list_of_cities()
    
    def get_movies_by_city(self,city):
        
        return self.movie_controller.get_movies_by_city(city)

    
    
    def get_shows_list_by_cinemahall(self,city: str,movie_id: str):
        cinema_hall_list: List[CinemaHall] = self.cinema_hall_controller.get_cinemaHall_by_city(city)

        cinema_hall_movies_shows_map: Dict[CinemaHall,Show] = defaultdict(list)

        for cinema_hall in cinema_hall_list:
            shows_list: List[Show] = cinema_hall.get_shows_list()
            for each_show in shows_list:
                if each_show.movie_id == movie_id:
                        cinema_hall_movies_shows_map[cinema_hall].append(each_show)
            
                
                    
        
        return cinema_hall_movies_shows_map
    
    def bookseats(self,seat_list: List[Seat],cinema_hall_id: str,screen_id: str,show_id: str):
         



        

        
    


        