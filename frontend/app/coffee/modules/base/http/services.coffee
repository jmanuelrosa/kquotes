kquotes = @kquotes


class HttpService extends kquotes.Service
    @.$inject = ["$http", "$kqStorage"]

    constructor: (@http, @storage) ->
        super()

    headers: ->
        token = @storage.get('token')
        if token
            return {"Authorization": "JWT #{token}"}
        return {}

    request: (options) ->
        options.headers = _.merge({}, options.headers or {}, @.headers())
        if _.isPlainObject(options.data)
            options.data = JSON.stringify(options.data)

        return @http(options)

    get: (url, params, options) ->
        options = _.merge({method: "GET", url: url}, options)
        options.params = params if params
        return @.request(options)

    post: (url, data, params, options) ->
        options = _.merge({method: "POST", url: url}, options)
        options.data = data if data
        options.params = params if params
        return @.request(options)

    put: (url, data, params, options) ->
        options = _.merge({method: "PUT", url: url}, options)
        options.data = data if data
        options.params = params if params
        return @.request(options)

    patch: (url, data, params, options) ->
        options = _.merge({method: "PATCH", url: url}, options)
        options.data = data if data
        options.params = params if params
        return @.request(options)

    delete: (url, data, params, options) ->
        options = _.merge({method: "DELETE", url: url}, options)
        options.data = data if data
        options.params = params if params
        return @.request(options)


module = angular.module("kquotesBase")
module.service("$kqHttp", HttpService)
