resourceProvider = ($repo) ->
    service = {}

    service.get = (userId) ->
        params = {}
        return $repo.queryOne("users", userId, params)

    service.list = () ->
        params = {}
        return $repo.queryMany("users", params)

    return (instance) ->
        instance.users = service


module = angular.module("kquotesResources")
module.factory("$kqUsersResourcesProvider", ["$kqRepo", resourceProvider])
