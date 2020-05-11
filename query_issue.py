query_issue = """
query { 
repository(name:"%s",owner:"%s"){
        issues(first: 100 %s) {
        totalCount
        pageInfo {
                hasNextPage
                endCursor
            } 
            nodes {
                number
                id
                comments {
                    totalCount
                }
                title
              createdAt
              closedAt
              
            }
        }
    }
}
"""
