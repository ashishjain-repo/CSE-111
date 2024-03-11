from datetime import datetime

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    fileContent = open(filename, 'r')
    content = fileContent.readlines()
    contentList = list()
    for line in content:
        contentList.append(line.strip().split(','))
    del contentList[0]
    PRODUCTS_DICT = dict()
    for lines in range(len(contentList)):
        PRODUCTS_DICT[contentList[lines][key_column_index]] = contentList[lines]
    return PRODUCTS_DICT


def main():
    filename = "products.csv"
    file = "request.csv"
    try:
        PRODUCTS_DICT = read_dictionary(filename, 0)
    except FileNotFoundError:
        print("Error: Missing file")
        print(f"[Errno 2] No such file or directory: '{filename}'")
        exit()
    listContent = open(file, 'r')
    content = listContent.readlines()
    contentList = []
    ESCAPE = 0
    for list in content:
        if ESCAPE == 0:
            ESCAPE+=1
            pass
        else:
            contentList.append(list.strip().split(','))
    cost = []
    quantity = []
    product = []
    for i in range(len(contentList)):
        # print(contentList[i][0])
        if contentList[i][0] in PRODUCTS_DICT:
            details = PRODUCTS_DICT.get(contentList[i][0])
            quantity.append(contentList[i][1])
            cost.append(details[2])
            product.append(details[1])
        else:
            print(f"Error: Unknown product ID in the '{file}' file\n'{contentList[i][0]}'")
            exit()

    print("Inkom Emporium\n")
    for items in range(len(quantity)):
        print(f"{product[items]}: {quantity[items]} @ {cost[items]}")
    total = 0
    numItems = 0
    for items in range(len(quantity)):
        total += (float(quantity[items]) * float(cost[items]))
        numItems+= int(quantity[items])

    current_date_and_time = datetime.now()
    hour = int(current_date_and_time.strftime("%I"))
    meridiem = current_date_and_time.strftime("%p")

    if hour <= 11 and meridiem == 'AM':
        discount = total-(total*0.1)
        salesTax = round(discount * 0.06, 2)
        final = round(salesTax + discount, 2)
        print("this")
    else:
        salesTax = round(total*0.06,2)
        final = round(salesTax+total,2)
    print(f"\nNumber of items: {numItems}")
    print(f"Subtotal: {round(total,2)}")
    print(f"Sales Tax: {salesTax}")
    print(f"Total: {round(final,2)}")
    formatted_date = current_date_and_time.strftime("%A %B %d %I:%M:%S %p %Y")

    print(f"\nThank you for shopping at the Inkom Emporium\n{formatted_date}")


if __name__ == "__main__":
    main()