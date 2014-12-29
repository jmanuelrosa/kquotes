from uuslug import uuslug


def slugify_uniquely(text, instance, separator="-", max_length=0):
    return uuslug(text, instance=instance, separator=separator, max_length=max_length)
