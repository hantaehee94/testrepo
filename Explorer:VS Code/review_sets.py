"""
Python will automatically remove duplicate items in a set.
"""

# Create a set
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}

# Convert list to set
album_list = [ "The Bodyguard", "Thriller", 1982, "00:42:19",
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_list_set = set(album_list)
album_list_set

# add element to set
album_list_set.add("Jazz")
album_list_set

# remove element from set
album_list_set.remove("Jazz")
album_list_set

None in album_list_set

# intersection of two sets
set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
set2 = {"pop", "rock", "soul", "disco"}
intersection = set1 & set2
intersection
set1.intersection(set2)

# difference of two sets
set1.difference(set2)
set2.difference(set1)

# By using the union operation, we can create the union of set1 and set2. The result remains the same regardless of the order of the sets.
set1.union(set2)
set2.union(set1)

# Check if superset
set1.issuperset(set2)
set2.issuperset(set1)
