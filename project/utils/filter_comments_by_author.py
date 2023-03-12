from models.user import User


def filter_comments_by_author(comments: list, author: User) -> list:
    filtered_comments: list = []
    for comment in comments:
        if comment.author_id == author.id:
            filtered_comments.append(comment)
    return filtered_comments
