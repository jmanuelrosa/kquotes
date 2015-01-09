resourceProvider = ($repo) ->
    service = {}

    service.get = (quoteId) ->
        params = {}
        return $repo.queryOne("quotes", quoteId, params)

    service.list = () ->
        params = {}
        return $repo.queryMany("quotes", params)

    return (instance) ->
        instance.quotes = service


module = angular.module("kquotesResources")
module.factory("$kqQuotesResourcesProvider", ["$kqRepo", resourceProvider])
