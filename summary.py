import seaborn as sns
import matplotlib.pyplot as plt
import ex_1
import ex_2
import ex_3
import ex_4

def choose_option():
    options = ["Which brewery produces the strongest beers by abv?"
               , "If you had to pick 3 beers to recommend to someone, how would you approach the problem ?"
               , "What are the factors that impacts the quality of beer the most ?"
               , "I enjoy a beer which aroma and appearance matches the beer style. What beer should I buy ?"]
    print("Please choose one of the following options:")
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                print(f"You chose: {options[choice - 1]}")
                choice
                break
            else:
                print("Invalid choice. Please choose a number from the list.")
        except ValueError:

            print("Invalid input. Please enter a number.")
    return choice

choice_no = choose_option()


print("Assumptions:")
print("1. I take into consideration the newest row taking review_time")
print("2. If there are some NaN value I drop the row")
# print(choice_no)

if choice_no == 1 :
    print('Question:')
    print('Which brewery produces the strongest beers by abv ?')

    print("Conclusion:")
    print("1. The strongest beer is produced in brewery 6513 (Schorschbräu)")
    print("2. I tried with standard stats to calculate average for each brewery - the result is the same. Brewery Schorschbräu produces the strongest beer within the dataset ")
    print("below the result of stats:")

    ax = sns.barplot(x='brewery_id', y='beer_abv', hue = 'stats', data=ex_1.df_agg_stats)
    ax.set_title('top 5 beer abv stats')
    ax.bar_label(ax.containers[0], fontsize=10)
    ax.bar_label(ax.containers[1], fontsize=10)
    plt.show()

elif choice_no == 2:
    print('Question:')
    print('If you had to pick 3 beers to recommend to someone, how would you approach the problem ?')

    print("Additional assumptions:")
    print("I would like to invite you to a trip where you could try 3 different types of beers.")
    print("According to the testing rules, I picked 3 different kinds and 3 different abv.")
    print("Let's start from the beginning...  ")
    print("All beers have the best scoring in all categories, so no need to worry about some failures")
    print("I decided to consider the highest number of row per each beer category, thats why ...")

    print(ex_2.df_agg_2)

    print("I choose: American Double / Imperial Stout, American Black Ale, Lambic - Unblended  ")

    print("We'll start with low abv and lager,so Lambic - Unblended")
    print(print(ex_2.choose_lambic))
    print("I choose the highest total with is the sum of all category rates and the newest review")
    print("Conclusion: I choose Lambic - Unblended from Brasserie Cantillon brewery with 5 abv")

    print("Now let's see the type with the highest number of review: American Double / Imperial Stout, the strongest one (max of abv for this category).")
    print("I chose American Double / Imperial Stout from SweetWater Brewing Company brewery with 13 abv")
    print(ex_2.choose_staut)

    print("The last one is American Black Ale, because it has good score and many reviewers.")
    print("I choose the newest data to make sure that review is the most actual")
    print("I chose merican Black Ale from SweetWater Brewing Company brewery with 9 abv.")
    print(ex_2.choose_ais)

elif choice_no == 3:
    print('Question:')
    print('What are the factors that impacts the quality of beer the most ?')

    print('I create correlation matrix and heat map:')
    sns.heatmap(ex_3.corr_matrix)
    plt.show()

    print('heat map shows that factors that impact the most of beer quality are: taste and palete')
    print('the highest score of those categories the highest overall score')

elif choice_no == 4:
    print('Question:')
    print('I enjoy a beer which aroma and appearance matches the beer style. What beer should I buy ?')

    print("Additional assumptions:")
    print("I chose all data with the highest score on aroma and appearance.")
    print("There are many options, but I would like to suggest you a Fruit / Vegetable Beer from the best (in terms of overall rate's mean ) brewery - they are my favourite and unique.")
    print(ex_4.best)

    print("I would suggest Raspberry Icee Black from Dark Horse Brewing Company")



