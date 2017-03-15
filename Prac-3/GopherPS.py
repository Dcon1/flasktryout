import random
DIED_MIN = 5
DIED_MAX = 25
BORN_MIN = 10
BORN_MAX = 20
SIMULATION_YEARS = 10
def main():
    gopher_population =  1000
    print("Welcome to the gopher population simulator!\nStarting population is {}".format(gopher_population))
    for i in range(0,SIMULATION_YEARS,1):
        calc_year(i, gopher_population)

def calc_year(year_number, gopher_amount):
    gopher_died = gopher_amount / 100 * random.randint(DIED_MIN, DIED_MAX)
    gopher_born = gopher_amount / 100 * random.randint(BORN_MIN, BORN_MAX)
    yearly_population = gopher_amount - gopher_died + gopher_born
    print("Year {}\n*****\n{:,.0f} gophers were born. {:,.0f} died.\npopulation: {:,.0f}\n".format(year_number + 1,gopher_born,gopher_died, yearly_population))
    return yearly_population

main()