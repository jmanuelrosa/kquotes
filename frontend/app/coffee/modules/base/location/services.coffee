
locationFactory = ($location, $route) ->
    $location.noreload =  (scope) ->
        lastRoute = $route.current
        un = scope.$on "$locationChangeSuccess", ->
            $route.current = lastRoute
            un()

        return $location
    return $location


module = angular.module("kquotesBase")
module.factory("$kqLocation", ["$location", "$route", locationFactory])