kquotes = @kquotes


class AuthService extends kquotes.Service
    @.$inject = [
        "$rootScope"
        "$kqStorage"
        "$kqModel"
        "$kqResources"
    ]

    constructor: (@rootScope, @storage, @model, @rs) ->
        super()

    getUser: ->
        if @rootScope.user
            return @rootScope.user

        userData = @storage.get("userInfo")
        if userData
            user = @model.make_model("users", userData)
            @rootscope.user = user
            return user

        return null

    setUser: (user) ->
        @rootScope.auth = user
        @storage.set("userInfo", user.getAttrs())
        @rootScope.user = user

    clear: ->
        @rootScope.auth = null
        @rootScope.user = null
        @storage.remove("userInfo")

    setToken: (token) ->
        @storage.set("token", token)

    getToken: ->
        return @storage.get("token")

    removeToken: ->
        @storage.remove("token")

    isAuthenticated: ->
        if @.getUser() != null
            return true
        return false

    login: (username, passowrd) ->
        @.logout()

        return @rs.auth.login(username, passowrd).then (data) =>
            user = @model.make_model("users", data.data)
            @.setUser(user)
            @.setToken(user.auth_token)
            return user

    logout: ->
        @.removeToken()
        @.clear()


module = angular.module("kquotesAuth")
module.service("$kqAuth", AuthService)
