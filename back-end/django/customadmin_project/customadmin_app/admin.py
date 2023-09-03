from django.contrib import admin
from . import models

# Register your models here.
class  MovieAdmin(admin.ModelAdmin):

    ## ORDERING FIELDS...
    fields = ["release_year", "title", "length"]

    ## ADDING SEARCH...
    ### It's possible to add as many fields as you want, but the more fields you add
    ### the longer it's going to take to search.
    search_fields = ["title"]

    ## ADDING FILTERS...
    ### Not all the fields are good filtering options
    list_filter = ["release_year", "length"]

    ## ADDING FIELDS
    ### This overrides the ## ORDERING FIELDS part
    list_display = ["release_year", "length", "release_year"]

    ## EDITABLE LIST VIEW
    list_editable = ["length"]
    


admin.site.register(models.Movie, MovieAdmin)
admin.site.register(models.Customer)
