from models.reviews import Review


def get_aggregate(instructor_id):
    aggregate = {'total': 0,'environment_rating': 0, 'organization_rating': 0, 'clarity_rating': 0, 'expertise_rating': 0}
    reviews = [review for review in Review.objects(instructor=instructor_id)]

    count = len(reviews)

    if count is 0:
        return {'total': 0, 'environment_rating': 0, 'organization_rating': 0, 'clarity_rating': 0, 'expertise_rating': 0}

    for review in reviews:
        aggregate['total'] = aggregate['total'] + review.aggregate_rating
        aggregate['environment_rating'] = aggregate['environment_rating'] + review.environment_rating
        aggregate['organization_rating'] = aggregate['organization_rating'] + review.organization_rating
        aggregate['clarity_rating'] = aggregate['clarity_rating'] + review.clarity_rating
        aggregate['expertise_rating'] = aggregate['expertise_rating'] + review.expertise_rating

    for key in aggregate.keys():
        aggregate[key] = format((aggregate[key] / count), '.1f')

    return aggregate
