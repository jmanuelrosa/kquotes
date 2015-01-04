kquotes = @kquotes


class ResourcesService extends kquotes.Service

module = angular.module("kquotesResources")
module.service("$kqResources", ResourcesService)


# Initialize resources service populating it with methods
# defined in separated files.
initResources = ($log, $rs) ->
    $log.debug "[kqResources] Initialize resources providers"
    providers = _.toArray(arguments).slice(2)

    for provider in providers
        provider($rs)


# Module entry point
module.run([
    "$log"
    "$kqResources"

    # Providers
    "$kqAuthResourcesProvider"
    "$kqUsersResourcesProvider"

    initResources
])
