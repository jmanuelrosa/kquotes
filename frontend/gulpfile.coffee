gulp                = require "gulp"
plumber             = require "gulp-plumber"
concat              = require "gulp-concat"
cache               = require "gulp-cached"
del                 = require "del"
watch               = require "gulp-watch"

jade                = require "gulp-jade"
jadeInheritance     = require "gulp-jade-inheritance"

coffee              = require "gulp-coffee"



paths = {
    app: "app/"
    dist: "dist/"
    tmp: "tmp/"
    jade: {
        index: "app/index.jade"
        partials: "app/partials/**/*.jade"
    }
    sass: []
    coffee: [
        "app/coffee/app.coffee"
        "app/coffee/utils..coffee"
        "app/coffee/**/*.coffee"
    ]
    css: [
        "bower_components/angular-material/angular-material.css"        # angular-material
    ]
    js: [
        "bower_components/hammerjs/hammer.js"                           # hammerjs
        "bower_components/jquery/dist/jquery.js"                        # jquery
        "bower_components/lodash/dist/lodash.js"                        # lodash
        "bower_components/moment/moment.js"                             # moment
        "bower_components/underscore.string/lib/underscore.string.js"   # underscore.string
        "bower_components/angular/angular.js"                           # angular
        "bower_components/angular-animate/angular-animate.js"           # angular-animate
        "bower_components/angular-aria/angular-aria.js"                 # angular-arial
        "bower_components/angular-loader/angular-loader.js"             # angular-loader
        "bower_components/angular-material/angular-material.js"         # angular-material
        "bower_components/angular-mocks/angular-mocks.js"               # angular-mocks
        "bower_components/angular-route/angular-route.js"               # angular-route
        "bower_components/angular-sanitize/angular-sanitize.js"         # angular-sanitize
    ]
}


######################################
## HTML
######################################

gulp.task "_html-partials", ->
    gulp.src(paths.jade.partials)
        .pipe(plumber())
        .pipe(cache("jade"))
        .pipe(jadeInheritance({basedir: "#{paths.app}/partials/"}))
        .pipe(jade({pretty: true}))
        .pipe(gulp.dest("#{paths.dist}/partials"))

gulp.task "_html-index", ->
    locals = {v: (new Date()).getTime()}

    gulp.src(paths.jade.index)
        .pipe(plumber())
        .pipe(jade({pretty: true, locals: locals}))
        .pipe(gulp.dest(paths.dist))


######################################
## CSS
######################################

gulp.task "_css-app", ->
    # TODO

gulp.task "_del_css-app", (cb) ->
    del(["#{paths.tmp}/vendor.css"], cb)


gulp.task "_css-vendor", ->
    gulp.src(paths.css)
        .pipe(concat("vendor.css"))
        .pipe(gulp.dest(paths.tmp))

gulp.task "_del_css-vendor", (cb )->
    del(["#{paths.tmp}/app.css"], cb)


gulp.task "_css", ["_del_css-app", "_css-app", "_del_css-vendor", "_css-vendor"], ->
    tmp_paths = [
        "#{paths.tmp}/vendor.css",
        "#{paths.tmp}/app.css"
    ]

    gulp.src(tmp_paths)
        .pipe(concat("main.css"))
        .pipe(gulp.dest("#{paths.dist}/styles/"))


######################################
## JS
######################################

gulp.task "_js-app", ->
    gulp.src(paths.coffee)
        .pipe(plumber())
        .pipe(coffee())
        .pipe(concat("app.js"))
        .pipe(gulp.dest("dist/js/"))

gulp.task "_js-libs", ->
    gulp.src(paths.js)
        .pipe(plumber())
        .pipe(concat("libs.js"))
        .pipe(gulp.dest("dist/js/"))


######################################
## DEV ENV
######################################

gulp.task "_dev-server", ->
    express = require "express"
    app = express()

    app.use("/js", express.static("#{__dirname}/dist/js"))
    app.use("/styles", express.static("#{__dirname}/dist/styles"))
    #app.use("/images", express.static("#{__dirname}/dist/images"))
    #app.use("/svg", express.static("#{__dirname}/dist/svg"))
    app.use("/partials", express.static("#{__dirname}/dist/partials"))
    #app.use("/fonts", express.static("#{__dirname}/dist/fonts"))

    app.all "/*", (req, res, next) ->
        # Just send the index.html for other files to support HTML5Mode
        res.sendFile("index.html", {root: "#{__dirname}/dist/"})

    app.listen(9001)


gulp.task "_dev-watch", ->
    gulp.watch     paths.jade.index,       ["_html-index"]
    gulp.watch     paths.jade.partials,    ["_html-partials"]
    gulp.watch     paths.css,              ["_css"]
    gulp.watch     paths.coffee,           ["_js-app"]
    gulp.watch     paths.js,               ["_js-libs"]


######################################
## MEIN TASKS
######################################

gulp.task "default", [
    "_html-index"
    "_html-partials"
    "_css"
    "_js-libs"
    "_js-app"
    "_dev-server"
    "_dev-watch"
]
