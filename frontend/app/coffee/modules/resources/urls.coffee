module = angular.module("kquotesResources")


urls = {
    "auth": "/auth/token/"
    "users": "/users/"
}

# Initialize api urls service
initUrls = ($log, $urls) ->
    $log.debug "[kqResources] Initialize api urls"
    $urls.update(urls)

module.run(["$log", "$kqUrls", initUrls])
