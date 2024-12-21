def rating_per(ratings):
    if not ratings:
        return "No ratings avalible"

    count=0
    for rating in ratings:
        if rating>=4:
            count=count+1
    percentage=count/len(ratings)*100
    return f"Positive Feedback: {percentage}"


ratings=[5,4,3,5,2,4,1,5]
print(rating_per(ratings))