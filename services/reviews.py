from models.reviews import Review
from models.users import User


def calculate_aggregate(cla, env, exp, org):
    return (cla+env+exp+org)/4


#   Create Review
def create_review(review_args):
    poster = User.objects(eb_id=review_args['poster_id'])[0]

    review = Review(comment=review_args['comment'],
                    poster_id=poster,
                    instructor_id=review_args['instructor_id'],
                    class_name=review_args['class_name'],
                    environment_rating=review_args['environment_rating'],
                    organization_rating=review_args['organization_rating'],
                    clarity_rating=review_args['clarity_rating'],
                    expertise_rating=review_args['expertise_rating'])
    review.aggregate_rating = calculate_aggregate(review.clarity_rating,
                                                  review.environment_rating,
                                                  review.expertise_rating,
                                                  review.organization_rating)
    review.save()
    return review.to_dict()


def update_review(review_args):
    review = Review.objects.get(eb_id=review_args['id'])
    review.comment = review_args['comment']
    review.environment_rating = review_args['environment_rating']
    review.organization_rating = review_args['organization_rating']
    review.clarity_rating = review_args['clarity_rating']
    review.expertise_rating = review_args['expertise_rating']
    review.aggregate_rating = calculate_aggregate(review.clarity_rating,
                                                  review.environment_rating,
                                                  review.expertise_rating,
                                                  review.organization_rating)
    review.save()
    return review.to_dict()



#   Delete Review
def delete_review(review_args):
    review = Review.objects.get(review_args['id'])
    if review.delete():
        return {"message": "success!"}
    else:
        return {"message": "failed"}
