###############################
# Modules
###############################

module = angular.module("kquotesAuth", [])
module = angular.module("kquotesBase", [])
module = angular.module("kquotesResources", [])


###############################
# Nav urls
###############################

urls = {
    # Erors
    "error": "/error"
    "not-found": "/not-found"
    "permission-denied": "/permission-denied"

    # Auth
    "login": "/login"

    # Profile
    "profile-me": "/"

    # Organizations
    "org-home": "/org/:slug"

}

init = ($log, $navurls) ->
    $log.debug "Initialize navigation urls"
    $navurls.update(urls)

module.run(["$log", "$kqNavUrls", init])
