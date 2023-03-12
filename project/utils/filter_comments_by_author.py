def filter_comments_by_author(comments, author):
    filtered_comments = []
    for comment in comments:
        if comment.author_id == author.id:
            filtered_comments.append(comment)
    return filtered_comments
