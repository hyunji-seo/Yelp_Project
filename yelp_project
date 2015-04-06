# project
import cx_Oracle, sys

con = cx_Oracle.connect('om', 'om', 'xe')
cur = con.cursor()

option = raw_input("== YELP ACADEMIC DATASET ANALYTICS TOOL ==\n\
Choose one of the following options below (e.g. '3'):\n\
>>OPTION 1: Top-rated/worst-rated businesses according to city\n\
>>OPTION 2: Average Star of reviews of all active users\n\
>>OPTION 3: Change over time in given stars by longest running elite user\n\
>>QUIT: Quit application\n\n>> ")

# top/worst businesses acc. to city
if option == "1":
        opt1 = raw_input("Select by 'STARS' or 'REVIEW COUNT'?\n>> ")
        input_city = raw_input("Enter city: ")
        if "STARS" in opt1:
                print("test")

                min_stars_business = cur.execute("SELECT MIN(STARS) FROM BUSINESS WHERE CITY = "+input_city)

                max_stars = cur.execute("SELECT MAX(STARS) FROM BUSINESS WHERE CITY = "+input_city)
                
                opt1_city = con.cursor()
                print("Worst business(es) by star rating in", input_city, "is", opt1_city.execute("SELECT NAME_DESC, FULL_ADDRESS, CITY, STATE FROM BUSINESS WHERE input_city = CITY AND min_stars = STARS"))
                print("Top business(es) by star rating in", input_city, "is", opt1_city.execute("SELECT NAME_DESC, FULL_ADDRESS, CITY, STATE FROM BUSINESS WHERE input_city = CITY AND max_stars = STARS"))
                raw_input(">>REVIEW COUNT: View top/worst businesses by review count\n>>OPTIONS MENU: View available options\n>>QUIT: Quit application")
                pass
        if "REVIEW COUNT" in raw_input():
                opt1_min = con.cursor()
                min_revct = opt1_min.execute("SELECT MIN(REVIEW_COUNT) FROM BUSINESS WHERE input_city = CITY")
                opt1_max = con.cursor()
                max_revct = opt1_max.execute("SELECT MAX(REVIEW_COUNT) FROM BUSINESS WHERE input_city = CITY")
                
                opt1_city = con.cursor()
                print("Worst business(es) by review count in", input_city, "is", opt1_city.execute("SELECT NAME_DESC, FULL_ADDRESS, CITY, STATE FROM BUSINESS WHERE input_city = CITY AND min_revct = REVIEW_COUNT"))
                print("Top business(es) by review count in", input_city, "is", opt1_city.execute("SELECT NAME_DESC, FULL_ADDRESS, CITY, STATE FROM BUSINESS WHERE input_city = CITY AND max_revct = REVIEW_COUNT"))		
                raw_input(">>STARS: top/worst businesses by stars\n>>OPTIONS MENU: see available options\nQUIT: Quit application")
        if "OPTIONS MENU" in raw_input():
                print(option)
        if "QUIT" in raw_input():
                print("Quitting application")
                opt1_max.close()
                opt1_min.close()
                opt1_city.close()
                con.close()

# avg stars of reviews of all active users
#if option == "OPTION 2":

# change in given stars by longest running elite user
#if option == "OPTION 3":

