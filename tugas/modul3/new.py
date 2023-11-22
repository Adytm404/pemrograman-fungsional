from functools import reduce

movies = [
    {
        "title": "Parasite",
        "year": 2019,
        "rating": 8.6,
        "genre": "Drama"
    },
    {
        "title": "Dune",
        "year": 2021,
        "rating": 7.9,
        "genre": "Sci-Fi"
    },
    {
        "title": "Eternals",
        "year": 2021,
        "rating": 6.4,
        "genre": "Action"
    },
    {
        "title": "Avengers: Endgame",
        "year": 2019,
        "rating": 8.4,
        "genre": "Action"
    },
    {
        "title": "Nomadland",
        "year": 2020,
        "rating": 7.3,
        "genre": "Drama"
    },
    {
        "title": "Spider-man: No Way Home",
        "year": 2021,
        "rating": 7.6,
        "genre": "Action"
    },
    {
        "title": "The French Dispatch",
        "year": 2021,
        "rating": 7.0,
        "genre": "Comedy"
    },
    {
        "title": "A Quiet Place Part II",
        "year": 2020,
        "rating": 7.4,
        "genre": "Horror"
    },
    {
        "title": "No Time to Die",
        "year": 2021,
        "rating": 6.8,
        "genre": "Action"
    },
    {
        "title": "The Power of the Dog",
        "year": 2021,
        "rating": 7.3,
        "genre": "Drama"
    },
    {
        "title": "The Last Duel",
        "year": 2021,
        "rating": 7.0,
        "genre": "Drama"
    }
]
 

def byGenre(data):
    result = {}
    temp = set(movie["genre"] for movie in data)
    for genre in temp:
        genreFilter = list(filter(lambda x: x["genre"] == genre, data))
        result[genre] = len(genreFilter)
    return result

def averageRating(data):
    temp = list(set(data["year"] for data in data))

    def ratingSum(year):
        movieFilter = list(filter(lambda x: x["year"] == year, data))
        ratingFilter = map(lambda x: x["rating"],movieFilter)
        totalSum = reduce(lambda x, y: x + y, ratingFilter)
        return totalSum

    def average(year):
        temp = list(filter(lambda x: x["year"] == year, data))
        totalSum = ratingSum(year)
        totalAverage = totalSum / len(temp)
        return year, totalAverage

    average_ratings = dict(map(average, temp))
    return average_ratings
    
def topRating(data):
    maxValue = reduce(lambda x,y: x if x > y else y, (movie["rating"] for movie in data))
    return list(filter(lambda x: x["rating"] == maxValue, data))

def searchMovie(data, input):
    return list(filter(lambda x: x["title"] == input, data))
    


def main():
    print("\n")
    print("1. Menghitung jumlah film berdasarkan genre")
    print("2. Menghitung rata-rata rating film berdasarkan tahun rilis")
    print("3. Menemukan film dengan rating tertinggi")
    print("4. Cari judul film untuk menampilkan informasi rating, tahun rilis, dan genre")
    print("5. Selesai")
    menu = input("Masukkan nomor tugas (1/2/3/4/5) : ")
    
    if(menu == "1"):
        print("Jumlah Film berdasarkan Genre:\n")
        print(byGenre(movies))
        main()
    elif(menu == "2"):
        print("Rata - rata Rating film berdasarkan tahun rilis\n")
        print(averageRating(movies))
        main()
    elif(menu == "3"):
        print("Film dengan Rating Tertinggi:\n")
        print(topRating(movies))
        main()
    elif(menu == "4"):
        film = input(str("Search by title : \n"))
        print(searchMovie(movies, film))
        main()
    else:
        print("Terimakasih")


if __name__ == "__main__":
   main()