kquotes = @.kquotes

module = angular.module("kquotesBase")


momentFormat = ->
    return (input, format) ->
        if input
            return moment(input).format(format)
        return ""

module.filter("momentFormat", momentFormat)


momentFromNow = ->
    return (input, without_suffix) ->
        if input
            return moment(input).fromNow(without_suffix or false)
        return ""

module.filter("momentFromNow", momentFromNow)


nl2br = ->
    return (msg, is_xhtml) ->
        breakTag = if is_xhtml? then '<br />' else '<br>'

        msg = "#{msg}".replace(/([^>\r\n]?)(\r\n|\n\r|\r|\n)/g, "$1#{breakTag}$2")
        return msg

module.filter("nl2br", nl2br)
