kquotes = @kquotes


kquotes.bindMethods = (object) =>
    dependencies = _.keys(object)

    methods = []

    _.forIn object, (value, key) =>
        if key not in dependencies
            methods.push(key)

    _.bindAll(object, methods)


kquotes.bindOnce = (scope, attr, continuation) =>
    val = scope.$eval(attr)
    if val != undefined
        return continuation(val)

    delBind = null
    delBind = scope.$watch attr, (val) ->
        return if val is undefined
        continuation(val)
        delBind() if delBind


kquotes.mixOf = (base, mixins...) ->
    class Mixed extends base

    for mixin in mixins by -1 #earlier mixins override later ones
        for name, method of mixin::
            Mixed::[name] = method
    return Mixed


kquotes.trim = (data, char) ->
    return _.str.trim(data, char)


kquotes.slugify = (data) ->
    return _.str.slugify(data)


kquotes.unslugify = (data) ->
    if data
        return _.str.capitalize(data.replace(/-/g, ' '))
    return data
