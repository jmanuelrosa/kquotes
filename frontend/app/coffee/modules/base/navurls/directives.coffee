kquotes = @kquotes
trim = kquotes.trim
bindOnce = kquotes.bindOnce


NavigationUrlsDirective = ($navUrls, $auth, $q, $location) ->
    # Example:
    # link(kq-nav="organization:slug='sss',")

    # bindOnce version that uses $q for offer
    # promise based api
    bindOnceP = ($scope, attr) ->
        defered = $q.defer()
        bindOnce $scope, attr, (v) ->
            defered.resolve(v)
        return defered.promise

    parseNav = (data, $scope) ->
        [name, params] = _.map(data.split(":"), trim)
        if params
            params = _.map(params.split(","), trim)
        else
            params = []
        values = _.map(params, (x) -> trim(x.split("=")[1]))
        promises = _.map(values, (x) -> bindOnceP($scope, x))

        return $q.all(promises).then ->
            options = {}
            for item in params
                [key, value] = _.map(item.split("="), trim)
                options[key] = $scope.$eval(value)
            return [name, options]

    link = ($scope, $el, $attrs) ->
        if $el.is("a")
            $el.attr("href", "#")

        $el.on "mouseenter", (event) ->
            target = $(event.currentTarget)

            if !target.data("fullUrl")
                parseNav($attrs.kqNav, $scope).then (result) ->
                    [name, options] = result
                    user = $auth.getUser()
                    options.user = user.username if user

                    url = $navUrls.resolve(name)
                    fullUrl = $navUrls.formatUrl(url, options)

                    target.data("fullUrl", fullUrl)

                    if target.is("a")
                        target.attr("href", fullUrl)

        $el.on "click", (event) ->
            event.preventDefault()
            target = $(event.currentTarget)

            if target.hasClass('noclick')
                return

            fullUrl = target.data("fullUrl")

            switch event.which
                when 1
                    $location.url(fullUrl)
                    $scope.$apply()
                when 2
                    window.open fullUrl

        $scope.$on "$destroy", ->
            $el.off()

    return {link: link}


module = angular.module("kquotesBase")
module.directive("kqNav", ["$kqNavUrls", "$kqAuth", "$q", "$kqLocation", NavigationUrlsDirective])
