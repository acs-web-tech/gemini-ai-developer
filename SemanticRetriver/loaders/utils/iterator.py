def document_iterator(iterator):
    result  = map(lambda value:{"data":value.page_content},iterator)
    return list(result)