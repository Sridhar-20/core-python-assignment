def total_cost(card):
    total=sum(card.values())
    if len(card)>5:
        total=total*0.9
    return f"Total Price: {int(total)}"

card={'labtop':50000,'Headphones':2000,'Mouse':500,'Keyboard':1500}
print(total_cost(card))