module = angular.module("kquotesResources")


urls = {
    "auth": "/auth/token/"
    "organizations": "/organizations/"
    "quotes": "/quotes/"
    "users": "/users/"
}

# Initialize api urls service
initUrls = ($log, $urls) ->
    $log.debug "[kqResources] Initialize api urls"
    $urls.update(urls)

module.run(["$log", "$kqUrls", initUrls])
