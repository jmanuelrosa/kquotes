@kquotes = kquotes = {}


############################
## Load Modules
###########################

modules = [
    # Main Global Modules
    "kquotesBase"
    "kquotesResources"

    # Specific Modules
    "kquotesAuth"

    # Vendor modules
    "ngRoute"
    "ngSanitize"
    "ngAnimate"
    "ngMaterial"
]

module = angular.module("kquotes", modules)


############################
## Configuration
###########################

configure = ($routeProvider, $locationProvider, $httpProvider, $provide) ->
    $routeProvider.when("/",
        {templateUrl: "/partials/home.html"})
    $routeProvider.when("/org/:slug",
        {templateUrl: "/partials/organization-home.html"})

    ## Auth
    $routeProvider.when("/login/",
        {templateUrl: "/partials/login.html",})

    ## Errors/Exceptions
    $routeProvider.when("/error",
        {templateUrl: "/partials/err/error.html"})
    $routeProvider.when("/not-found",
        {templateUrl: "/partials/err/not-found.html"})
    $routeProvider.when("/permission-denied",
        {templateUrl: "/partials/err/permission-denied.html"})

    $routeProvider.otherwise({redirectTo: '/not-found'})
    $locationProvider.html5Mode({enabled: true, requireBase: false})

    defaultHeaders = {
        "Content-Type": "application/json"
        "Accept-Language": "en"
    }

    $httpProvider.defaults.headers.delete = defaultHeaders
    $httpProvider.defaults.headers.patch = defaultHeaders
    $httpProvider.defaults.headers.post = defaultHeaders
    $httpProvider.defaults.headers.put = defaultHeaders
    $httpProvider.defaults.headers.get = {}

    # Add next param when user try to access to a secction need auth permissions.
    authHttpIntercept = ($q, $location, $navUrls) ->
        httpResponseError = (response) ->
            if response.status == 0
                $location.path($navUrls.resolve("error"))
                $location.replace()
            else if response.status == 401 or
                    response.status == 403
                nextPath = $location.path()
                $location.url($navUrls.resolve("login")).search("next=#{nextPath}")
            return $q.reject(response)

        return {responseError: httpResponseError}

    $provide.factory("authHttpIntercept", ["$q", "$location", "$kqNavUrls", authHttpIntercept])
    $httpProvider.interceptors.push('authHttpIntercept')

module.config(["$routeProvider", "$locationProvider", "$httpProvider", "$provide",  configure])


############################
## Initialize
###########################

init = ($log) ->
    $log.info """
                       Wellcome to kQuotes
                       -------------------

                   .-=-.
                 .'     \\        pio
              __.|    9 )_\\  pio         .-=-.
         _.-''          /              _/     `.
      <`'     ..._    <'              /_( 9    |.__
       `._ .-'    `.  |        pio      \\          ``-._
        ; `.    .-'  /            pio    `>    _...     `'>
         \\  `~~'  _.'                     |  .'    `-. _,'
          `"..."'% _                       \\ `-.    ,' ;
            \\__  |`.                        `.  `~~'  /
            /`.                             _ 7`"..."'
                                            ,'| __/
                                        hjw     ,'\
    """
module.run(["$log", init])
