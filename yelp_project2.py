# project
import cx_Oracle, sys

def lister(name):
        name = list(name)
        name = name[0][0]
        
def main():
        
        con = cx_Oracle.connect('om', 'om', 'xe')
        cur = con.cursor()


        quit = False
        while quit == False:

                option = raw_input("== YELP ACADEMIC DATASET ANALYTICS TOOL ==\n\
Choose one of the following options below (e.g. '3'):\n\
>>OPTION 1: Categorical breakdown by city of stars by review count\n\
>>OPTION 2: Categorical breakdown by city of reviews by review count\n\
>>OPTION 3: Average rating by franchise\n\
>>OPTION 4: Average rating across all users\n\
>>OPTION 5: Categorical count distribution by average stars for all users\n\
>>OPTION 6: Average stars by year for a particular user\n\
>>QUIT: Quit application\n\n>> ")

                if option == "1":
                        input_city = raw_input("Enter city name: ")
                        input_city = input_city.rstrip('\n')

                        star_distribution = cur.execute("SELECT COUNT(*) AS STAR_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' GROUP BY STARS ORDER BY STARS")
                        star_distribution = list(star_distribution)

                        star_1 = star_distribution[0][0]
                        star_15 = star_distribution[1][0]
                        star_2 = star_distribution[2][0]
                        star_25 = star_distribution[3][0]
                        star_3 = star_distribution[4][0]
                        star_35 = star_distribution[5][0]
                        star_4 = star_distribution[6][0]
                        star_45 = star_distribution[7][0]
                        star_5 = star_distribution[8][0]

                        star_list = ['1  ','1.5','2  ','2.5','3  ','3.5','4  ','4.5','5  ']
                        
                        avg_stars = cur.execute("SELECT COUNT(*) AS CITY_REVIEW_COUNT FROM BUSINESS WHERE CITY = \'"+input_city+"\'")
                        avg_stars = list(avg_stars)
                        avg_stars = avg_stars[0][0]

                        avg_stars = float(avg_stars)

                        

                        print("Rating | Total Reviews in Range | Percentile of Total")

                        for i in range(len(star_distribution)):
                                star = star_distribution[i][0]
                                
                                print("  %s            %d                    %.2f"%(star_list[i], star, (float(star)/avg_stars)*100))
                                

                        break_loop = raw_input("Press any key to continue.....")
                

                if option == "2":

                        input_city = raw_input("Enter city name: ")
                        input_city = input_city.rstrip('\n')
                        
                        rev_count_100 = cur.execute("SELECT \'100\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT < 101 GROUP BY \'100\'")
                        rev_count_100 = list(rev_count_100)
                        rev_count_100 = rev_count_100[0][1]

                        
                        rev_count_200 = cur.execute("SELECT \'200\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 101 AND 200 GROUP BY \'200\'")
                        rev_count_200 = list(rev_count_200)
                        rev_count_200 = rev_count_200[0][1]


                        #FINISH SQL VARIABLES
                        rev_count_300 = cur.execute("SELECT \'300\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 201 AND 300 GROUP BY \'300\'")
                        rev_count_300 = list(rev_count_300)
                        rev_count_300 = rev_count_300[0][1]
                        
                        rev_count_400 = cur.execute("SELECT \'400\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 301 AND 400 GROUP BY \'400\'")
                        rev_count_400 = list(rev_count_400)
                        rev_count_400 = rev_count_400[0][1]
                        
                        rev_count_500 = cur.execute("SELECT \'500\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 401 AND 500 GROUP BY \'500\'")
                        rev_count_500 = list(rev_count_500)
                        rev_count_500 = rev_count_500[0][1]
                        
                        rev_count_600 = cur.execute("SELECT \'600\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 501 AND 600 GROUP BY \'600\'")
                        rev_count_600 = list(rev_count_600)
                        rev_count_600 = rev_count_600[0][1]
                        
                        rev_count_700 = cur.execute("SELECT \'700\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 601 AND 700 GROUP BY \'700\'")
                        rev_count_700 = list(rev_count_700)
                        rev_count_700 = rev_count_700[0][1]
                        
                        rev_count_800 = cur.execute("SELECT \'800\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 701 AND 800 GROUP BY \'800\'")
                        rev_count_800 = list(rev_count_800)
                        rev_count_800 = rev_count_800[0][1]
                        
                        rev_count_900 = cur.execute("SELECT \'900\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 801 AND 900 GROUP BY \'900\'")
                        rev_count_900 = list(rev_count_900)
                        rev_count_900 = rev_count_900[0][1]
                        
                        rev_count_1000 = cur.execute("SELECT \'1000\' AS REVIEW_RANGE, COUNT(*) AS REVIEW_TOTAL FROM BUSINESS WHERE CITY = \'"+input_city+"\' and REVIEW_COUNT BETWEEN 901 AND 1000 GROUP BY \'1000\'")
                        rev_count_1000 = list(rev_count_1000)
                        rev_count_1000 = rev_count_1000[0][1]
                        

                        review_print_list = ["0-100","100-200","200-300","300-400","400-500","500-600","600-700","800-900","900-1000"]
                        review_count_list = [rev_count_100, rev_count_200, rev_count_300, rev_count_400, rev_count_500,rev_count_600,rev_count_700,rev_count_800,rev_count_900,rev_count_1000]
                        
                        rev_count_avg = cur.execute("SELECT COUNT(*) FROM BUSINESS WHERE CITY = \'"+input_city+"\'")
                        rev_count_avg = list(rev_count_avg)
                        rev_count_avg = rev_count_avg[0][0]
                        rev_count_avg = float(rev_count_avg)



                        #OUTPUT
                        print("Range | Number of Businesses | Percent of Total")
                        for i in range(len(review_count_list)-1):
                                print("  %s        %s                 %.2f"%(review_print_list[i], review_count_list[i], (float(review_count_list[i])/rev_count_avg)*100))


                        break_loop = raw_input("Press any key to continue.....")

                if option == "3":
                        franchise = raw_input("Enter franchise name: ")
                        franchise = franchise.rstrip('\n')

                        franch_avg_stars = cur.execute("SELECT AVG(STARS), COUNT(*) FROM BUSINESS WHERE NAME_DESC Like \'%"+franchise+"%\' ")
                        franch_avg_stars = list(franch_avg_stars)
                        franch_stars, franch_count = franch_avg_stars[0]

                        print("Average Rating for %s: %f"%(franchise, franch_stars))
                        print("Total Locations of %s Sampled: %d"%(franchise, franch_count))



                        break_loop = raw_input("Press any key to continue.....")

                if option == "4":

                        avg_all_users = cur.execute("SELECT AVG(AVERAGE_STARS) FROM USERS")
                        avg_all_users = list(avg_all_users)
                        avg_all_users = avg_all_users[0][0]

                        print("Average rating across all users: %s" %avg_all_users)

                        break_loop = raw_input("Press any key to continue.....")


                if option == "5":

                        avg_star_2 = cur.execute("SELECT AVG(REVIEW_COUNT) FROM USERS WHERE AVERAGE_STARS < 2")
                        avg_star_2 = list(avg_star_2)
                        avg_star_2 = avg_star_2[0][0]
                        
                        
                        avg_star_3 = cur.execute("SELECT AVG(REVIEW_COUNT) FROM USERS WHERE AVERAGE_STARS BETWEEN 2 AND 3")
                        avg_star_3 = list(avg_star_3)
                        avg_star_3 = avg_star_3[0][0]
                        
                        avg_star_4 = cur.execute("SELECT AVG(REVIEW_COUNT) FROM USERS WHERE AVERAGE_STARS BETWEEN 3 AND 4")
                        avg_star_4 = list(avg_star_4)
                        avg_star_4 = avg_star_4[0][0]
                        
                        avg_star_5 = cur.execute("SELECT AVG(REVIEW_COUNT) FROM USERS WHERE AVERAGE_STARS BETWEEN 4 AND 5")
                        avg_star_5 = list(avg_star_5)
                        avg_star_5 = avg_star_5[0][0]

                        #OUTPUT
                        print("Rating Range | Average Review Count")
                        print("   < 2              %f"%(avg_star_2))
                        print("  2 - 3             %f"%(avg_star_3))
                        print("  3 - 4             %f"%(avg_star_4))
                        print("  4 - 5             %f"%(avg_star_5))
                        
                
                        break_loop = raw_input("Press any key to continue.....")
                        
                if option == "6":
                        
                        #user_id for demo: kGgAARL2UmvCcTRfiscjug
                        user_id = raw_input("Enter user_id: ")
                        user_id = user_id.rstrip('\n')


                        user_by_year = cur.execute("SELECT AVG(STARS), to_char(REVIEW_DATE, \'YYYY\') AS REVIEW_YEAR FROM REVIEWS WHERE USER_ID = \'"+user_id+"\' GROUP BY to_char(REVIEW_DATE, \'YYYY\') ORDER BY REVIEW_YEAR")
                        user_by_year = list(user_by_year)

                        print("")
                        print("REVIEW YEAR  |  AVERAGE RATING")
                        print("")
                        for i in range(len(user_by_year)):
                                user_avg_star, review_year = user_by_year[i]
                                print ("   %s         %s" %(review_year, user_avg_star))

                        break_loop = raw_input("Press any key to continue.....")
                    


                        

                if option == "quit" or option == "QUIT" or option == "Quit":
                        print("Quitting application")
                        cur.close()
                        quit = True
                        
"""
Slide: Title
Slide: Describe Yelp , ERD
Slide: Describe approach of devloping a tool to analze relational information
Slide: DEMO
SLIDE: TABLEU graphs
Slide: Unexpected issues, review table, recsv editor, cleaning data up
Slide: possible extensions, adding more functionality andmore analysis tools, add data visualization functionality directly from app, export findings
Slide: CLOSING, QUESTIONS?
"""


main()
