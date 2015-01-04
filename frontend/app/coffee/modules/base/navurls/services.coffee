kquotes = @kquotes
trim = kquotes.trim


class NavigationUrlsService extends kquotes.Service
    constructor: ->
        @.urls = {}

    update: (urls) ->
        @.urls = _.merge({}, @.urls, urls or {})

    formatUrl: (url, ctx={}) ->
        replacer = (match) ->
            match = trim(match, ":")
            return ctx[match] or "undefined"
        return url.replace(/(:\w+)/g, replacer)

    resolve: (name, ctx) ->
        url = @.urls[name]
        return "" if not url
        return @.formatUrl(url, ctx) if ctx
        return url


module = angular.module("kquotesBase")
module.service("$kqNavUrls", NavigationUrlsService)
