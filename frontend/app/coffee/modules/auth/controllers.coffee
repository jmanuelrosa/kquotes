kquotes = @kquotes
bindMethods = kquotes.bindMethods


module = angular.module("kquotesAuth")


class LoginController extends kquotes.Controller
    @.$inject = [
        "$log"
        "$rootScope"
        "$scope"
        "$routeParams"
        "$kqAuth"
        "$kqLocation"
        "$kqNavUrls"
    ]
    constructor: (@log, @rootScope, @scope, @routeParams, @auth, @location, @navUrls) ->
        bindMethods(@)

    submitLogin: ->
        onSuccess = (data) =>
            if @routeParams["next"] and @routeParams["next"] != @navUrls.resolve("login")
                nextUrl = @routeParams["next"]
            else
                nextUrl = @navUrls.resolve("home")
            @location.path(nextUrl)

        onError = (data) =>
            @log.debug "TODO: Catch login errors"

        username = @scope.username
        password = @scope.password
        @auth.login(username, password).then(onSuccess, onError)

module.controller("LoginController", LoginController)
