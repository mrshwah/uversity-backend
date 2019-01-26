from models.reviews import Review


def create_review(review_args):
    review = Review(comment=review_args['comment'], environment_rating=review_args['environment_rating'], organization_rating=review_args['organization_rating'], clarity_rating=review_args['clarity_rating'], expertise_rating=review_args['expertise_rating'])
    review.save()
    return review.to_dict()
