gulp = require "gulp"

paths = {
    app: "app/"
    dist: "dist/"
    tmp: "tmp/"
    jade: [
        "app/index.jade"
        "app/partials/**/*.jade"
    ]
    sass: []
    coffee: ["app/coffee/**/*.coffee"]
    css: [
        "bower_components/angular-material/angular-material.css"        # angular-material
    ]
    js: [
        "bower_components/jquery/dist/jquery.js"                        # jquery
        "bower_components/lodash/dist/lodash.js"                        # lodash
        "bower_components/underscore.string/lib/underscore.string.js"   # underscore.string
        "bower_components/moment/moment.js"                             # moment
        "bower_components/angular/angular.js"                           # angular
        "bower_components/angular-route/angular-route.js"               # angular-route
        "bower_components/angular-loader/angular-loader.js"             # angular-loader
        "bower_components/angular-animate/angular-animate.js"           # angular-animate
        "bower_components/angular-sanitize/angular-sanitize.js"         # angular-sanitize
        "bower_components/angular-mocks/angular-mocks.js"               # angular-mocks
        "bower_components/angular-aria/angular-aria.js"                 # angular-material
        "bower_components/angular-material/angular-material.js"         # angular-material
    ]
}


gulp.task "_dev-server", ->
    express = require "express"
    app = express()

    #app.use("/js", express.static("#{__dirname}/dist/js"))
    #app.use("/styles", express.static("#{__dirname}/dist/styles"))
    #app.use("/images", express.static("#{__dirname}/dist/images"))
    #app.use("/svg", express.static("#{__dirname}/dist/svg"))
    #app.use("/partials", express.static("#{__dirname}/dist/partials"))
    #app.use("/fonts", express.static("#{__dirname}/dist/fonts"))

    app.all "/*", (req, res, next) ->
        # Just send the index.html for other files to support HTML5Mode
        res.sendFile("index.html", {root: "#{__dirname}/dist/"})

    app.listen(9001)


gulp.task "default", [
    "_dev-server"
]
