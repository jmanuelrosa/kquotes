resourceProvider = ($repo) ->
    service = {}

    service.get = (organizationId) ->
        params = {}
        return $repo.queryOne("organizations", organizationId, params)

    service.list = () ->
        params = {}
        return $repo.queryMany("organizations", params)

    return (instance) ->
        instance.organizations = service


module = angular.module("kquotesResources")
module.factory("$kqOrganizationsResourcesProvider", ["$kqRepo", resourceProvider])
