kquotes = @kquotes
bindMethods = kquotes.bindMethods


module = angular.module("kquotesProfile")


class HomeController extends kquotes.Controller
    @.$inject = [
        "$log"
        "$rootScope"
        "$scope"
        "$kqResources"
        "$q"
    ]
    constructor: (@log, @rootScope, @scope, @rs, @q) ->
        bindMethods(@)
        @.loadInitialData()

    loadQuotes: ->
        return @rs.quotes.list().then (quotes) =>
            @scope.quotes = quotes
            return quotes

    loadOrganizations: ->
        return @rs.organizations.list().then (organizations) =>
            @scope.organizations = organizations
            return organizations

    loadInitialData: ->
        @q.all([@.loadQuotes(),
                @.loadOrganizations])


module.controller("HomeController", HomeController)
