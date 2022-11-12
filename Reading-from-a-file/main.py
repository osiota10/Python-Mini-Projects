file = open("document.txt").readlines()
length = len(file)

start = 0
end = 0

for line in file:
    if line.startswith("NOTABLE PRODUCTS"):
        start = file.index(line)

    if line.startswith("OVERVIEW"):
        end = file.index(line)

# List slice
list_of_products_slice = file[start + 2:end - 1]

# List of Products
list_of_products = []
for item in list_of_products_slice:
    list_of_products.append(item.splitlines())


new_list = []
for items in list_of_products:
    for item in items:
        start = 0
        end = 0
        if "(" in item:
            start = item.index("(")

        if ")" in item:
            end = item.index(")")

        items_sold_in_words = item[start + 1:end]
        item_name = item[:start - 1]

        if "sold" in items_sold_in_words:
            items_sold_in_words = items_sold_in_words.replace("sold", "")

        # Get the price figure
        price = items_sold_in_words.split()
        price_converted = float(price[0])

        # price conversion
        price_in_figure = 0
        if "thousand" in items_sold_in_words:
            price_in_figure = price_converted * 1000
        elif "million" in items_sold_in_words:
            price_in_figure = price_converted * 1000000
        else:
            pass

        # create a dictionary
        def create_dict(*args):
            return dict(((k, eval(k)) for k in args))
        d = create_dict('item_name', 'price_in_figure', 'items_sold_in_words')

        new_list.append(d)

# list in ascending according price
sorted_new_list = sorted(new_list, key=lambda x: x['price_in_figure'], reverse=True)


# top five selling products
top_five_products = sorted_new_list[:5]
for products in top_five_products:
    number_of_item = top_five_products.index(products) + 1
    print(f"{number_of_item} {''} {products['item_name']}")

# accepting input
value = int(input('Enter a value from 1 to 5: '))
if value <= len(top_five_products):
    individual_item = top_five_products[value - 1]
    individual_item_index = top_five_products.index(individual_item)

    if value - 1 == individual_item_index:
        print(f"{'ACT '}{individual_item['item_name']} {'has sold'} {individual_item['items_sold_in_words']}{'units'}")
else:
    print("Enter a number from 1 to 5")
