from models.reviews import Review


def get_aggregate(instructor_id):
    aggregate = 0;
    count = 0;
    reviews = [review.to_dict() for review in Review.objects(instructor=instructor_id)]

    for review in reviews:
        aggregate = aggregate + review.aggregate_rating

    aggregate = aggregate/count
    return aggregate
