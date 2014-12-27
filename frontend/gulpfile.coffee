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
    js: []
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
