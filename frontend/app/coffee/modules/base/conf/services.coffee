kquotes = @kquotes


defaults = {
    api: "http://localhost:8000/api/v1/"
    debug: true
    lang: "en"
}


class ConfigurationService extends kquotes.Service
    @.$inject = ["localconf"]

    constructor: (localconf) ->
        @.config = _.merge(_.clone(defaults, true), localconf)

    get: (key, defaultValue=null) ->
        if _.has(@.config, key)
            return @.config[key]
        return defaultValue


module = angular.module("kquotesBase")
module.service("$kqConfig", ConfigurationService)

module.value("localconf", null)

