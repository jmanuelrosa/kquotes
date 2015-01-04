resourceProvider = ($repo) ->
    service = {}

    return (instance) ->
        instance.auth = service


module = angular.module("kquotesResources")
module.factory("$kqAuthResourcesProvider", ["$kqRepo", resourceProvider])
