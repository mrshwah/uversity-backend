from models.reviews import Review


#   Create Review
def create_review(review_args):
    review = Review(comment=review_args['comment'],
                    poster_id=review_args['poster_id'],
                    instructor_id=review_args['instructor_id'],
                    class_name=review_args['class_name'],
                    environment_rating=review_args['environment_rating'],
                    organization_rating=review_args['organization_rating'],
                    clarity_rating=review_args['clarity_rating'],
                    expertise_rating=review_args['expertise_rating'])
    review.save()
    return review.to_dict()


#   Delete Review
def delete_review(review_args):
    review = Review.objects(id__exists=review_args['id'])
    review.delete()
