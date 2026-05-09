fruit_flavors_candy = ("marshmallows", "jelly", "lollipop")
fruity_flavors = ("banana", "mango", "grape")

candy_set = {fruit_flavors_candy[2] + " " + 
             fruity_flavors[1], 
             fruit_flavors_candy[0] + " " + 
             fruity_flavors [1],
             fruit_flavors_candy[1] + " " +
             fruity_flavors[0]
}

print("Today’s candy options include:")
print(candy_set)

# When printing the output multiple times, the order chages. It doesn't have a specific order since it it set. 