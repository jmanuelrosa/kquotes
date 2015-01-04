kquotes = @kquotes


format = (fmt, obj) ->
    obj = _.clone(obj)
    return fmt.replace /%s/g, (match) -> String(obj.shift())


class UrlsService extends kquotes.Service
    @.$inject = ["$kqConfig"]

    constructor: (@config) ->
        @.urls = {}
        @.mainUrl = @config.get("api")

    update: (urls) ->
        @.urls = _.merge(@.urls, urls)

    resolve: ->
        args = _.toArray(arguments)

        if args.length == 0
            throw Error("wrong arguments to setUrls")

        name = args.slice(0, 1)[0]
        url = format(@.urls[name], args.slice(1))

        return format("%s/%s", [
            _.str.rtrim(@.mainUrl, "/"),
            _.str.ltrim(url, "/")
        ])


module = angular.module("kquotesBase")
module.service('$kqUrls', UrlsService)
