query = """
    query{
      search(query: "stars:>100", type: REPOSITORY, first: 50 %s) {
        repositoryCount
        pageInfo {
          hasNextPage
          endCursor
        }   
        nodes {
          ... on Repository {
            name
            owner{login}
            url
            stargazers{totalCount}
            issues{totalCount}
            primaryLanguage {
              name
            }
          }
        }
      }
    
    }
"""