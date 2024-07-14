def document_iterator(iterator):
    result  = map(lambda value:{"content":value.page_content,"metadata":value.metadata},iterator)
    return list(result)