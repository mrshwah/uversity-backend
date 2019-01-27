from models.categories import Category


def get_categories():
    categories = Category.objects()
    categories = [category.to_dict() for category in Category.objects()]
    return categories

