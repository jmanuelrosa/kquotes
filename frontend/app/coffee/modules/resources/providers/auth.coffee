resourceProvider = ($repo, $http, $urls) ->
    service = {}

    service.login = (username, password) ->
        url = $urls.resolve("auth")
        data = {username: username, password: password}
        return $http.post(url, data)

    return (instance) ->
        instance.auth = service


module = angular.module("kquotesResources")
module.factory("$kqAuthResourcesProvider", ["$kqRepo", "$kqHttp", "$kqUrls", resourceProvider])
