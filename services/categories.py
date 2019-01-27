from models.categories import Category as categories


def get_categories():
    return categories.to_dict()

