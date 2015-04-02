# project
import sys
import cx_Oracle

con = cx_Oracle.connect('C##cs329e_php274/C##cs329e_php274@129.152.144.84:1521/ORCL')

option = raw_input("== YELP ACADEMIC DATASET ==\nChoose one of the following options below (e.g. 'OPTION 1'):\n>>OPTION 1: Top-rated/worst-rated businesses according to city\n>>OPTION 2: Average Star of reviews of all active users\n>>OPTION 3: Change over time in given stars by longest running elite user\n>>QUIT: Quit application")

# top/worst businesses acc. to city
if option == "OPTION 1":
	opt1 = raw_input("Select by 'STARS' or 'REVIEW COUNT'?")
	input_city = raw_input("Enter city:")
	if "STARS" in raw_input():
		opt1_min = con.cursor()
		min_stars = opt1_min.execute("SELECT MIN(STARS) FROM BUSINESS WHERE input_city = CITY")
		opt1_max = con.cursor()
		max_stars = opt1_max.execute("SELECT MAX(STARS) FROM BUSINESS WHERE input_city = CITY")

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

