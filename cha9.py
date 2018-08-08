print("-----1-----")
#with open("loop.py", "r") as f:
#	print(f.read())


###
print("-----2-----")
#my_list = []
#q = input("What color do you like?:")
#with open("answer.txt", "a") as f:
#	answer = f.write(q + ",")
#	my_list.append(answer)


###
print("-----3-----")
import csv
movies = [["Top Gun", "Risky Business", "Minority Repeat"], \
         ["Titanic", "The Revenant", "Inception"], \
         ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w", newline='') as moviefile:
	temp = csv.writer(moviefile, delimiter=",")
	for movie_list in movies:
		temp.writerow(movie_list)